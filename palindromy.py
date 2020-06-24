def palindromy(slowo):
    """
    Check if a word passed as input is a palindrome (a word read from left to right and backwards gives is the same word)
    Function returns a flag as output. If word is a palinddrome, then function returns "true"
    """
    is_palindrom = True
    dl_slowo = len(slowo)
    for i in range(dl_slowo):
        if str.lower(slowo[i]) != str.lower(slowo[len(slowo)-i-1]):
            is_palindrom = False
    return is_palindrom

print(palindromy("anna"))
