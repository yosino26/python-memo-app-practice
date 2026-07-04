defshow_menu():
print("==== メモ管理アプリ ====")
print("1. メモを追加")
print("2. メモ一覧を見る")
print("3. メモを検索")
print("4. メモを削除")
print("5. 終了")


whileTrue:
show_menu()

choice=input("番号を選んでください: ")

whileTrue:
show_menu()

choice=input("番号を選んでください: ")

ifchoice=="1":
print("メモを追加します")
elifchoice=="2":
print("メモ一覧を表示します")
elifchoice=="3":
print("メモを検索します")
elifchoice=="4":
print("メモを削除します")
elifchoice=="5":
print("アプリを終了します")
break
else:
print("1〜5の番号を入力してください")