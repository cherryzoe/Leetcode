class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        # 三指针
        i, j, k = 0, 0, 0
        res = []
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                res.append(arr1[i])
                i += 1
                j += 1
                k += 1
            # 两两比较，最小指针右移。注意考虑包含等号的情况，3个里面2个相等
            elif arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:
                i += 1
            elif arr2[j] <= arr1[i] and arr2[j] <= arr3[k]:
                j += 1
            elif arr3[k] <= arr1[i] and arr3[k] <= arr2[j]:
                k += 1
        return res
