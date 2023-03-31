import re

file =open('input.txt','r')
whole_file = [i for i in file.read().split("\n") if i!=""]


reg_n=int(whole_file[0])
reg_exp=whole_file[1:reg_n+1]
strings=whole_file[reg_n+2:]

for i in strings:
    match="NO"
    index=0
    for exp in range(reg_n):
        check= re.fullmatch(reg_exp[exp],i)
        if check!=None:
            match="YES"
            index=exp+1
    print(match,",",index)
