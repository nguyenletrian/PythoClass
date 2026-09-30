"""
# Cho
file_r = open("my_doc.txt","r") # To open for reading
file_w = open("new_report.txt","w") # To open for writing (overites) tạo mới nếu chưa có
file_a = open("log.txt","a") # To open for appeding, tạo mới nếu chưa có
file_b = open("log.txt","rb") #"wb"
# r+, w+ là cả ghi và đọc

#.read() Đọc hết nội dung
#.readline(): đọc 1 dòng mỗi lần
#.readlines(): đọc tất cả các dòng
with open("data.txt","r") as f:
    full_content = f.read() 
    f.seek(0) #Reset pointer Đưa lại dòng số 1
    first_line = f.readline() # line

with open ("poem.txt","w") as f:
    f.write("Roses are red,\n")
    f.write("Violets are blue,\n")
print("... Reading poem.txt")
    
#.close() để đóng file

#with open("filename","mode") as file_object: # mở và tự động đóng.

#.write(string): ghi file
#.writelines(list_of_strings) 1 mảng các chuỗi vào

"""

FIlE_NAME = "products.csv"

# Doc du lieu tu file và trả về danh sách đọc được
def read_products():
    # Tạo 1 biến kiểu list chứa tất cả sản phẩm đoc được từ file
    productList = []
    try:
        with open(FIlE_NAME,"r") as file:
            # Bỏ qua dòng đầu
            file.readline()
            # Đọc tiếp từ dòng số 2 trong file
            for line in file:
                data = line.strip() # Bỏ ký tự \n ở cuối mỗi dòng
                data = data.split(",")
                # Tạo sản phẩm theo dạng dictionary
                product = {
                    "id":data[0],
                    "name":data[1],
                    "price":data[2],
                }
                # Thêm sản phẩm vào list
                productList.append(product)
        return(productList)
    except FileNotFoundError: # Để trước vì nó là con của Exception
        print("File ko tim thay")
    except Exception as e: # Exception là cha của các lỗi
        print("Error: " + e)

# Hàm hiển thị sản phẩm
def display_product(products):
    # Kiểm tra nếu file rỗng (chưa có dữ liệu)
    if len(products) == 0:
        print("No products")
        return()
    # Nếu có dữ liệu thì in ra
    print("n\ ======================= Product list ====================")
    for p in products:
        print(f"ProductID: {p["id"]} --- ProductName: {p["name"]} --- Price:{p["price"]} ")
    

# Hàm thêm sản phẩm
def add_product(products):
    # Nhập product id
    product_id = input("Enter Product ID:")
    # Kiểm tra xem id này có tồn tại hay chưa?
    for p in products:
        if p["id"].lower() == product_id.lower():
            print("ID was duplicated")
            return()
    # Nhập tên
    product_name = input("Enter Product Name:")
    
    # Nhập giá
    try:
        product_price  = float(input("Enter price:"))
    except ValueError:
        print("Price must be number!!!")
    except Exception as e:
        print("Error: " + e)
        
    # Tạo sản phẩm theo dạng dictionary
    product = {"id":product_id,"name":product_name,"price":product_price}
    products.append(product)
    print("Produce added successfully")
    
        

# Hàm tìm kiếm sản phẩm:
def search_product(products):
    # Nhập ID để tìm kiếm
    product_id = input("Enter Product ID:")
    
    # Tạo 1 biến kiểu list để chứa các sản phẩm tìm thấy được
    found = []
    for p in products:
        if product_id.lower() in p["id"].lower():
            found.append(p)
    
    # Kiểm tra xem có tìm kiếm được hya ko
    if len(found) >0:
        display_product(found)
    else:
        print("No product found")
        
        
# Hàm lưu vào file:
def save_product(products):
    try:
        with open(FIlE_NAME,"w") as file:
            # Ghi lại dòng đầu tiên
            file.write("ProductID,ProductName,Price\n")
            
            # Ghi các dòng tiếp theo dự vào danh sách products
            for p in products:
                line = f"{p["id"]},{p["name"]},{p["price"]}\n"
                file.write(line)
            print("Write sucessfully.")
    except Exception as e:
        print("Error: ",e)

#Main Menu
def main():
    # Đọc dữ liệu khi chương trình chạy, gọi hàm read_product
    products = read_products()
    
    
    while True:
        print("""
==== MENU ==== 
1. Display all products
2. Add product
3. Search product by id
4. Save products to file.
5. Exit program
==== MENU ====             
""")
        choice = input("Enter your choice:")
        if choice == "1":
            display_product(products)
        elif choice == "2":
            add_product(products)
        elif choice == "3":
            search_product(products)
        elif choice == "4":
            save_product(products)
        elif choice == "5":
            print("Exit program")
            break
        else:
            print("Wrong choice, Enter 1-5")

main()
            
        