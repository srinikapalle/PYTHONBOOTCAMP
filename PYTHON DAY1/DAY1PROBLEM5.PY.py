x_height=int(input())
y_height=int(input())
x_weight=int(input())
y_weight=int(input())
if x_height==140 and x_weight%2==0:
    print("x is selected")
elif y_height==118 or y_height<=148 and y_weight%7==0:
    print("y is selected")
else:
    print("both are not selected")

