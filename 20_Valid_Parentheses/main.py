class Solution:
    def __init__(self):
        self.convert_dict = {
            '}': '{',
            ')': '(',
            ']': '['
        }

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        () : round bracket
        [] : square braket
        {} : brace
        """
        comp_array = [0]       

        for i in range(len(s)):
            if comp_array[len(comp_array)-1] == "False":
                return False
            
            #Check whether the parenthesis is open type
            if s[i] == "(" or s[i] == "[" or s[i] =="{":
                comp_array.append(s[i])
            #Check whether the parenthesis is open type
            elif s[i] in self.convert_dict:
                comp_array = self.process_close_char(s[i], comp_array)
                continue
        if len(comp_array) != 1:
            return False
        else:
            return True
        
    def process_close_char(self, s, comp_array):
        """
        :type s: char
        :type comp_array: str
        """
        if comp_array[len(comp_array)-1] == self.convert_dict[s] and len(comp_array) > 1:
            comp_array.pop()
        else:
            comp_array.append("False")

        return comp_array

solution = Solution()
string_array = []
"""
string_array.append("()")
string_array.append("()[]{}")
string_array.append("]")
string_array.append("(]")
string_array.append("[")
"""
string_array.append("]")
for i in string_array:
    print(solution.isValid(i))