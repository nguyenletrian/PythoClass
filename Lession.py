"""
Cài pip install jupyter
jupyter notebook

Kiểu dữ kiệu mytable =  thay đổi được: list
Kiểu dữ liệu Immutable = không thay đổi được: tuple...
integer (int)
float (float)
complex numbers
Dùng type() để kiểm tra loại biến
1000000 =  1_000_000
// là chia lấy phần nguyên
1e6 = 1x10 ** 6 (=1000000.0)
Boolean = True/False

 0 1 2 3 4 5 
 P y t h o n 
-6-5-4-3-2-1
print(text[0]) = P
print(text[3]) = h
print(text[-1]) = n
print(text[-4]) = t

String slicing: [Start:Stop:Step] #Stop - 1
word = "PYTHON"
word[1:4] = "YTH"
word[0:6:2] = "PTO"
word[::2] = "PTO"
word[-4:-1] ='THO'
word[::-1] = 'NOHTYP' # ĐẢO STRING, CHUỖI
work[1:-1] = 'YTHO'

markdown # NUMBERIC -> Shift + Enter

'Hi '*3 ='Hi Hi Hi'
'py' in 'python'
'java' not in 'Python'
'hello' == 'hello' # So sánh
'hello' = 'hello' # Gán giá trị
<, >, <=, >=

 STRING METHODS
 methods là những hàm hỗ trợ cho object text.upper()
 còn hàm là truyền vào xài print()
 
 upper() => viết hoa
 lower() => Viết thường
 strip() => cắt khoảng cách đầu và cuối
 replace() => thay thế text.replace('l','_')
 split(): cắt chuỗi thành mảng text.split()
 capitalize(): ký tự đầu tiên sẽ thành in hoa text.capitalize()
 endswith(): text.endswith("orld")
find(): text.find("world") => index
index(): text.index("lo") => 5
isnumeric(): Check phải số không text.isnumeric()

f"Hello,{name}!"
"Age: {}".format(age)
"Marks: %d" % marks    # %d %f 

implicit: ngầm định


10 // 4 = 2 chia làm tròn
10 % 3 = 1 chia lấy lấy dư
2 ** 3 = 8 (Mũ)

Assigenment Operators = Toán tử gán
x = 10 (gán x = 10)
x += 5 tương đương x = x + 5

Comparison Opertors: toán tử so sánh
==; !=; >; <; >=; <=

Logical Operators: Toán tử luận lý
and: tất cả phải thoả mới đúng
or: 1 trong chúng thoả là đc
not: Ngược lại với giá trị vào

Indetiry Operators: Toán tử nhận dạng
int = 4 bytes = 4 * 8 bits = 32 bits
float = 4 bytes
bool = 1 byte

is: trả về true nếu cả 2 đều tham chiếu đến 1 đối tượng
is not: returne True nếu cả 2 tham chiếu đến 2 đối tượng khác nhau

Membership Operators
in: trả về True value nằm trong sequence
not in: trả về True nếu không tồn tại trong sequence

True = 1
False = 0

Chuyển thập phân sang nhị phân
5
5/2 = 2 dư 1
2/2 = 1 dư 0
1/2 = 0 dư 1
Đọc ngược số dư = 101
9
9/2 = 4 dư 1
4/2 = 2 dư 0
2/2 = 1 dư 0
1/2 = 0 dư 1
8
8/2 = 2 dư 0
2/2 = 1 dư 0
1/2 = 0 dư 1


Chuyển nhị phân sang thập phân
001
7 6 5 4 3 2 1 0 (lớn hơn 7 tứ tăng lên bình thường)
          0 0 1
001 = 0 * 2 (mũ với vị trí đứng) + 0 * 2(mũ với vị trí đứng) + 1 * 2(mũ với vị trí đứng)
001 = 0 * 2^2 +  0 * 2^1 + 1 * 2^0 = 1(hệ thập phân)
1100 = 1*2^3 + 1*2^2 = 12

10
10/2 = 5 dư 0
5/2 = 2 dư 1
2/2 = 1 dư 0
1/2 = 0 dư 1

12
12/2 = 6 dư 0
6/2 = 3 dư 0
3/2 = 1 dư 1
1/2 = 0 dư 1

10 or 12
1010
1100
1110
-> 14


Bitwise Operators: Toán tử bit level
& = AND
| = OR
^ = XOR (Bằng 1 nếu các bit khác nhau)
~ = NOT (-x + 1)

<< = Dịch bit sang trái (left shift) dịch sáng trái 1 bit, thiếu sẽ = 0 
(5 << 1 = 10) <=> 5*2^1 = 10
(5 << 2 = 20) <=> 5*2^2 =  20

>> = Dịch bit sang phải (right shift)
5 >> 1 = 5 // 2^1 = 2


Precedence Order (High to Low) Thứ tự ưu tiên
()
**
unary: +x -x ~x
*,/,//,%
+,-
<<,>>
&,^,`
==,!=,>,<
not, and, or
=

Các Erros
Systax Errors: là lỗi sai cú pháp, bị trước khi chạy
Runtime: Lỗi khi chạy chương trình, ví dụ chia cho 0
Logical: Lỗi logic trong chương trình, ko báo lỗi
Error Handling in Python: Quản lý lỗi bằng try except


Conditional Statements

Control + / comment nhanh


"""