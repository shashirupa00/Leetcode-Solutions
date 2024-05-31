class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        xor = 0

        for num in nums:
            xor ^= num
        
        diffBit = 1

        while not (diffBit & xor):
            diffBit = diffBit << 1
        
        a, b = 0, 0

        for num in nums:
            if diffBit & num:
                a = a ^ num
            else:
                b = b ^ num
        
        return [a, b]


         