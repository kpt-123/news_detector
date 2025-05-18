import count_tokens
import chromadb
from  tools import ollama_embedding_by_api
import uuid
import count_tokens
from chromadb.errors import NotFoundError

def collection_exists(client, name):
    try:
        client.get_collection(name=name)
        return True
    except NotFoundError:
        return False

#按照段落划分过滤空行和超短段落
def split_text(text):
    return [p.strip() for p in text.split("\n") if len(p.strip()) > 5]

def collection_exists(client, name):
    try:
        client.get_collection(name=name)
        return True
    except NotFoundError:
        return False
    
#将texts中的每一个段落向量化,并且存入chromadb中
def initial(text):
    texts=split_text(text) #按照段落划分过滤空行和超短段落
    client=chromadb.PersistentClient(path="E:\新闻检测\db\claim_relevant")
    if collection_exists(client,name="claim_env"): #如果存在claim_relevant集合，就删除
        client.delete_collection(name="claim_env")
    collection=client.get_or_create_collection(name="claim_env") #创建claim_relevant集合
    ids=[str(uuid.uuid4()) for _ in range(len(texts))] #生成id
    embeddings=[ollama_embedding_by_api(text) for text in texts] #向量化
    collection.add( #添加到chromadb中
        documents=texts,
        embeddings=embeddings,
        ids=ids
    )
#查找最相关的段落
def search_similai_paragraphs(claim,top_k=1):
    client=chromadb.PersistentClient(path="db/claim_relevant") #连接数据库
    collection=client.get_collection(name="claim_env") #连接集合
    claim_embedding=ollama_embedding_by_api(claim) #向量化
    res=collection.query(query_embeddings=claim_embedding,n_results=top_k) #查找最相关的段落
    result=res["documents"][0] #获取最相关的段落
    id=res["ids"][0] #获取最相关的段落的id
    collection.delete(ids=id) #删除最相关的段落
    return result[0]
    
def generate_env(claim,prompt,text):
    initial(text)
    result=search_similai_paragraphs(claim) #查找最相关的段落
    while count_tokens.count_tokens(prompt,result): #判断是否超出了LLMtokens上限，如果没有超出，就进行下一步
        #print("未超出LLMtokens上限")
        prompt=prompt+result+"\n\n"#将网页的正文内容插入到prompt中，作为证据
        result=search_similai_paragraphs(claim) #查找最相关的段落
    return prompt
    