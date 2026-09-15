import string
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        x=[]
        alphabets=list(string.ascii_lowercase)
        for char in alphabets:
            min_count=min(word.count(char) for word in words)
            x.extend([char]*min_count)
        return x