class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total=0
        for i,char in enumerate(s):
            current_val=roman_to_int[char]
            if (i+1) < len(s) and current_val <roman_to_int[s[i+1]]:
                total-=current_val
            else:
                total+=current_val
        return total