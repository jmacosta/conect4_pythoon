def explode_string(s):
    """
    Convierte una cadena en una lista 
    """
    return list(s)


def explode_list_of_strings(ls):
    """ 
    Convierte una lista de cadenas en lista de listas
    """
    listLs = []
    for elt in ls:
        listLs.append(explode_string(elt))
    return listLs
