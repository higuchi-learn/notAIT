import random

p_ichi = 1
c_ichi = 1

def banmen():
    global p_ichi,c_ichi
    p_ichi = draw_banmen(p_ichi)
    c_ichi = draw_banmen(c_ichi)

def draw_banmen(ichi):
    if  ichi < 17 :
        print("P:"+"・" * (ichi-1)+"●"+"・" * (17-ichi-1) + "★" + "・" * 13 + "Goal")
    elif ichi > 17:
        print("P:"+"・" * 16 +"★" + "・" * (ichi-17-1) +"●" + "・" * (30-ichi) + "Goal")
    elif ichi == 17:
        print("P:"+"・" * 16+"●"+"・" * 13 + "Goal")
        ichi -= 5
        print("5マス戻ります")
        print("P:"+"・" * (ichi-1)+"●"+"・" * (17-ichi-1) + "★" + "・" * 13 + "Goal")
    return ichi

def sugoroku(ichi, target):
    input(f"Enterキーを押すと{target}のコマが進みます")
    r = random.randint(1, 6)
    print("「" + str(r) + "」" + "進みます")
    ichi += r
    if ichi > 30:
        ichi = 30
    return ichi

banmen()
print("\n")
while True:
    p_ichi = sugoroku(p_ichi,"プレイヤー")
    banmen()
    if p_ichi == 30:
        print("プレイヤーの勝ちです")
        break
    print("\n")
    c_ichi = sugoroku(c_ichi,"コンピューター")
    banmen()
    if p_ichi == 30:
        print("コンピューターの勝ちです")
        break
    print("\n")