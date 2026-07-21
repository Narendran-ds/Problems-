def palindrome_num_check(n):
    o=n
    r=0
    while(n>0):
        d=n%10
        r=r*10+d
        n//=10
    if (o==r):
        return True
    else:
        return False
print(palindrome_num_check(111))