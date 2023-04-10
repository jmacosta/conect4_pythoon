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


def first_elements(list_of_lists):
    """
    recojo de cada lista el primer lemento y lo guardo en una nueva lista 
    """
    return n_elements(list_of_lists, 0)


def n_elements(list_of_lists, n):
    """
    recojo de cada lista el primer lemento y lo guardo en una nueva lista 
    """
    nElements = []
    nElements = list(
        map(lambda element: element[n], list_of_lists)
    )
    return nElements


def transponse(list_of_lists):
    matrix = []
    matrix = [n_elements(list_of_lists, i) for i in range(len(list_of_lists))]

    return matrix


def displace(list, distance, filler=None):
    if distance == 0:
        return list
    elif (distance > 0):
        filling = [filler]*distance
        res = filling + list
        res = res[:-distance]
        return res
    else:
        filling = [filler]*abs(distance)
        res = list + filling
        res = res[abs(distance):]
        return res

# cagada esto compueba una matriz al reves


def displace_board(board, limitDisplace):
    res = []
    for index in range(limitDisplace):
        res.append(displace(board[index], -index))
    return res


def displace_matrix(m, filler=None):
    res = []
    for index in range(len(m)):
        res.append(displace(m[index], index-1, filler))
    return res


def reverse_list(listParam):
    return list(reversed(listParam))


def reverse_matrix(matrix):
    rvMatrix = list(map(lambda element: reverse_list(element), matrix))
    return rvMatrix
