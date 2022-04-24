import DirModule
import FileModule

#DirModule.file_extname_changed('テストデータ\テスト2','tsv','csv')


keys = FileModule.file_read('テストデータ\テスト3\キーワード.txt')
FileModule.file_replace_comment('テストデータ\テスト3\入力ファイル.txt', keys)

print("============================================================")

