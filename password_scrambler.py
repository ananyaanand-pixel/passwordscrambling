
# test code for run
 
ui =input("enter password=")
ui =ui.lower()
leet_rules={"a":"4","e":"6","i":"9","o":"0","u":"8"}
sp=""
for letter in ui:
    if letter in leet_rules:
        sp=sp+leet_rules[letter]
    else:
        sp=sp+letter
print("your secure password is:",sp) 
