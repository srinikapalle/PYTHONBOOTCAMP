#MR X IS TRYING TO CREATE ANEW PASSWORD FOR HIS INSTAGRAM ACCOUNT THESE ARE REQUIRED CONDITIONS FOR CREATING A NEW PASSWORD
#1.MINIMUM LENGTH IS 8,MAX LENGTH IS 15 
#2.ONLY@ IS ALLOWED IN THE PASSWORD
#3.NO SPACES ARE ALLOWED
#4.ONLY ALPHA NUMERICS ARE ALLOWED
#YOUR ARE SUPPOSED TO PRINT WEAK IF LENGTH IS EXACTLY 8 MEDIUM LENGTH IS BETWEEN 8 TO 12 STRONG IF LENGTH IS BETWEEN 12 TO 15.
PASSWORD=input()
K=len(PASSWORD)
if K<=8:
    print("weak")
elif K>8 and K=12:
    print("medium")
elif K>12  and K=15:
    print("strong")
else:
    print("plz check the condions")
str="@/"
str[0]=@
str[1]=/
for i in str:
    if i in str[0] or str[1]:
        count+=1 # type: ignore