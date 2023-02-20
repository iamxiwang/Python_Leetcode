# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
# Sure! Here's an example of a Python solution to the problem you described:

# python
# Copy code
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         # Define a dictionary to map each Roman numeral to its corresponding value
#         roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
#         # Initialize the result to zero
#         result = 0
        
#         # Iterate through the input string
#         for i in range(len(s)):
#             # If the current Roman numeral is less than the next one, subtract its value from the result
#             if i < len(s) - 1 and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
#                 result -= roman_to_int[s[i]]
#             # Otherwise, add its value to the result
#             else:
#                 result += roman_to_int[s[i]]
        
#         # Return the final result
#         return result
# In this solution, we define a class called Solution with a method called romanToInt that takes in a string s representing a Roman numeral and returns its corresponding integer value.

# We first create a dictionary called roman_to_int that maps each Roman numeral to its corresponding integer value.

# We then initialize a variable called result to zero, and iterate through the input string s. For each Roman numeral, we check if its value should be added or subtracted based on whether it is less than the value of the next Roman numeral in the string. If it is less, we subtract its value from the result; otherwise, we add its value to the result.

# Finally, we return the final result.

# To use this solution, you can create an instance of the Solution class and call its romanToInt method with a Roman numeral string as an argument:

# scss
# Copy code
# solution = Solution()
# result = solution.romanToInt("XXVII")
# print(result)  # Output: 27






class Solution:
    def romanToInt(self, s: str) -> int:
        # Define a dictionary to map each Roman numeral to its corresponding value
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        # Initialize the result to zero
        result = 0
        
        # Iterate through the input string
        for i in range(len(s)):
            # If the current Roman numeral is less than the next one, subtract its value from the result
            if i < len(s) - 1 and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
                result -= roman_to_int[s[i]]
            # Otherwise, add its value to the result
            else:
                result += roman_to_int[s[i]]
        
        # Return the final result
        return result