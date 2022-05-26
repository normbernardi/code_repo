# OLD OUTDATED OBSOLETE AND OTHERWISE UNDESIRABLE
# def lls(s:str):
#    length = 0
#    for c in s:
#        find = [c]
#        print("find is now: ")
#        print(find)
#        for s_c in s[(s.index(c)+1):]:
#            print("sc is now: " + s_c)
#            if s_c not in find:
#               if s_c != c:
#                    print("appending:" + s_c)
#                    find.append(s_c)
#            else:
#                test = "".join(find)
#                print("test is: " + test)
#                if len(test) > length:
#                    print(test + ' is longer.')
#                    length = len(test)
#               break
#    return length

def lls(s: str):
    if not s:
        return 0
    length = 1
    for i in range(0, len(s)):
        unique_chars = [s[i]]
        for j in range(i+1, len(s)):
            if s[j] not in unique_chars:
                unique_chars.append(s[j])
                j += 1
            else:
                break
        test = "".join(unique_chars)
        length = max(length, len(test))
    return length

print(lls("werwetop"))
