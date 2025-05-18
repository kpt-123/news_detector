
def should_print_result(response_text,threhold=0.5):
    lines=response_text.strip().split("\n")
    if len(lines)<3:
        return False#格式不对
    lable=lines[0].strip()
    try:
        confidence=float(lines[1].strip())
    except ValueError:
        return False#置信度解析失败
    if lable in ["True","False"] and confidence>=threhold:
        #print("结果为:"+response_text)
        return True
    return False