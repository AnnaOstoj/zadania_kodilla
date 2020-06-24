def palindromy(slowo):
    """
    Check if a word/phrase passed as input is a palindrome (a word read from left to right and backwards gives is the same word)
    Function returns a flag as output. If word is a palinddrome, then function returns "true"
    """
    is_palindrom = True
    
    only_letters = [char for char in slowo if char.isalnum()]

    dl_slowo = len(only_letters)
    for i in range(dl_slowo):
        if str.lower(only_letters[i]) != str.lower(only_letters[len(only_letters)-i-1]):
            is_palindrom = False
    return is_palindrom

print(palindromy("Łapał za kran, a kanarka złapał"))


