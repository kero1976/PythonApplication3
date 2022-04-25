import csv

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
    return sorted(set(lines), reverse=True)


def creat_csv_keyword(filePath):
    """
    変更前キーワード、変更後キーワードの形式
    """
    lines = create_keyword(filePath)
    result = []
    for line in lines:
        result.append(line.split(','))
    return result

def file_replace_comment2(filePath,keywords):
    """
    キーワードを変更後に置換する
    """
    datas = file_read(filePath)
    result =[]

    for data in datas:
        index = 0
        while index < len(keywords):
            if(data.find(keywords[index][0]) != -1):
                result.append(data.replace(keywords[index][0],keywords[index][1]))
                break
            else:
                index += 1
        else:
            result.append(data)

    with open(filePath, mode='w') as f:
        f.write('\n'.join(result))