def find_one(list, needle):
    return find_n(list, needle, 1)


def find_n(list, needle, ocurrences):
    if (ocurrences >= 0):
        found = 0
        index = 0
        while (index < len(list) and found < ocurrences):
            if (list[index] == needle):
                found += 1
            index += 1
        return found >= ocurrences
    else:
        return False


def find_streak(list, needle, ocurrences):
    if (ocurrences >= 0):
        found = 0
        index = 0
        streak = False
        while (index < len(list) and found < ocurrences):
            if (list[index] == needle):
                found += 1
                streak = True
            else:
                found = 0
                streak = False
            index += 1
        return found >= ocurrences
    else:
        return False
