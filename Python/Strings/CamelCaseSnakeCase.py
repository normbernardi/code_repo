def variable_to_camel_case(text: str) -> str:
    split_text = []
    for word in text.split("_"):
        if word.isalnum():
            split_text.append(word.capitalize())
    camel_case = "".join(split_text)
    return camel_case[0].lower() + camel_case[1:]

def camel_case_to_snake_case(camel: str) -> str: # not mine
    snake_case = camel[0].lower()
    UNDERSCORE = "_"
    for char in camel[1:]:
        if char.isupper():
            snake_case += UNDERSCORE + char.lower()
        else:
            snake_case += char
    return snake_case

print(variable_to_camel_case("For_what_its_worth_buffalo_springfield"))
print((camel_case_to_snake_case("ForWhatItsWorthBuffaloSpringfield")))