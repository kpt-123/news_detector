import re
def replace_block(prompt: str,start_text:str,end_text:str,new_content):
    # 构建非贪婪正则：从 start 到 end 的中间内容全部替换
    pattern = re.escape(start_text) + r'.*?' + re.escape(end_text)
    
    return re.sub(pattern, new_content, prompt, flags=re.DOTALL)
