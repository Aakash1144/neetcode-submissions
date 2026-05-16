class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = []
        for i in range(0,len(heights)-1):
            left = i
            right = len(heights)-1
            while(left<right):
                width = right-left
                min_edge = min(heights[left],heights[right])
                area = width * min_edge
                #print("width, min_edge, area",width,area,min_edge)
                areas.append(area)
                if(min_edge==heights[left]):
                    left = left+1
                else:
                    right = right-1
        #print(areas)
        return max(areas)
