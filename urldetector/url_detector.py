#url safety detector
url=input("enter your url:-").strip().lower()

#check for secure protocol
if url.startswith("https://"):
    print("url is safe, proceed to click it")
# check for insecure protocol
elif url.startswith("http://"):
    print("check twice before proceeding ahead.")
# check if it is IP Address or missing protocol
elif url.startswith("www.") or "." in url:
    print("not safe- missing protocol or invalid format")
else:
    print("not safe/ invalid entry")
