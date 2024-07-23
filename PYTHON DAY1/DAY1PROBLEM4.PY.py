cost_apple=15
cost_banana=4
cost_orange=5
print("enter no apples")
no_apples=int(input())
print("enter no bananas")
no_bananas=int(input())
print("enter no oranges")
no_oranges=int(input())
sum=(no_apples*cost_apple+no_bananas*cost_banana+no_oranges*cost_orange)
print("enter the amount_given")
amount_given=int(input())
if(sum>amount_given):
  print("cheated")
else:
  print("not cheated")
