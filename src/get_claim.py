def read_news_from_file(filepath="新闻.txt"):
    try:
        with open(filepath,"r",encoding="utf-8")as f:
            news=f.read()
        return news
    except Exception as e:
        print(f"读取文件时出错:{e}")
        return None
