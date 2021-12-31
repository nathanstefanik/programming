

def twoSum(numbers, target):
        hashmap = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[numbers[i]] = i
        
