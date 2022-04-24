import DirModule
import FileModule

#DirModule.file_extname_changed('テストデータ\テスト2','tsv','csv')


files = FileModule.file_read('テストデータ\テスト3\キーワード.txt')

print("============================================================")
for file in files:
    print(file)

