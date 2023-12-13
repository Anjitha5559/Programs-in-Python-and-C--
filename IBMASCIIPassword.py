string = "796115110113721110141108"
string = string[::-1]
print(string)
res = ""
i = 0
while i<len(string)-1:
    x = string[i]+string[i+1]
    if x == "32":
        res = res + " "
    elif int(x) in range(65,91) or int(x) in range(97,100):
        res = res + chr(int(x))
    elif i+2<len(string):
        x = x +string[i+2]
        res = res + chr(int(x))
        i+=1
    i+=2
print(res)
        