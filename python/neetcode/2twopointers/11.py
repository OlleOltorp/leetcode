# Time: (O(n))
# Space: (O(n))

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) -1

        largetsvol = 0
        
        while True: 
            lheight = height[left]
            rheight = height[right]

            print(lheight, rheight)
        
            vol = min(lheight,rheight) * (right-left)
            print("newvol", vol)
            if vol > largetsvol:
                print("insertednewvol")
                largetsvol = vol

            if lheight < rheight:
                left+=1
            elif rheight < lheight:
                right-=1
            else:
                left+=1

            if left == right:
                break

            if right ==  0:
                break

            if left == len(height)-1:
                break
            
        return largetsvol
