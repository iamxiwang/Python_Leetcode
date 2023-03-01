# compress
# Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'

def compress(s):
    compressed_string =''
    count = 1
    sub_str = s[0]
    i = 1
    while i < len(s):
      if s[i] == sub_str:
          count += 1
          if i == len(s) - 1:
            compressed_string += str(count) + sub_str
      elif s[i] != sub_str and count == 1:
          compressed_string += sub_str
          sub_str = s[i]
          count = 1
      elif s[i] != sub_str and count > 1:
            compressed_string += str(count) + sub_str
            sub_str = s[i]
            count = 1    
            if i ==len(s) - 1 and s[i-1] != s[i]:
                compressed_string +=s[i]
      i+=1
      
    return compressed_string


# two pointer:
def compress(s):
    s += '?'
    i = 0
    j = 0
    result =''
    
    while j < len(s):
      if s[i] == s[j]:
        j += 1
      else:
        num = j - i
        if num == 1:
          result += s[i]
          i = j
        else:
          result += str(num) + s[i]
          i = j
        j += 1
      
      
    
      
    return result