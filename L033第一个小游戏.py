import random

secret = random.randint(1, 10)
print('------------------我爱鱼C工作室------------------')

try:
    temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")

except (EOFError, KeyboardInterrupt):
    print('\n输入错误')

else:
    while 1:
        try:
            guess = int(temp)
            break
        except ValueError:
            print('您输入不是数字，请重新输入：', end='')
            temp = input()

    while guess != secret:
        temp = input("哎呀，猜错了，请重新输入吧：")
        while 1:
            try:
                guess = int(temp)
                break
            except ValueError:
                print('您输入不是数字，请重新输入：', end='')
                temp = input()
        if guess == secret:
            print("我草，你是小甲鱼心里的蛔虫吗？！")
            print("哼，猜中了也没有奖励！")
        else:
            if guess > secret:
                print("哥，大了大了~~~")
            else:
                print("嘿，小了，小了~~~")
    print("游戏结束，不玩啦^_^")

