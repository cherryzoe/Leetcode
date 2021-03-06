
class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
#       sort input array by its units number from high to low. we want to load boxes with more units first.
        boxTypes = sorted(boxTypes, key = lambda x:x[1], reverse = True)
        res = 0
        remain_box = truckSize

        for i in boxTypes:
            box, unit = i[0], i[1]
            box = min(box, remain_box)
            res += unit * box
            remain_box -= box
            if remain_box == 0:
                break
        return res 

class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes = sorted(boxTypes, key = lambda b:b[1], reverse = True)
        res = 0
        total_size = 0
        for box in boxTypes:
            size, unit_cnt,  = box[0], box[1] 
            while size > 0: 
                res += unit_cnt
                size -= 1
                total_size += 1
                if total_size == truckSize:
                    return res
        # when truck size is very large that even when all of the boxes are place in but still not fully loaded 
        # in this case, we still need to return res of current loads
        return res
