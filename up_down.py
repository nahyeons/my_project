import random

while True:
    random_number = random.randint(1, 100)
    try_count = 1 # 시도 횟수!

    while True:
        try:   
            my_number = int(input("🎮1~100 사이 숫자를 입력해보세요 👾")) 

            if my_number > random_number:
                print("down⬇️")
            elif my_number < random_number:
                print("up⬆️")
            else:
                print(f"👏👏정답입니다~ 🥳 {try_count}회 만에 맞췄네요!👏👏") # f-sting 으로 시도 횟수도 나오게 해야징
                break # 여기서 정답 맞추면 종료하고

            try_count = try_count + 1

        except ValueError: #'excep:' 에서 ValueError 사용하니까 에러 안나..
            print("🚨 삐삐- Error 발생! 🤬 숫자로 입력해야죠!! 🚨")

        #요기서 계속 샐행 물어봐주고!
    play_again = input("한 번 더 하실래요? (yes/no) ")  
    if play_again.lower() == 'no': # 요기서 yes or no 판단!
        print("-----Game Over-----") #'!=' : 같지않다 / '==' 같다 
        break                        # play_again.lower() != 'yes' 도 같은 말이라 실행 됨!!