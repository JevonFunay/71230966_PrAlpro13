def palindrome(kalimat):
    kalimat2 = ''
    for i in kalimat.upper():
        if i.isalpha():
            kalimat2 = kalimat2 + i
               
    if len(kalimat2) == 1 or len(kalimat2) == 0:
        return True

    if kalimat2[0] != kalimat2[-1]:
        return False
    return palindrome(kalimat2[1:-1])


print(palindrome("halo"))
print(palindrome("kasur rusak"))
print(palindrome("a"))

