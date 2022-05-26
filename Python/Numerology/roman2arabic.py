rom2arabic_base = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def convert_letter(rom: str) -> int:
    split_list = []
    for char in rom.upper().replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC"):
        if char in rom2arabic_base:
            split_list.append(rom2arabic_base[char])
    return sum(split_list)


print(convert_letter("MCVIII"))


