class Solution:
    def reverseWords(self, s: str) -> str:
        newarr = s.strip().split()
        reversedstring = []
        print(s)
        for i in range(len(newarr)-1, -1 , -1):
            reversedstring.append(newarr[i])
        return ' '.join(reversedstring)
        
        