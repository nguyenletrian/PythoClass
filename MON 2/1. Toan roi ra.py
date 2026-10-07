"""
====== Logical Connectives =========
AND (^): conjunction: cả 2 thoả
OR (u): Disjunction: thoả 1 trong 2
NOT: Phủ định
IF... THEN: Implication: Nếu trời mưa thì mặt đường sẽ ẩm
IF AND ONLY IF: Biconditional: khi và chỉ khi: quan hệ 2 chiều

======= Propositional Calculus - MỆNH ĐỀ ======
Mệnh đề là 1 câu lệnh có thể có giá trị True hoặc False, không phải là 1 câu hỏi
nhưng ko thể là cả 2 thường là được đặt là p là q
- Atomic Propositions: Mệnh đề đơn, không thể chia nhỏ
- Compound Propositions: Mệnh đề phức hợp gồm nhiều mệnh đề đơn gộp lại với nhau
ví dụ "Man is Mortal"
"12 + 9 = 32"

"Go out and play": không phải mệnh đề vì ko cho ra kết quả đúng sai

Mệnh đề phức hợp: "Trời đang mưa và Nam đang nói"

IF... THEN
T --> T -> T
T --> F -> F
F --> T -> T
F --> T -> T
F --> F -> T
Nếu trời mưa thì mặt đất ướt

IF AND ONLY IF (P->Q) ^ (Q->P)
T <-> T -> T
T <-> F -> F
F <-> T -> F
F <-> F -> T

score = 60
ass_completed = False
if score >= 40 and ass_completed:
    print("Pass")
else:
    print("Fail")
    
print("-----")
score = 60
ass_completed = False
if score >= 40 or ass_completed:
    print("Pass")
else:
    print("Fail")



#BẢNG CHÂN TRỊ
values = [True,False]
print("P \t Q \t AND \t OR \t NOT")
for p in values:
    for q in values:
        result_and = p and q
        result_or = p or q
        result_not = not p
        print(p,q,result_and,result_or,result_not,sep=" \t")

TAUTOLOGIES: Hằng đúng
Contradictions: Hằng sai
"""
total_students = 100
english = 40 #A
math = 50 # B
science = 30 # C
english_math = 10   # A^B
math_science = 8    # B^C
english_science = 5 # A^C
like_three = 3 # A^B^C
# Tính số học sinh thích nhất 1 môn
# A U B U C = A + B + C - (A^B) - (B^C) - (A^C) + (A^B^C)
any = english + math + science + english_math - math_science - english_science + like_three
# tinh so hoc sinh ko thich mon nao
none = total_students - any
print("It nhat 1 mon: ",any)
print("Khong thich mon nao: ",none)

# Số học sinh chỉ thích đúng 2 môn là English và Math = englist_math - like_three
only_math = math - english_math - math_science + like_three

# Số học sinh chỉ thích đúng 2 môn là English và Math = englist_math - like_three
only_englist = english - english_math - english_science + like_three
