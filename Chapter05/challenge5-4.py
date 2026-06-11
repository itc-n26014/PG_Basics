takaya = {
        "名前": "高屋星那",
        "身長": "170",
        "好きなこと": "音楽を聞く,ゲーム,漫画",
        "好きな作家": "知念実希人",
        "苦手なもの": "野菜,勉強"}

ask = input("知りたい情報を入力してください。")
if ask in takaya:
    answer = takaya[ask]
    print(answer)
else:
    print("見つかりませんでした。")
