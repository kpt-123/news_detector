import search
import count_tokens
import generate_env
import GPT_generate
import should_print_result
import get_claim
import replace_block
import fake_news_web
claim=get_claim.read_news_from_file("E:\新闻检测\src\新闻.txt")

fake_news_domains=[] #假新闻网站的域名列表
fake_news_domains=fake_news_web.get_fake_news_web()
threshold=0.5
search_suggest=claim

searched_urls=[]
query_count=0
prompt_template = f"""
请根据已有信息判断新闻的真实性，并严格按照以下格式输出（共3行）：

1. 如果判断为真实，请输出：
True
(置信度0~1之间的小数)
解释性语句

2. 如果判断为虚假，请输出：
False
(置信度0~1之间的小数)
解释性语句

3. 如果证据不足，请输出：
NEI
证据的摘要(请仅压缩提取现有证据中**明确提到的客观事实内容**，不要加入任何主观判断、结论或倾向性词语（如“未证实”“未找到”“没有证据表明”""未提及""等），不要推测新闻真伪，仅对证据文本进行简洁提取。)
建议下一步的查询的关键词(具体且明确的下一步查询建议，内容包括待查询的重点问题或者方向的关键词,已经查询过网址:{{searched_urls}},请勿提供类似查询方向的关键词)

⚠️ 重要要求：
- 输出必须严格是三行（不多不少）。
- 不要添加“下一步查询建议”、“更多解释”、空行或任何额外信息。
- 每一行之间只使用一个换行符 `\\n`。
- 任何超出三行的内容都将视为错误输出。

新闻内容：{claim}

证据：
"""

urls=search.first_search(search_suggest) #使用bing search api进行搜索
filtered_urls=search.filter_fake_news_sites(urls,fake_news_domains) #过滤假新闻网站
texts=[] #存储网页正文内容
url_count=0
for url in filtered_urls: #遍历过滤后的网址列表，对每个网址进行抓取
    text=search.extract_text_from_url(url) #抓取网页正文内容
    texts.append(text) #将网页正文内容添加到texts列表中
#遍历每个网页正文内容,并将其加入到证据中,直到达到LLM的tokens上限为止,如果超出了LLM的tokens上限,就调用generate_env.py中的generate_env函数,生成新的prompt
for text in texts: 
    if count_tokens.count_tokens(prompt_template,text)==True: #判断是否超出了LLMtokens上限，如果没有超出，就进行下一步
        #print("未超出LLMtokens上限")
        url_count=url_count+1
        prompt_template=prompt_template+text+"\n\n"#将网页的正文内容插入到prompt中，作为证据
    else:
        prompt_template=generate_env.generate_env(search_suggest,prompt_template,text) #如果超出了LLMtokens上限，就调用generate_env.py中的generate_env函数，生成新的prompt
        break
searched_urls+=filtered_urls[0:url_count]
urls_text=",".join(searched_urls)
prompt=prompt_template.replace("{searched_urls}",urls_text)

