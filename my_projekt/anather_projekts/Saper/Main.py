from BoardClass import Board

def Start():
    print("Enter Size plz (x, y)")
    a = list(map(int, input().split()))
    b = a[1]
    a = a[0]
    mainGame = Board(a, b)

    while True:
        mainGame.printing()
        print("(y:, x:)", end='')
        if not mainGame.inputing(list(map(int, input().split()))):
            print("you lose")
            break
        if not mainGame.IsEnd():
            print("you win")
            break
    print("game over")


while True:
    Start()
    a = input("end (or) no: ")
    if a == "end":
        break