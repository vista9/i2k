"""
if - если, с пробелом после if, с : в конце
если в условии образуется True, то выполняется первый блок кода внутри if
если в условии образуется False, то выполняется второй блок кода внутри else
else без условия, но с : в конце
else не обязателен
"""
age = int(input("Enter your age: "))

if age > 18:
    print("You are eligible to vote")
    print("You are eligible to vote")
    print("You are eligible to vote")
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

if True and 6 < 5 or not False:
    print("True")

flag1 = True

if flag1:
    print("True")

"""
Flase:
0
""
''
[]
()
{}
set()
frozenset()
None

True:
когда есть что-то
"""

if 0:
    if 0:
        print("True")
    else:
        print("False")
else:
    print("False")


mark = int(input("Enter your mark: "))

if mark >= 80:
    print("A")
elif mark >= 60:
    print("B")
elif mark >= 40:
    print("C")
else:
    print("D")
