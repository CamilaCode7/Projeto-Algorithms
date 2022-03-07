def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if not word:
        return False
    low_index = 0
    high_index = len(word) - 1
    for _ in range(len(word)//2):
        if word[low_index] != word[high_index]:
            return False
        low_index += 1
        high_index -= 1
    return True


print(is_palindrome_iterative('camila'))
