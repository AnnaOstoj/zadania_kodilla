def palindromy(slowo):
    flaga = "True"
    dl_slowo = len(slowo)
    for i in range(dl_slowo):
        print(slowo[i],slowo[dl_slowo-i-1])
        if slowo[i] != slowo[len(slowo)-i-1]:
            flaga = "False"
    
    return flaga

print(palindromy("kajak"))
