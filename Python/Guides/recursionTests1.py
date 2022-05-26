kap_seq = []
def kaprekar_seq(n: int, old_n=0) -> [int]:
    if len(str(n)) <= 1:
        return [n]
    if n != old_n:
        asc_intstr = "".join(sorted(str(n)))
        des_intstr = asc_intstr[::-1]
        old_n = n
        kap_seq.append(n)
        return kaprekar_seq(int(des_intstr) - int(asc_intstr), n)
    else:
        kap_seq_instance = kap_seq.copy()
        kap_seq.clear()
        return kap_seq_instance

def length(input) -> int:
    if not input:
        return 0
    else:
        return 1 + length(input[1:])

def recursive_sum(seq) -> int:
    if not seq:
        return 0
    else:
        return recursive_sum(seq[:-1]) + seq[-1]

def is_anagram(input_string: str, check_string: str) -> bool:
    if len(input_string) != len(check_string):
        return False
    for a, b in zip(sorted(input_string.lower()), sorted(check_string.lower())):
        if a != b:
            return False
    return True
