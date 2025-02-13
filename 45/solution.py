class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
            
        step_queue = [0]
        found = {0}

        cnt = 0
        while step_queue:
            cnt += 1
            length = len(step_queue)
            for i in range(length):
                cur = step_queue.pop(0)
                for j in range(cur+1, cur+nums[cur]+1):
                    if j not in found:
                        step_queue.append(j)
                        found.add(j)
                    if j == len(nums)-1:
                        return cnt
