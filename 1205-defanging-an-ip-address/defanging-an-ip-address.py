class Solution:
    def defangIPaddr(self, address: str) -> str:
      modified_address=address.replace(".","[.]")
      return modified_address
