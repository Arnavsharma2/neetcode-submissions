class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)
        binary = binary[2:]
        while len(binary) != 32:
            binary += '0'
        
        return int(binary, 2)