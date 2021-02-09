IP = input("Enter Value to convert to decimal: ").upper()
NS = input("Enter the base of the value: ")
val = int(0)
i = int(0)
bValid = (True)
while (i < len(IP) and bValid):
    char = IP[(len(IP)-1)-i]
    if char.isalpha():
        iMul = (ord(char)-55)
    else:
        iMul = int(char)
    bValid = iMul < int(NS)
    val += int(NS)**i*iMul
    i +=1
if bValid:
    print("%s in base %s = %s in decimal" % (IP,NS,str(val)))
else:
    print("The value of %s does not exist in a %s system" % (IP,NS))
#This can account for a total of 35 numbering systems
#Die is die Big brain lol.
#As julle die dom goed will sien kyk na die vorige submission
print("\n"*2)
IP = input("Enter the word to test for Palindrome: ")
i = int(0)
bValid = True
while ((i < len(IP)) and bValid):
    bValid = IP[i].upper() == IP[len(IP)-1-i].upper()
    print(IP[i]+" -- "+IP[len(IP)-1-i])
    i += 1
if (bValid):
    print("--> Palindrome") 
else:
    print("--> Not Palindrome")
