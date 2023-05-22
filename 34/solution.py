class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        start = -1
        end = -1
        notfound = False
        while start == -1 or end == -1:
            head = 0
            tail = len(nums)-1
            if notfound:
                break
            while True:
                print(head, tail, start, end)
                if head == tail and nums[head] != target:
                    notfound = True
                    break
                half = int((head+tail+1)/2)
                if nums[half] > target:
                    tail = half-1
                elif nums[half] < target:
                    head = half
                else:
                    if start == -1:
                        if half == 0:
                            start = half
                            break
                        elif nums[half-1] != target:
                            start = half
                            break
                        else:
                            tail = half-1
                    else:
                        if half == len(nums)-1:
                            end = half
                            break
                        elif nums[half+1] != target:
                            end = half
                            break
                        else:
                            head = half
        return [start, end]
