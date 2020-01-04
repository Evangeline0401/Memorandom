#Classについてのチュートリアル

from menu_item import MenuItem

# ここでインスタンスの作成
menu_item1 = MenuItem('サンドイッチ', 500)
menu_item2 = MenuItem('チョコケーキ', 400)
menu_item3 = MenuItem('コーヒー', 300)
menu_item4 = MenuItem('オレンジジュース', 200)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

index = 0

for menu_item in menu_items:
    # menu_item.info()でmenu_itemを使ってメソッド2を呼び出している
    print(str(index) + '. ' + menu_item.info())
    index += 1

print('--------------------')

order = int(input('メニューの番号を入力してください: '))
selected_menu = menu_items[order]
print('選択されたメニュー: ' + selected_menu.name) # selected_menu.nameで選ばれたメニューのnameを表示

# コンソールから入力を受け取り、変数countに代入してください
count = int(input("個数を入力してください(3つ以上で1割引): "))

# get_total_priceメソッドを呼び出してください
result = selected_menu.get_total_price(count) # countを引数としてメソッド3を呼び出している

# 「合計は〇〇円です」となるように出力してください
print("合計は" + str(result) + "円です")
