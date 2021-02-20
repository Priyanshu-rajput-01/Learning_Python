#this is a code for recursion function
def fac(value):
    if value == 0:
        result = 1
    else :
        result = value*fac(value-1)
    return result
#__main__
ans = 'y'
print = (ans)
while ans == 'y' or ans == 'Y':
    val = int(input('enter the value whose factorial you want to calculate :'))
    print(type(val))
   