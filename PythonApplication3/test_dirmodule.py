import DirModule

def test_passing():
    files = DirModule.file_names('テストデータ\テスト1')
    assert files == ['テストデータ\テスト1\ABC\TextFile1.txt','テストデータ\テスト1\ABC\TextFile2.txt','テストデータ\テスト1\DEF\XYZ\TextFile3.txt']