file = open ("input.txt","r")
code = file.read().split("\n")
tokens=[]
for part in code:
    if "public" in part and "class" not in part and "main" not in part:
        if "static" in part:
            filter_part = part.split("static")[1].strip()
            tokens.append(filter_part)
        else:
            tokens.append(part.split("public")[1].strip())
for new in tokens:
    type_method=""
    method=""
    for j in range(len(new)):
        if new[j]==" ":
            while new[j]!=")":
                method+=new[j]
                j+=1
            break
        else:
            type_method+=new[j]
    print("Method:"+method+")","| return type:",type_method)