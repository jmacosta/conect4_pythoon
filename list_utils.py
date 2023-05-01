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


def all_same(listParam):
    if len(listParam) > 0:
        for index in range(len(listParam)):
            if listParam[index] != listParam[0]:
                return False
    return True


def collapse_list(l, empty='.'):
    """ 
    Concatena  los elementos de una lista en una string y la devuelve
    """
    lString = ''
    if l != []:
        for elt in l:
            if elt == None:
                lString = lString + empty
            else:
                lString = lString + str(elt)
    return lString


def collapse_matrix(matrix, empty='.', fence='|'):
    """ 
      Concatena  los elementos de una lista de listas en una unica string separada por fence y la devuelve
    """
    matrixString = ''
    if matrix != []:
        for elt in matrix:
            matrixString = matrixString + collapse_list(elt, empty) + fence
    return matrixString[:-len(fence)]


def replace_all_in_list(l, oldElt, newElt):
    """ 
    Debo remplazar elemanto viejo si esta en la lista por elemento nuevo 
    """
    # comprueba si x es == elemento viejo, si no lo es lo añade a la lista tal cual. si lo es lo reemplaza y luego lo añade
    return [x if x != oldElt else newElt for x in l]


def replace_all_in_matrix(matrix, oldElt, newElt):
    newMatrix = []
    for elt in matrix:
        newMatrix.append(replace_all_in_list(elt, oldElt, newElt))
    return newMatrix
