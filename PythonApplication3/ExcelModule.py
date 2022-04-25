import pandas as pd

"""
pandasと???をpipでインストールする
"""


def excel_read_sheet_name(filePath):
    """
    EXCELファイルのシート名を取得する
    """
    book = pd.ExcelFile(filePath)
    return book.sheet_names

def excel_read_sheet(filePath, sheet):
    """
    指定したシートの特定列のデータを取得する
    """
    book = pd.ExcelFile(filePath)
    df = book.parse(sheet)
    return df.iloc[:,1]
