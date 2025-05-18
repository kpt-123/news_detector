import requests
import functools
import uuid
import chromadb


#1.读取文件内容
def file_chunk_list():
    with open ("knowledge\新闻知识.txt",encoding="utf-8",mode="r") as  fp:
        data=fp.read()
    #根据换行切割
    chunk_list=data.split("\n\n")
    chunk_list=[chunk for chunk in chunk_list if chunk]
    return chunk_list


#向量化
def ollama_embedding_by_api(text):
    res=requests.post(
        url="http://127.0.0.1:11434/api/embeddings",
        json={
            "model":"nomic-embed-text",
            "prompt":text
        }
    )
    embedding=res.json()["embedding"]
    return embedding
def initial():
    client=chromadb.PersistentClient(path="db/chroma_demo") #数据库 类似于文件夹
    if client.get_collection(name="collection_v1"):
        client.delete_collection(name="collection_v1")
    collection=client.get_or_create_collection(name="collection_v1")  #集合 类似于表格
    documents=file_chunk_list()
    ids=[str(uuid.uuid4()) for _ in range(len(documents))] 
    embeddings=[ollama_embedding_by_api(document) for document in documents]
    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=ids
    )
def ollama_generate_by_api(prompt):
    response=requests.post(
        url="http://127.0.0.1:11434/api/generate",
        json={
            "model":"deepseek-r1:1.5b",
            "prompt":prompt, 
            "stream":False,
            "temperature":0.1
        }
    )
    res=response.json()["response"]
    return res
def run():
    key_word="感冒胃疼"
    key_word_embedding=ollama_embedding_by_api(key_word)
    collection=chromadb.PersistentClient(path="db/chroma_demo").get_collection(name="collection_v1")
    res=collection.query(query_embeddings=key_word_embedding,n_results=2)
    result=res["documents"][0]
    context="\n".join(result)
    print(context)
    prompt=f"""
    你是新闻鉴别器，根据下面的参考信息:{context}回答用户的问题:{key_word}。
    """
    result=ollama_generate_by_api(prompt)
    print(result)
