def convert2digits(n: int) -> str:
    single_word = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ",
                   "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ",
                   "sixteen ", "seventeen ", "eighteen ", "nineteen "]
    tens = ["", "", "twenty-", "thirty-", "forty-", "fifty-", "sixty-", "seventy-", "eighty-", "ninety-"]
    if n == 0:
        return "Zero"
    elif is_single_word(n):
        return single_word[n]
    else:
        return tens[n // 10] + single_word[n % 10]

def is_single_word(n: int) -> bool:
    return n < 20

def convert3digits(n: int) -> str:
    if n < 100:
        return convert2digits(n)
    elif n % 100 == 0:
        return convert2digits(n // 100) + "hundred "
    else:
        return convert2digits(n // 100) + "hundred and " + convert2digits(n % 100)
def figure2words(n: int) -> str:
    denoms = {10 ** 9: "billion ", 10 ** 6: "million ", 10 ** 3: "thousand ", 1: ""}
    denom_values = sorted(denoms.keys(), reverse = True)
    in_words = ""
    for denom in denom_values:
        d = n // denom
        if d > 0:
            in_words += convert3digits(d) + denoms[denom]
        n %= denom
    return in_words

print(figure2words(19492137856))
