#validate email
accountnumber=input("enter a accountnumber")
pinnumber=input("enter a pinnumber")
currentbal=input("enter a currentbal")
withdrawbal=input("enter a withdrawbal")
totalbal=input("enter a totalbal")
if not(totalbal) > (withdrawbal):
    print("enter a currentbal")
elif (totalbal) < (currentbal):
    print("enter a totalbal")
elif (withdrawbal) < (totalbal):
    print("enter a insufficientbal")
n=int(input("enter a number"))
if (n==1):
    print("withdrawbal")
elif (n==2):
    print("totalbal")
