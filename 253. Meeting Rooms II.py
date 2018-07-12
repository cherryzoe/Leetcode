Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Tips:
#     https://leetcode.com/problems/meeting-rooms-ii/discuss/67855/Explanation-of-%22Super-Easy-Java-Solution-Beats-98.8%22-from-@pinkfloyda
# or example, we have meetings that span along time as follows:   
# |_____|
#       |______|
# |________|
#         |_______|     
# Then, the start time array and end time array after sorting appear like follows:

# ||    ||
#      |   |   |  |
# the minimal number of rooms equal to the max number of overlapping meeting in any time point. 
# The code is actually counting the number of overlapping meetings throughout the timeline and recording the maximum.

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        s, e = [],[]
        for i in intervals:
            s.append(i.start)
            e.append(i.end)
        s.sort()
        e.sort()
        i = j = rm = res = 0
        while i < len(s) and j < len(e):
            if s[i] < e[j]:
                rm += 1
                i += 1
            else:
                rm -=1
                j += 1
            res = max(res,rm)
        return res
