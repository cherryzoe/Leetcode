# 输入：
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# 输出：
# [null,null,null,null,false,true,true,true]

# 解释：
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True

# 解题思路：
# 用字典树的数据结构
# 如果是'.'的情况，需要遍历到当前节点所有child

class trieNode(object):

    def __init__(self):
        self.child = {}
        self.isEnd = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = trieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        # 必须要把root赋值到cur中，不能直接移动原来的root指针，因为每次执行addWord操作都要从root开始
        cur = self.root
        for w in word:
            if w not in cur.child:
                cur.child[w] = trieNode()
            cur = cur.child[w]
        cur.isEnd = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.dfs(self.root, word, 0)

    def dfs(self, root, word, idx):
        if idx == len(word):
            return root.isEnd
       
        w = word[idx]
        if w == '.':
            for j in root.child:
                if self.dfs(root.child[j], word, idx+1):
                    return True
            # 遍历完所有子节点之后还没找到合适的结果，返回False
            return False
        else:
            if w not in root.child:
                return False
            return self.dfs(root.child[w], word, idx+1)
                    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
