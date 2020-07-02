class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary
        # Store the numbers as keys and values will be 
        # list of the indicies for that number
        # Iterate through numbers once again 
        # If target - number is in the keys of hash map
        # It is possible to find a match
        numbersInd = {}
        for i in range(len(nums)):
            curNum = nums[i]
            if curNum not in numbersInd.keys():
                numbersInd[curNum] = [i]
            else:
                numbersInd[curNum].append(i)
        print(numbersInd)
        for i in range(len(nums)):
            curNum = nums[i]
            aim = target - curNum
            if aim in numbersInd.keys():
                if i != numbersInd[aim][0]:
                    return [i, numbersInd[aim][0]]
        # Since exactly one solution is guaranteed no need to put 
        # another return for edge cases