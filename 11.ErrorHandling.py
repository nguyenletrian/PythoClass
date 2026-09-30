try:
    pass
except ZeroDivisionError:
    pass
else:
    #Chạy nếu try ko báo lỗi
    pass
finally:
    #Chạy dù try lỗi hay ko
    pass
ZeroDivisionError
FileNotFoundError
TypeError
ValueError
IndexError
KeyError

def check_num(val):
    try:
        num = int(val)
    except ValueError:
        print(f"'{val}' is not a number.")
    else:
        print(f"Success:{num}")
    finally:
        print("Clean up done.")
    print("-"*15)
check_num("10")
check_num("abc")

