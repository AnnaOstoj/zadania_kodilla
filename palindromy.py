def palindromy(slowo):
    is_palindrom = True
    dl_slowo = len(slowo)
    for i in range(dl_slowo):
        if str.lower(slowo[i]) != str.lower(slowo[len(slowo)-i-1]):
            is_palindrom = False
    return is_palindrom

print(palindromy("anna"))
