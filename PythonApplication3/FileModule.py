def file_read(filePath):
    """
    ファイルを読み込み、リストにして返す
    """
    with open(filePath,'r') as f:
        return f.read().splitlines()

def file_replace(filePath,list):
    with open(filePath,'r') as f:
        