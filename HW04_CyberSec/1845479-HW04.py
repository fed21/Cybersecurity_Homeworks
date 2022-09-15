import hashlib

for password in open("rockyou.txt", "r",encoding='utf-8'):
    if hashlib.md5((password.strip()+"yhbG").encode("utf-8")).hexdigest() == "f2b31b3a7a7c41093321d0c98c37f5ad":
        print("[+] password for Collins Hackle is "+password.strip())
        break
        
 
 