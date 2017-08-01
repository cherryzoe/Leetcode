Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.


solution 1(wrong answer) why?

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(set(nums))
        if n < 3:
            return max(nums)
        else:
            nums = list(set(sorted(nums)))
            return nums[-3]
            
        
 solution 2:
 利用变量a, b, c分别记录数组第1,2,3大的数字. 遍历一次数组即可，时间复杂度O(n)
 
 题目要求时间复杂度为O（n），所以排除使用先排序的方法来做，排序后基本时间复杂度就超了。
 所以只能遍历一遍来记录第三大的数，我们用三个整型变量来记录，由于题目没说有没有负数，
 所以我们没法定义一个绝对小于数组中所有数字的初始值，只能以数组中第一个数字来作为初始值，
 然后遍历一个一个数字去比较看应该替代三个数字中哪个数字，注意如果比第一个数字大，那么原本第一个数字的值要移动到第二个，
 原本第二个数字的值要移动到第三个，如果替代的是第二个数字，同样要把原本第二个数字的值移动到第三个，
 道理很简单。由于我们是用第一个数字作为初始值的，因此在替换数字时还有一个原因就是如果第二个和第三个数字还是初始值，
 而出现了与初始值不同的数字，那就不要求比原数字大了，直接替换并后移，否则如果第一个数字最大，那即使有第三大数字也不会记录下来。
 
 由于题目说了是非空数组，所以不用考虑空数组特殊情况。
 最后要判断三个数字是不是不一样，不一样才返回第三大数字，否则就要返回最大的数字。




 class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a =b =c =None
        for n in nums:
            if n>a:
                a,b,c = n,a,b
            elif a>n>b:
                b,c = n,b
            elif b>n>c:
                c = n
        return c if c is not None else a
