import DirModule

DirModule.file_extname_changed('テストデータ\テスト2','tsv','csv')

str = "abccsvdef.csv"
ext = "csv"

print(str[:-len(ext)])