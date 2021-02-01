现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。

可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

示例 1:

输入: 2, [[1,0]] 
输出: [0,1]
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
示例 2:

输入: 4, [[1,0],[2,0],[3,1],[3,2]]
输出: [0,1,2,3] or [0,2,1,3]
解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
     因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。

每次只能选你能上的课
每次只能选 入度为 0 的课，因为它不依赖别的课
假设选了 0，导致 依赖 0 的课的入度减小，课 3 的入度由 2 变 1
接着选 1，导致课 3 的入度变 0，课 4 的入度由 2 变 1
接着选 2，导致课 4 的入度变 0，当前 3 和 4 入度为 0
继续选 入度为 0 的课 …… 直到选不到 入度为 0 的课

形似 树的BFS
起初让 入度为 0 的课 入列
然后逐个出列，课出列 即 课被选 ，并 减小相关课的入度
判定是否有课的入度新变为 0，安排入列、再出列……
直到没有 入度为 0 的课 可入列……

BFS 前的准备工作
我们关心 课的入度 —— 该值要被减，要被监控
我们关心 课之间的依赖关系 —— 选这门课会减小哪些课的入度
因此我们需要合适的数据结构，去存储这些关系
入度数组 和 邻接表
- 课号是 0 到 n - 1，作为索引，值为入度。遍历先决条件表，求出每门课的初始入度
- 用哈希表记录 依赖关系 （也可以用 邻接矩阵 ，但它有点大）
key： 课的编号
value： 依赖它的后续课程

BFS 思路
- queue 队列中始终是【入度为 0 的课】在里面流动
- 选择一门课，就让它 出列，同时 查看哈希表，看它 对应哪些后续课
- 将这些后续课的 入度 - 1，如果有 减至 0 的，就将它 推入 queue
- 不再有新的入度 0 的课入列 时，此时 queue 为空，退出循环



class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        q = []
        # 新建字典保存课程直接的先后序列
        dic = {}
        # 保存每门课的入度
        degree = [0 for _ in range(numCourses)]
        for p in prerequisites:
            if p[0] not in dic:
                dic[p[0]] = [p[1]]
                degree[p[0]] = 1
            else:
                dic[p[0]].append(p[1])
                degree[p[0]] += 1
        for idx, val in enumerate(degree):
            if val == 0:
                q.append(idx)
        # print dic, degree,q
        
        while q:
            course = q.pop()
            res.append(course)
            for i in dic:
                if course in dic[i]:
                    # dic[i].remove(course)
                    degree[i] -= 1
                    if degree[i] == 0:
                        q.append(i)
                        degree[i] = -1
        return res if len(res) == numCourses else []
