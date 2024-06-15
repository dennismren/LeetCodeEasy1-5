class Solution:
    def reverseVowels(self, s: str) -> str:

        word = list(s)
        l = len(word)

        vowels = ["a","e","i","o","u","A","E","I","O","U"]

        left = 0
        right = l-1

        for i in range(l):
            
            if(left<right):
                if(word[left] in vowels and word[right] in vowels):
                    x = word[left]
                    word[left] = word[right]
                    word[right] = x
                    left+=1
                    right-=1
                elif(word[left] in vowels):
                    right-=1
                elif(word[right] in vowels):
                    left +=1
                else:
                    left+=1
                    right-=1
        
                
        return "".join(word) 
   