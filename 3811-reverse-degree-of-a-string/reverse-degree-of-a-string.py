class Solution:
    def reverseDegree(self, s: str) -> int:
        reverse_alphabet={}
        keys=string.ascii_lowercase
        values=range(26,0,-1)
        reverse_alphabet.update(zip(keys,values))
        total=0
        for i,char in enumerate(s,start=1):
            total+=i*reverse_alphabet[char]
        return total


