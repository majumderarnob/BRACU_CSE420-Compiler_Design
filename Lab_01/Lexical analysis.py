fileOpen = open("input.txt","r")
new = fileOpen.read().split()

keywords = ['auto','break','case','char','const','continue','default','do','double','else','enum',
'extern','float','for','goto', 'long','register','return','short','signed','sizeof','static','struct',
'switch','typedef','union','unsigned','void','volatile','while','int', 'float', 'if', 'else']

math_operators = ['+', '-', '=','*','/','++', "--", '//', '**']

logical_operators = ['>', '<','==','!','!=','<=','>=']

numerical_values = ['0','1','2','3','4','5','6','7','8','9']

others = [',', ';', '(', ')', '{', '}']

keywordStrore = []
mathOperatorStore = []
logicStore = []
numerialStore = []
otherStore = []
identifier = []

for i in range(len(new)):
    if new[i] in keywords and new[i] not in keywordStrore:
        keywordStrore.append(new[i])

    else:
        val = ""
        for j in new[i]:
            if j in others:
                if j not in otherStore:
                    otherStore.append(j)

                if val.isnumeric() or "." in val:
                    numerialStore.append(val)

                elif val in keywords and val not in keywordStrore:
                    keywordStrore.append(val)

                else:
                    if val !='' and val not in identifier:
                        identifier.append(val)
                val=""

            elif j in math_operators:
                if j not in mathOperatorStore:
                    mathOperatorStore.append(j)

                if val.isnumeric() or "." in val:
                    numerialStore.append(val)

                elif val in keywords and val not in keywordStrore:
                    keywordStrore.append(val)

                else:
                    if val !='' and val not in identifier:
                        identifier.append(val)
                val=""

            elif j in logical_operators:
                if j not in logicStore:
                    logicStore.append(j)

                if val.isnumeric() or "." in val:
                    numerialStore.append(val)

                elif val in keywords and val not in keywordStrore:
                    keywordStrore.append(val)

                else:
                    if val !='' and val not in identifier:
                        identifier.append(val)
                val=""

            elif j in numerical_values or j.isalpha() or j=='.':
                val = val + j

        if val.isnumeric() or "." in val:
            numerialStore.append(val)

        elif val in keywords and val not in keywordStrore:
            keywordStrore.append(val)

        elif val in others and val not in otherStore:
            otherStore.append(val)
            
        else:
            if val !='' and val not in identifier:
                identifier.append(val)
        

print('keywords:')
print(*keywordStrore,sep=",")  
print('\nIdentifiers:')
print(*identifier,sep=",")
print('\nMath Operators:')
print(*mathOperatorStore,sep=", ")
print('\nLogical Operators:')
print(*logicStore,sep=",")       
print('\nNumerical Values:')
print(*numerialStore,sep=", ")       
print('\nOthers:')
print(*otherStore,sep=" ")