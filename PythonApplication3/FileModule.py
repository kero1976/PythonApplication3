def file_read(filePath):
    """
    ファイルを読み込み、リストにして返す
    """
    with open(filePath,'r') as f:
        return f.read().splitlines()

def file_replace_comment(filePath,keywords):
    """
    キーワードが入っている行の先頭にコメントを付与する
    """
    datas = file_read(filePath)
    result =[]

    for data in datas:
        index = 0
        while index < len(keywords):
            if(data.find(keywords[index]) != -1):
                result.append("//" + keywords[index] + "//" + data)
                break
            else:
                index += 1
        else:
            result.append(data)

    with open(filePath, mode='w') as f:
        f.write('\n'.join(result))

def create_keyword(filePath):
    lines = file_read(filePath)
    return set(lines)