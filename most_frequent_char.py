def most_frequent_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

    result = s[0]
    for key in count:
        if count[key] > count[result]:
            result = key

    return result
