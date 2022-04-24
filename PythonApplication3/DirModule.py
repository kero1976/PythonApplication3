import glob
import logging
import os

formatter = "%(asctime)s:%(funcName)s:%(message)s"
logging.basicConfig(level=logging.DEBUG, format=formatter)

def file_names(dir):
    """
    指定した引数のフォルダにあるファイルをすべて返す
    フォルダは返さない
    """
    logging.debug('パラメータ:{}'.format(dir))
    result = []
    files = glob.glob(dir + "\**", recursive=True)
    for file in files:
        if os.path.isdir(file):
            logging.debug('{} is Directory'.format(file))
        else:
            logging.debug('{} is File'.format(file))
            result.append(file)

    logging.debug("END")
    return result

def file_extname_changed(dir,old,new):
    """
    指定したフォルダ内のファイルの拡張子を変更する。
    """
    files = file_names(dir)
    for file in files:
        if(file.endswith(old)):
            os.rename(file, file[:-len(old)] + new)

