# dinh nghia cac ham tuong ung
def func1():
    print("Them sinh vien")
    #nhap id
    id = input("Nhap id: ")
    print("id: ", id)

def func2():
    print("Xoa sinh vien")

# dinh nghia ham menu()
def menu():
    # khai bao bien lua chon
    choice = 0
    while True:
        print("****************MENU****************************")
        print("1. Them sinh vien")
        print("2. Xoa sinh vien")
        print("3. Thoat chuong trinh")
        print("****************MENU****************************")
        # nhap lua chon
        choice = int(input("Nhap lua chon(1-3): "))
        if choice == 1:
            #goi ham so 1
            func1()
        elif choice == 2:
            # goi ham so 2
            func2()
        elif choice == 3:
            print("Thoat chuong trinh")
            break
        else:
            print("Chi nhap 1-3")


# goi ham
menu()



