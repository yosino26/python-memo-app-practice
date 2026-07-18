memos = []


def show_menu():
    print("==== メモ管理アプリ ====")
    print("1. メモを追加")
    print("2. メモ一覧を見る")
    print("3. メモを検索")
    print("4. メモを削除")
    print("5. 終了")


def add_memo():
    memo = input("追加するメモを入力してください: ")
    memos.append(memo)
    print("メモを追加しました")


def show_memos():
    if len(memos) == 0:
        print("メモはまだありません")
    else:
        print("==== メモ一覧 ====")
        for index, memo in enumerate(memos, start=1):
            print(f"{index}. {memo}")


def search_memos():
    keyword = input("検索するキーワードを入力してください: ")

    found = False

    print("==== 検索結果 ====")

    for index, memo in enumerate(memos, start=1):
        if keyword in memo:
            print(f"{index}. {memo}")
            found = True

    if not found:
        print("該当するメモはありません")

def delete_memo():
    if len(memos) == 0:
        print("削除できるメモはありません")
        return

    show_memos()
    
    delete_number = input("削除するメモの番号を入力してください: ")

    if not delete_number.isdigit():
        print("番号を入力してください")
        return

    delete_index = int(delete_number) - 1

    if delete_index < 0 or delete_index >= len(memos):
        print("存在しない番号です")
        return     
    deleted_memo = memos.pop(delete_index)
    print(f"メモを削除しました: {deleted_memo}")        


while True:
    show_menu()

    choice = input("番号を選んでください: ")

    if choice == "1":
        add_memo()
    elif choice == "2":
        show_memos()
    elif choice == "3":
        search_memos()
    elif choice == "4":
        delete_memo()
    elif choice == "5":
        print("アプリを終了します")
        break
    else:
        print("1〜5の番号を入力してください")