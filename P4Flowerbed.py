class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        counter = 0
        consec = 1

        l = len(flowerbed)

        if(n==0):
            return True

        for i in range(l):

            if(flowerbed[i] == 0):
                consec += 1
                if(i == l-1 and flowerbed[i-1] == 0):
                    counter += 1
                    consec -=1

            else:
                
                counter += (consec-1)//2
                consec = 0

        if(consec > 1):
            counter += (consec-1)//2

        return counter>=n
        
           