# 6 option + 1 menu thoat

def func1():
    print("Them sinh vien")
    id = input("nhap id:")
    print(id)
    
def func2():
    print("Them sinh vien")
    id = input("nhap id:")
    print(id)


    
def menu():
    print("""
#################
1. Them sinh vien
2. Xoa sinh vien
3. Dong chuong trinh
#################
""")
    choice = 0
    while True:
        # Nhap lua chon
        choice = int(input("Nhap lua chon:(1-3):"))
        if choice == 1:
            #gọi ham  so 1
            pass
        elif choice == 2:
            # goi ham so 2
            pass
        elif choice ==3:
            print("Thoat chuong trinh")
            break #Neu muon chon menu thoat
        else:
            print("chi nhap 1-3")

menu()

