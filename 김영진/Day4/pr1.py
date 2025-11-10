#1

def cafe():

    menu = {
        "Americano": 3000,
        "Iced Americano": 3500,
        "Cappuccino": 4000,
        "Caffe Latte": 4500,
        "Espresso": 3600
    }

  
    print("=== 동윤이의 커피 가게 메뉴 ===")

    for item, price in menu.items():
        print(f"{item}: {price}원")

    choice = input("원하시는 메뉴를 입력하세요: ")


    if choice in menu:
        print(f"{choice}의 가격은 {menu[choice]}원입니다.")
    else:
        print("죄송합니다. 해당 메뉴는 없습니다.")

cafe()

    