#currency checker
print("checking your money in indian rupess")
print('''$= u.s dollar
         W= korean won
         E= euro 
         p= sterling pound''')
print("make sure currency symbol is as mentioned")
sym=input("enter currency symbol $ w p e =").lower()
val=float(input("enter value="))
if sym=="$":
    print("value in inr is ", val*95.68)
elif sym=="w":
    print("value in inr is", val*0.069)
elif sym=="e":
    print("value in inr is", val*111.76)
elif sym=="p":
    print("value in inr is", val*130.52)
else:
     print("unrecognised currency!")
print("Currency exchange rate is as per date 24/8/26")
