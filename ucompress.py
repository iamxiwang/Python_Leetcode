# uncompress
# Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:

# <number><char>

# for example, '2c' or '3a'.

def uncompress(s):
    output = ''
    i = 0
    num = ''
    while i < len(s):
        char = s[i]
        if char.isdigit():
            num += char
        else:
            output += int(num) * char
            num = ''
        i += 1
    return output

print(uncompress("2c3a1t"))
# test_00:
# uncompress("2c3a1t") # -> 'ccaaat'
# test_01:
# uncompress("4s2b") # -> 'ssssbb'
# test_02:
# uncompress("2p1o5p") # -> 'ppoppppp'
# test_03:
# uncompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'
# test_04:
# uncompress("127y") # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'