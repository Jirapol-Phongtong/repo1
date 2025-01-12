def palindrome(num):
    return str(num) == str(num)[::-1]
def find (num2):
    largest = 0
    if num2.isdigit():
        num = int(num2)
    else:
        return("invalid")
    if num == 3 :
        for a in range(999, 99, -1): 
            for b in range(a, 99, -1):
                product = a * b
                if palindrome(product) and product > largest:
                    largest = product
        return largest
    if num == 2 :
        for a in range(99,0,-1):
            for b in range(a,0,-1):
                product = a * b
                if palindrome(product) and product > largest:
                    largest = product
        return largest
    
    if num < 2 :
        return("invalid")

value = input()
output = find(value)
print(output)