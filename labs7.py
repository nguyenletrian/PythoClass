from abc import ABC, abstractmethod

# 1. ABSTRACT CLASS (lớp cha)
class Product(ABC):
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    @abstractmethod
    def display_info(self):
        pass

# 2. ELECTRONIC PRODUCT (lớp con)
class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def display_info(self):
        print(
            "ID:", self.product_id,
            "| Name:", self.name,
            "| Price:", self.price,
            "| Brand:", self.brand,
            "| Warranty:", self.warranty, "months"
        )

# 3. CLOTHING PRODUCT (lớp con)
class ClothingProduct(Product):
    def __init__(self, product_id, name, price, size, material):
        super().__init__(product_id, name, price)
        self.size = size
        self.material = material

    def display_info(self):
        print(
            "ID:", self.product_id,
            "| Name:", self.name,
            "| Price:", self.price,
            "| Size:", self.size,
            "| Material:", self.material
        )

# 4. PRODUCT MANAGER
class ProductManager:
    def __init__(self):
        # thuộc tính products kiểu dữ liệu list khởi tạo là rỗng
        # chứa tất cả sản phẩm sẽ được thêm vào
        self.products = []

    # CREATE
    def add_product(self):
        print("\n----------------- ADD PRODUCT -----------------")
        product_id = input("Enter Product ID: ")

        # kiểm tra duplicate ID
        for product in self.products:
            if product.product_id == product_id:
                print("Error: Product ID already exists!")
                return

        name = input("Enter Product name: ")
        price = float(input("Enter Product price: "))

        # chọn loại sản phẩm do có 2 loại sản phẩm (2 class con)
        print("\nProduct Type")
        print("1. Electronic Product")
        print("2. Clothing Product")
        choice = input("Choose product type: ")

        if choice == "1":
            brand = input("Brand: ")
            warranty = int(input("Warranty (months): "))

            # tạo đối tượng sản phẩm ElectronicProduct
            product = ElectronicProduct(product_id, name, price, brand, warranty)
            # thêm sản phẩm vào list
            self.products.append(product)
            print("Electronic product added successfully!")

        elif choice == "2":
            size = input("Size: ")
            material = input("Material: ")

            # tạo đối tượng sản phẩm ClothingProduct
            product = ClothingProduct(product_id, name, price, size, material)
            # thêm sản phẩm vào list
            self.products.append(product)
            print("Clothing product added successfully!")

        else:
            print("Invalid product type!")

    # READ
    def show_products(self):
        if len(self.products) == 0:
            print("No products found!")
            return

        print("\n----------------- PRODUCT LIST -----------------")
        for product in self.products:
            product.display_info()

    # FIND PRODUCT
    # dùng để kiểm tra xem product id có tồn tại không trước khi update hay delete
    def find_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product

        return None

    # UPDATE
    def update_product(self, product_id):

        product = self.find_product(product_id)

        if product == None:
            print("Product ID does not exist!")
            return

        print("\nCurrent information:")
        product.display_info()

        print("Enter new information:")
        new_price = float(input("Enter new price: "))
        product.price = new_price
        print("Product updated successfully!")

        print("\nAfter update:")
        product.display_info()

    # DELETE
    def delete_product(self, product_id):

        product = self.find_product(product_id)

        if product == None:
            print("Product ID does not exist!")
            return

        self.products.remove(product)
        print("Product deleted successfully!")

# 5. MAIN MENU
def main():
    manager = ProductManager()

    while True:
        print("   PRODUCT MANAGEMENT SYSTEM    ")
        print("*************************************************")
        print("1. Add Product")
        print("2. Show Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")
        print("*************************************************")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_product()

        elif choice == "2":
            manager.show_products()

        elif choice == "3":
            product_id = input("Enter Product ID: ")
            manager.update_product(product_id)

        elif choice == "4":
            product_id = input("Enter Product ID: ")
            manager.delete_product(product_id)

        elif choice == "5":
            print("Exit program!")
            break

        else:
            print("Invalid menu selection!")

# 6. START PROGRAM
main()