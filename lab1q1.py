def Num(num2):
    num = int(num2)
    if num < 0 or num >= 10 :
        return("invalid")
    sum=(num+((num*10)+num)+((((num*10)+num)*10)+num)+((((((num*10)+num)*10)+num)*10)+num))
    return(sum)
value = input()
output = Num(value)
print(output)