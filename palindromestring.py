def palindorme_string(s):
   # s=s.lower()- used to change the word to lower case so that Madam will be a palindrome
    left=0
    right=len(s)-1
    while left < right:
        if s[left]!=s[right]:
            return False
        left +=1
        right -=1
    return True
print(palindorme_string("Madam"))
