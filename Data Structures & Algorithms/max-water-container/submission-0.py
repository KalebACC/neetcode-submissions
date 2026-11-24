class Solution:
    def maxArea(self, heights: List[int]) -> int:
        front = 0
        back = len(heights)-1
        largest = -100

        while front < back:
            area = (abs(front-back) * min(heights[front],heights[back]))
            
            if area > largest:
                largest = area

            if heights[back] < heights[front]:
                back -=1
            else:
                front +=1
        
        return largest