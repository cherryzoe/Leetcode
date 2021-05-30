class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        # to assign a new task, 
        # go to busy pool and kill the finished process (end_time < cur_time)if there is any. put it back to idle pool.
        # get the top(least weight) server from idle pool and assign to task
        # if there is no idle availble, wait for the next availble server from busy ==> go to busy and find the top one, update its end time by 
        # new_end_time = supposed_end_time + time_of_task
        import heapq

        idle = [] # (weight, id)
        busy = [] # (end_time, weight, id)

        for i in range(len(servers)):
            heapq.heappush(idle, (servers[i], i))

        res = []
        for i in range(len(tasks)):
            cur_time = i
            # free up finished server, put back to idle pool
            while busy:
                pre_end, w, server_id = busy[0]
                if pre_end < cur_time:
                    sID = heapq.heappop(busy)[2]
                    heapq.heappush(idle, (w, sID))
                else:
                    break
            # when idle pool has server available, pick to top one (least weight)
            if len(idle) > 0:
                weight, server_id = heapq.heappop(idle)
                end_time = cur_time + tasks[i] - 1
                heapq.heappush(busy, (end_time, weight, server_id))
                res.append(server_id)
            else:
                # no idle availble, get top from busy and delay its end time by adding tasks[i]
                end, weight, sID = heapq.heappop(busy)
                heapq.heappush(busy, (end+tasks[i], weight,  sID))
                res.append(sID)
        return res
