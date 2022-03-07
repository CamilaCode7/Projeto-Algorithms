# explicação sobre o "ord()" https://www.geeksforgeeks.org/ord-function-python/
# https://www.geeksforgeeks.org/python-program-to-check-whether-two-strings-are-anagram-of-each-other/?ref=rp]


def is_anagram(first_string, second_string):
    n_chars = 256
    count1 = [0] * n_chars
    count2 = [0] * n_chars

    for i in first_string:
        count1[ord(i)] += 1
        print(ord(i))
    for i in second_string:
        count2[ord(i)] += 1
        print(ord(i))
    for i in range(0, 256):
        if count1[i] != count2[i]:
            print(count1[i])
            return False
    return True


# print(is_anagram("abcba", "abcba"))
