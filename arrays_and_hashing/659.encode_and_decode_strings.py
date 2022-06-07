from re import I


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        new_str = "***".join(strs)
        return new_str

    def encodeOptimzed(self, strs):
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        new_str_list = str.split("***")
        return new_str_list

    def decodeOptimized(self, str):
        res,i = [],0

        while i  < len(str):
            j = i
            while str[j] != "#":
                j+=1
            
            length = int(str[i:j])
            res.append(str[j + 1: j +1 + length])
            i = j+1 + length
        return res


solution = Solution()

encoded_str = (solution.encodeOptimzed(["lint","co#de","love","you"]))

print(encoded_str)

print(solution.decodeOptimized(encoded_str))