There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
Example 1:

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

https://blog.csdn.net/kenden23/article/details/14106137
我觉得做这道题的关键是要可以总结出来这道题目的属性，注意Note这个地方，其属性主要有两个：

1 如果总的gas - cost小于零的话，那么没有解返回-1

2 如果前面所有的gas - cost加起来小于零，那么前面所有的点都不能作为出发点。

原创： 靖心http://write.blog.csdn.net/postedit/14106137

第一个属性的正确性很好理解。那么为什么第二个属性成立呢？

首先我们是从i =0个gas station计算起的，设开始剩油量为left=0，如果这个station的油是可以到达下一个station的，那么left=gas-cost为正数，

到了下一个station就有两种情况：

1 如果i=1个station的gas-cost也为正，那么前面的left加上当前station的剩油量也为正。

2 如果i=1个station的gas-cost为负，那么前面的left加上当前的station的剩油量也有两种情况：

一） left为正，那么可以继续到下一个station，重复前面计算i=2,i=3...，直到发生第二）种情况

 二）如果left为负，那么就不能到下一个station了，这个时候如果i=k(i<k<n)，这个时候是否需要从第i=1个station开始重新计算呢？不需要，因为第k个station之前的所有left都为正的，到了第k个station才变成负。

证明：

left(i)>0, 如果left(i+1)<0，从i+1个station重新开始测试是没有必要的；
如果left(i+2) > 0呢？ 那么left(i) + left(i+1)>0; left(i) + left(i+1) +left(i+2) > left(i+2)那么从i+2个station开始也是没有必要的，以此类推……left(i) + ...+ left(k-2)>0, 那么left(i)+...+left(k-2) > left(k-1)， 那么就是没有必要从第k-1个节点重新开始计算了，现在到了第k个station的剩油量left变为负，也不能作为出发点，那么直接到k+1个计算就可以了。这就可以得出属性2了。


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total, summ, start = 0,0,0
        for i in range(len(gas)):
            summ += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if summ < 0:
                start = i+1
                summ = 0
        if total < 0:
            return -1
        return start
 
