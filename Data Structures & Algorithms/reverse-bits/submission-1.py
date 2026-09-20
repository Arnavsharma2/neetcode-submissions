class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)
        binary = binary[2:]
        joiner = ''
        while len(binary) + len(joiner) != 32:
            joiner += '0'
        binary = joiner + binary
        binary = binary[::-1]
        
        return int(binary, 2)