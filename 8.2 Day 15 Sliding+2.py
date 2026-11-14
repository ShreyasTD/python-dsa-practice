"""
i=0
r= len(a)-1
maxA=0
while l<r:
    maxA=max(maxA, min(a[l],a[r])*(r-l))
    if a[l]<=a[r]:
        l+=1
    else:
        r-=1"""
#reverse a string without using [::] function
#check if a string is palindrome
"""
s="abacba"

isPali=True

for i in range(len(s)//2):

    if s[i]!=s[len(s)-i-1]:

        isPali=False

        break
print(isPali)

#reverse a string without using [::] function
str ="shreyas"
rev=""
for i in str:
    rev=i+rev
print(rev)

#check if a string is palindrome 
s="abaabaaba"
isPalidrom=True
for i in range(len(s)//2):
    if s[i]!=s[len(s)-i-1]:
        isPalidrom=False
        break
print(isPalidrom)
#count number of vowels in a string
str="string"
vowels="aeiou"
count =0

for i in range (len(str)):
    if str[i] in vowels:
        count+=1

print(count)
#Find Longest Substring without repeating characters.
a=["abcabcbb","bbbbb","pwwkew"]
for i in a:
    left=0
    right=0
    maxLength=0
    subString=""
    while right<len(i):
        if i[right] not in subString:
            subString+=i[right]
            maxLength=max(maxLength,len(subString))
            right+=1
        else:
            subString=subString[1:]
            left+=1
    print(maxLength)

"""
# string consepts introduction:
"""
s="shreyas td"
# reverse using : 
print(s[::-1])

#concatination of string:
s1="shreyas"
s2="td"
s3=s1+" "+s2
print(s3)
print(s1*3) #multiplication of string
"""
"""
#reverse a string without using [::] function
s="shreyas"
rev=""
for i in s:
    rev=i+rev
print(rev)

#check if a string is palindrome or not
s="abacbaabcaba"
isPali=True
for i in range(len(s)//2):
    if s[i]!=s[len(s)-i-1]:
        isPali=False
        break
print(isPali)
"""
"""
print(ord("0"))#ord function gives the ascii value of a character
print(chr(65))#chr function gives the character of a ascii value

#count number of vowels in a string
str="string"
vowels="aeiou"
count=0
for i in range(len(str)):
    if str[i] in vowels:
        count+=1
print(count)
"""
#find the longest substring without repeating characters
a=["abcabcbb","bbbbb","pwwkew"]
for i in a:
    left=0
    right=0
    maxLength=0
    subString=""
    while right<len(i):
        if i[right] not in subString:
            subString+=i[right]
            maxLength=max(maxLength,len(subString))
            right+=1
        else:
            subString=subString[1:]
            left+=1
    print(maxLength)
    