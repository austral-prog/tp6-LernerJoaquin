def remove_elements(lista):
    result = []
    for i in range(len(lista)):
        if i not in [0, 4, 5]:
            result.append(lista[i])
    return result


def add_elements(lista):
    lista.insert(0, 'Pink')   
    lista.append('Yellow')    
    return lista


def is_empty(lista):
    if not lista:        
        return True
    else:
        return False



def check_lists(lista1, lista2):
    if len(lista1) < 3 or len(lista2) < 3:
        return False

    return lista1[2] == lista2[2]
 

    

def list_of_lists(lista):
    lista[0] = lista[0][:2]     
    lista[1] = lista[1][1:4]    
    lista[2] = lista[2][-2:]    
    return lista
