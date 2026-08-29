# Given a string as a parameter of a function, return the length of longest substring which contains non repeating characters.
def maxLengthSubstringNRC(s):
    left=0
    ans=0
    characterSet=set()
    for right in range(len(s)):
        while s[right] in characterSet:
            characterSet.remove(s[left])
            left+=1
        characterSet.add(s[right])
        ans=max(ans, right-left+1)
    return ans
print(maxLengthSubstringNRC("acbadabb"))

#intervals = [[2,6],[1,8],[8,10]]