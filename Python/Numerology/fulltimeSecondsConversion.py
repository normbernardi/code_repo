def fulltime_to_seconds(input: str) -> int:
    split_input = input.split(":")
    print(split_input)
    return (int(split_input[0]) * 3600) + (int(split_input[1] * 60)) + int(split_input[2])

def seconds_to_fulltime(input: int) -> str:
    hours = input // 3600
    minutes = (input % 3600) // 60
    seconds = (input % 3600) % 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'
