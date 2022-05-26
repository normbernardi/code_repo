def race(v1, v2, g):
    if v1 >= v2:
        return None
    a, b, sec = g, 0, 0
    while not b >= a:
        sec += 1
        b += (v2/3600)
        a += (v1/3600)
    print(sec)
    return convert_sec_to_hms(sec)


def convert_sec_to_hms(sec: int) -> [int]:
    print(sec)
    h = sec / 3600
    m = (h - (h // 1)) * 60
    s = (m - (m // 1)) * 60

    return [h, m, s]

print(race(80, 91, 37))
