"""l=0
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
s="abacba"

isPali=True

for i in range(len(s)//2):

    if s[i]!=s[len(s)-i-1]:

        isPali=False

        break
print(isPali)