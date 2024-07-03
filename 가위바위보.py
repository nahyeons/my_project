import random

choices = ["가위", "바위", "보"] 

print("🎮가위, 바위, 보 게임👾")

while True:
    player = input("🤫가위, 바위, 보 중 하나를 선택하세요🤔")
    my_choice = random.choice(choices)
    print(F"😎사용자: {player} 💻 컴퓨터: {my_choice}")

    if player == my_choice:
        print("wow 비겼어요!")
    elif player == "가위":
        if my_choice == "보":
            print("🥳 이겼어요! 👏👏")
        else:
            print("😅 이런! 졌네요..다시해봐요 🍀")
    elif player == "바위":
        if my_choice == "가위":
            print("🥳 이겼어요! 👏👏")
        else:
            print("😅 이런! 졌네요..다시해봐요 🍀")
    elif player == "보":
        if my_choice == "바위":
            print("🥳 이겼어요! 👏👏")
        else:
            print("😅 이런! 졌네요..다시해봐요 🍀")

    else:
        print("🚨Error🚨 가위, 바위, 보 중에서 다시 골라보세요 😇")

    play_again = input("게임을 다시 하시겠습니까? (yes or no) ")   # 플레이 
    if play_again.lower() == 'no':
        print("-----Game Over-----")
        break 