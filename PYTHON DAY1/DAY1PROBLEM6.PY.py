number=int(input())
if(number<0 and number%2==0):
  print("negative and even number")
elif(number>0 and number%2==0):
  print("positive and even number")
elif(number<0 and number%2!= 0):
  print("negative and odd number")
else:
  print("positive and odd number")