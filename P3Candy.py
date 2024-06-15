class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        tfList = []
        for i in candies: 
            if(i+extraCandies >= max(candies)):
                tfList.append(True)
            else: 
                tfList.append(False)

        return tfList


        