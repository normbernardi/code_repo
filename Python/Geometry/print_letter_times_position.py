def repeat_seq(string: str) -> str:
    if len(string) == 1:
        return string.capitalize()
    else:
        return repeat_seq(string[:-1]) + '->' + (string[-1] * len(string)).capitalize()

print(repeat_seq("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
