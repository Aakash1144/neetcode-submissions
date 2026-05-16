class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights)-1
        while(left<right):
            width = right-left
            min_edge = min(heights[left],heights[right])
            area = width * min_edge
            #print("width, min_edge, area",width,area,min_edge)
            max_area = max(area, max_area)
            if(min_edge==heights[left]):
                left = left+1
            else:
                right = right-1
    #print(areas)
        return max_area
