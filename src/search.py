import requests
from urllib.parse import urlparse
import trafilatura
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
from newspaper import Article
import undetected_chromedriver as uc

chrome_version=136
api_key="your_key"
#使用bing search api进行搜索



def format_to_tavily_query(text):
    # 替换中文、英文逗号为空格，再用空格切分
    tokens = re.split(r"[，,、\s]+", text.strip())

    # 去重 + 去除空字符串
    tokens = list({t.strip() for t in tokens if t.strip()})

    # 每个关键词加双引号
    quoted = [f'"{token}"' for token in tokens]
    
    # 拼接成查询字符串（空格分隔，表示 AND 逻辑）
    return " ".join(quoted)
def first_search(claim):
   
    print(claim)
    url = "https://api.tavily.com/search"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "query": claim,
        "num_results": 10
    }
    response = requests.post(url, headers=headers, json=payload)  # ✅ 用 POST
    results = response.json()

    urls = [item["url"] for item in results.get("results", [])]
    return urls

def tavily_search(claim):
    claim=format_to_tavily_query(claim)
    print(claim)
    url = "https://api.tavily.com/search"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "query": claim,
        "num_results": 10
    }
    response = requests.post(url, headers=headers, json=payload)  # ✅ 用 POST
    results = response.json()

    urls = [item["url"] for item in results.get("results", [])]
    return urls




#过滤假新闻网站
def filter_fake_news_sites(urls,fake_news_domains):
    # 过滤假新闻网站的域名
    filtered_urls=[]
    for url in urls:
        domain=urlparse(url).netloc.replace("www.","") #获取域名
        if domain not in fake_news_domains: #如果域名不在假新闻网站的域名列表中，就添加到filtered_urls中
            filtered_urls.append(url)
    return filtered_urls




def extract_with_selenium(url):
    # 设置反爬浏览器参数
    options = uc.ChromeOptions()
    options.add_argument("--headless")  # 可选，去掉这行能看到真实浏览器
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

    # 启动无检测的浏览器
    driver = uc.Chrome(options=options, headless=True,version_main=chrome_version)
    
    try:
        driver.get(url)
        time.sleep(5)  # 等待 JS 渲染（视网站复杂度可以调整时间）

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        # 优先查找 <article> 标签
        article = soup.find("article")
        if article:
            return article.get_text(strip=True)
        
        # 否则返回全页面文本
        body = soup.find("body")
        return body.get_text(strip=True) if body else None

    except Exception as e:
        print(f"[Selenium 提取失败]：{e}")
        return None

    finally:
        driver.quit()

def detect_language_from_url(url):
    # 简单判断是否为中文网站：.cn 域名或 URL 中含中文字符
    if '.cn' in url or re.search(r'[\u4e00-\u9fff]', url):
        return 'zh'
    return 'en'
#抓取网页正文内容
def extract_text_from_url(url):
    lang=detect_language_from_url(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        html = None

        if response.status_code == 200:
            html = response.text
            text = trafilatura.extract(html)
            if text:
                return text.strip()

    except requests.exceptions.RequestException as e:
        print(f"请求异常：{e}")

    # 如果 requests 失败或者 trafilatura 提取失败，尝试 Selenium
    article = extract_with_selenium(url)
    if article:
        return article

    # 如果 Selenium 失败，尝试 newspaper3k
    try:
        article = Article(url, language=lang)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print(f"newspaper3k 抓取失败：{e}")
        return None



