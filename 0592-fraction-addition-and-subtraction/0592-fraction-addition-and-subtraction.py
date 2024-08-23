class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        nums = re.split(r'(?<=\d)/|(?=[+-])', expression)

        if nums[0] == '': nums = nums[1:]

        if len(nums) <= 2:
            return expression

        while len(nums) >= 4:
            
            d1, n1 = int(nums.pop()), int(nums.pop())
            d2, n2 = int(nums.pop()), int(nums.pop())

            newNumerator = n1 * d2 + n2 * d1
            newDenominator = d1 * d2

            nums.append(newNumerator)
            nums.append(newDenominator)
        
        if nums[0] == 0:
            return "0/1"
        
        divisor = math.gcd(nums[0], nums[1])
        
        return str(nums[0] // divisor) + '/' + str(nums[1] // divisor)