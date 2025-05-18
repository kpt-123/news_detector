import tiktoken
max_token=100000

def count_tokens(prompt,text):
    enc=tiktoken.encoding_for_model("gpt-4o")
    full_input=prompt+"\n\n"+text
    #编码并统计tokens数
    tokens=enc.encode(full_input)
    tokens_count=len(tokens)
    if tokens_count>max_token:
        #print("已经超出了LLMtokens上限,并对文档进行切割")
        return False
    else :
        return True
