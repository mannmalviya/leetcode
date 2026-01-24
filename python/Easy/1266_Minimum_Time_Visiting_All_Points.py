"""
LeetCode Problem: 1266. Minimum Time Visiting All Points
Link:
- https://leetcode.com/problems/minimum-time-visiting-all-points/?envType=daily-question&envId=2026-01-12

Date Solved: Jan 14th, 2026
Total Time Spent: 25 mins + 16mins

Thought Process: 
- To find the minimum amount of time to go from one point to the next I was thinking in the direction of using a loop to do some kind of calculation of how close you are getting to the destination point while maintaining the time its taking, but then I got the idea for the O(1) solution.
- I got the idea when I read the problem again and it said "move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second)".

Notes:
- Daily Challenge problem
- The official editorial solution was very similar to my implementation. The key idea of maximizing the time spent moving diagonally is the same.
"""


from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """
            - Since we need to go from one point to the next in the list of points, in order to find the minimum time to travel to all points we can break the problem down to finding the minimum amount of time to get from one point to the next.
            - This was my initial solution that I submitted and passed all tests, beats 100% in runtime and 23% in memory
              
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        def dist(p1: List, p2: List):
            """
                - Returns the minimum time to get from point p1 to point p2
                - for 2 pts (x1,y1) and (x2,y2) we first travel diagonally as far as we can, which is determined by whichever of dx or dy is smaller, as otherwise you will overshoot
                - so for eg. if dx < dy then we travel dx horizontally and dx vertically and now we are gauranteed to be on the vertical line passing through p2 in time dx and we simply need to travel along the y axis a  distance of (dy - dx), which will take us (dy - dx) time, resulting in a total time of dx + (dy - dx) = dy
                - The above example ofc also works if dy < dx due to the symmetry of the problem
                - it also works if dx = dy
            """
            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]

            dx = abs(x2 - x1)
            dy = abs(y2 - y1)

            if dx < dy:
                return dy
            else:
                return dx
         
        time = 0
        for i in range(len(points) - 1):
            time += dist(points[i], points[i+1])

        return time
    

def main():
    return

if __name__ == "__main__":
    main()