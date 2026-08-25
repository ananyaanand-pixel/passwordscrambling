#currency checker
print("checking your money in indian rupess")
print("$= u.s dollar ")
print("W= korean won ")
print("E= euro ")
print("p= sterling pound ")
print("make sure currency symbol is as mentioned and its sensitive to caps")
sym=input("enter currency symbol $ W p E =")
val=float(input("enter value="))
if sym=="$":
    print("value in inr is ", val*95.68)
elif sym=="W":
    print("value in inr is", val*0.069)
elif sym=="E":
    print("value in inr is", val*111.76)
elif sym=="p":
    print("value in inr is", val*130.52)
else:
     print("unrecognised currency!")
print("value is as per date 24/8/26")
