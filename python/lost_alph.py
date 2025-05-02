import time
n = 0
FREQUENCY = 5
mistake_count = 0
total_score = 0
while True :
    n += 1
    print(f"-*-*-*- {n}回目 -*-*-*-")
    print("消える文字以外の文字列は？")
    input_string = input()
    i = 0
    while True :
        interval = ord(input_string[i+1]) - ord(input_string[i])
        if interval == 2 :
            lost_alphabet = chr(ord(input_string[i])+1)
            break
        i += 1

    start_time = time.time()
    while True :
        print("消えている文字は？", end = "")
        ans_alphabet = input()
        if lost_alphabet == ans_alphabet :
            print("正解です")
            end_time = time.time()
            break
        else :
            print("違います")
            mistake_count += 1
    answering_time = end_time - start_time
    get_point = 12 - answering_time + 0.5
    answering_time = int(answering_time)
    get_point = int(get_point)
    if get_point < 0 :
        get_point = 0
    total_score += get_point
    print(f"{answering_time}秒かかりました")
    print(f"{get_point}点GET！ total_score = {total_score}\n\n")
    if n == FREQUENCY :
        break

print(f"合計スコア : {total_score}")
print(f"間違えた回数 : {mistake_count}")
final_score = total_score - mistake_count
print(f"最終スコア : {final_score}")
