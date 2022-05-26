def vowel_upper_con_lower(s: str) -> str:
    vowels = 'aeiouAEIOU'
    new_s = ''
    for char in s:
        if char in vowels:
            new_s += char.upper()
        else:
            new_s += char.lower()
    return new_s

print(vowel_upper_con_lower("ASNFOIANSFDOKNSAKN1324512!@$\n \t test"))