while True:
    if query_count>1:
        prompt=replace_block.replace_block(prompt,"请根据已有信息判断新闻的真实性，并严格按照以下格式输出（共3行）","""⚠️ 重要要求：
- 输出必须严格是三行（不多不少）。
- 不要添加“下一步查询建议”、“更多解释”、空行或任何额外信息。
- 每一行之间只使用一个换行符 `\\n`。
- 任何超出三行的内容都将视为错误输出。""","""请根据已有信息判断新闻的真实性，并严格按照以下格式输出（共3行）：

1. 如果判断为真实，请输出：
True
(置信度0~1之间的小数)
解释性语句

2. 如果判断为虚假，请输出：
False
(置信度0~1之间的小数)
解释性语句


⚠️ 重要要求：
- 输出必须严格是三行（不多不少）。
- 不要添加“下一步查询建议”、“更多解释”、空行或任何额外信息。
- 每一行之间只使用一个换行符 `\\n`。
- 任何超出三行的内容都将视为错误输出。""")
        
    result=GPT_generate.gpt_generate(prompt) #调用GPT_generate.py中的gpt_generate函数，生成回复
    query_count+=1
    print(result)
    lines=result.strip().split("\n")
    label=lines[0].strip()
    if label in ["True","False"]:
        confidence=float(lines[1].strip())
        explanation=lines[2].strip
    else:
        env=lines[1].strip()
        search_suggest=lines[2].strip()
    flag=should_print_result.should_print_result(result,threshold)
    if flag:
        break
    else:
        if label=="NEI":
            prompt_template = f"""
请根据已有信息判断新闻的真实性，并严格按照以下格式输出（共3行）：

1. 如果判断为真实，请输出：
True
(置信度0~1之间的小数)
解释性语句

2. 如果判断为虚假，请输出：
False
(置信度0~1之间的小数)
解释性语句

3. 如果证据不足，请输出：
NEI
证据的摘要(请仅压缩提取现有证据中**明确提到的客观事实内容**，不要加入任何主观判断、结论或倾向性词语（如“未证实”“未找到”“没有证据表明”""未提及""等），不要推测新闻真伪，仅对证据文本进行简洁提取。)
建议下一步的查询的关键词(具体且明确的下一步查询建议，内容包括待查询的重点问题或者方向的关键词,已经查询过网址:{{searched_urls}},请勿提供类似查询方向的关键词)

⚠️ 重要要求：
- 输出必须严格是三行（不多不少）。
- 不要添加“下一步查询建议”、“更多解释”、空行或任何额外信息。
- 每一行之间只使用一个换行符 `\\n`。
- 任何超出三行的内容都将视为错误输出。

新闻内容：{claim}

证据：{env}
"""
           
            urls=search.tavily_search(search_suggest) #使用bing search api进行搜索
            filtered_urls=search.filter_fake_news_sites(urls,fake_news_domains) #过滤假新闻网站
            texts=[] #存储网页正文内容
            url_count=0
            for url in filtered_urls: #遍历过滤后的网址列表，对每个网址进行抓取
                text=search.extract_text_from_url(url) #抓取网页正文内容
                texts.append(text) #将网页正文内容添加到texts列表中
            #遍历每个网页正文内容,并将其加入到证据中,直到达到LLM的tokens上限为止,如果超出了LLM的tokens上限,就调用generate_env.py中的generate_env函数,生成新的prompt
            for text in texts: 
                if count_tokens.count_tokens(prompt_template,text)==True: #判断是否超出了LLMtokens上限，如果没有超出，就进行下一步
                    #print("未超出LLMtokens上限")
                    url_count=url_count+1
                    prompt_template=prompt_template+text+"\n\n"#将网页的正文内容插入到prompt中，作为证据
                else:
                    prompt_template=generate_env.generate_env(search_suggest,prompt_template,text) #如果超出了LLMtokens上限，就调用generate_env.py中的generate_env函数，生成新的prompt
                    break
            searched_urls+=filtered_urls[0:url_count]
            urls_text=",".join(searched_urls)
            prompt=prompt_template.replace("{searched_urls}",urls_text)
           
        else:
            if "证据为:" in prompt:
                env=prompt.split("证据为:")[1].strip()
                prompt = f"""
新闻内容：
{claim}

已有证据：
{env}

上一次模型判断：
{label}
{confidence}
{explanation}

新的任务要求：

由于置信度低于阈值，无法直接判断新闻真实性，请严格执行以下步骤：

1. 提炼已有信息，生成一个压缩后的证据信息摘要(尽量详细一些)；
2. 根据目前不确定性，提出下一步可查询的方向或建议的问题；
3. **严格只返回以下两行内容，中间用换行符分隔，不得添加其他内容、解释或多余空行：**

压缩证据:证据的摘要(请仅压缩提取现有证据中**明确提到的客观事实内容**，不要加入任何主观判断、结论或倾向性词语（如“未证实”“未找到”“没有证据表明”""未提及""等），不要推测新闻真伪，仅对证据文本进行简洁提取。)
建议下一步的查询的关键词(具体且明确的下一步查询建议，内容包括待查询的重点问题或者方向的关键词,已经查询过网址:{searched_urls},请勿提供类似查询方向的关键词)

请务必只返回上述格式的两行文本，任何多余内容都视为格式错误。
"""

                result=GPT_generate.gpt_generate(prompt)
                env=result.split("压缩证据:")[1].split("\n")[0].strip()
                prompt_template = f"""
请根据已有信息判断新闻的真实性，并严格按照以下格式输出（共3行）：

1. 如果判断为真实，请输出：
True
(置信度0~1之间的小数)
解释性语句

2. 如果判断为虚假，请输出：
False
(置信度0~1之间的小数)
解释性语句

3. 如果证据不足，请输出：
NEI
证据的摘要(请仅压缩提取现有证据中**明确提到的客观事实内容**，不要加入任何主观判断、结论或倾向性词语（如“未证实”“未找到”“没有证据表明”""未提及""等），不要推测新闻真伪，仅对证据文本进行简洁提取。)
建议下一步的查询的关键词(具体且明确的下一步查询建议，内容包括待查询的重点问题或者方向的关键词,已经查询过网址:{{searched_urls}},请勿提供类似查询方向的关键词)

⚠️ 重要要求：
- 输出必须严格是三行（不多不少）。
- 不要添加“下一步查询建议”、“更多解释”、空行或任何额外信息。
- 每一行之间只使用一个换行符 `\\n`。
- 任何超出三行的内容都将视为错误输出。

新闻内容：{claim}

证据：{env}
"""
                #env=result.strip().split("\n")[0]
                search_suggest=result.split("下一步查询建议:")[1].strip()
                #search_suggest=result.strip().split("\n")[1]
                
                urls=search.tavily_search(search_suggest) #使用bing search api进行搜索
                filtered_urls=search.filter_fake_news_sites(urls,fake_news_domains) #过滤假新闻网站
                texts=[] #存储网页正文内容
                url_count=0
                for url in filtered_urls: #遍历过滤后的网址列表，对每个网址进行抓取
                    text=search.extract_text_from_url(url) #抓取网页正文内容
                    texts.append(text) #将网页正文内容添加到texts列表中
                #遍历每个网页正文内容,并将其加入到证据中,直到达到LLM的tokens上限为止,如果超出了LLM的tokens上限,就调用generate_env.py中的generate_env函数,生成新的prompt
                for text in texts: 
                    if count_tokens.count_tokens(prompt_template,text)==True: #判断是否超出了LLMtokens上限，如果没有超出，就进行下一步
                        #print("未超出LLMtokens上限")
                        url_count=url_count+1
                        prompt_template=prompt_template+text+"\n\n"#将网页的正文内容插入到prompt中，作为证据
                    else:
                        prompt_template=generate_env.generate_env(search_suggest,prompt_template,text) #如果超出了LLMtokens上限，就调用generate_env.py中的generate_env函数，生成新的prompt
                        break
                searched_urls+=filtered_urls[0:url_count]
                urls_text=",".join(searched_urls)
                prompt=prompt_template.replace("{searched_urls}",urls_text)



