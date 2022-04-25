import DirModule
import FileModule
import ExcelModule
import collections

#DirModule.file_extname_changed('テストデータ\テスト2','tsv','csv')


#keys = FileModule.creat_csv_keyword('テストデータ\テスト4\キーワード.txt')
#FileModule.file_replace_comment2('テストデータ\テスト4\入力ファイル.txt', keys)

print("============================================================")

sheets = ExcelModule.excel_read_sheet_name('テストデータ\テスト5\テスト.xlsx')
cols = ExcelModule.excel_read_sheet('テストデータ\テスト5\テスト.xlsx', sheets[1])


for col in cols:
    print(col)

c = collections.Counter(cols)
print(c)