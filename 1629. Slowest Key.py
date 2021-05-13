class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        if not releaseTimes:
            return ''
        
        max_duration = releaseTimes[0]
        res = keysPressed[0]

        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i-1]

            if duration > max_duration:
                max_duration = duration
                res = keysPressed[i]

            elif duration == max_duration:
                res = max(res, keysPressed[i])

        return res 

