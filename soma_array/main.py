
lista = [1,2,3,4,5,6,7,8,9,10]

print(lista)

soma_lista = sum(lista)
print(f"Soma da lista = {soma_lista}")

def menor_que_11():
    for i in lista:
        if i < 11:
            return True
    return False
