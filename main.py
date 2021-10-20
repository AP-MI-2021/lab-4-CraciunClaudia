def show_menu():
    print('1. Citire liste')
    print('2. Acelasi numar de elemente pare')
    print('3. Intersectia listelor')
    print('4. Palindroame obtinute prin concatenarea a doua liste')
    print('5.')
    print('x. Exit')

def read_list():
    lst= []
    lst_str=input('Dati prima lista de numere separate prin spatiu : ')
    lst_str_split =lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst

def read_list_1():
    lst1=[]
    lst1_str=input('Dati a doua lista de numere separate prin spatiu:')
    lst1_str_split=lst1_str.split(' ')
    for num_str in lst1_str_split:
        lst1.append(int(num_str))
    return lst1


def get_even_list(lst):
    '''
    Determina daca elementele din prima lista sunt pare
    :param lst: O lista de numere
    :return: O lista cu numere pare
    '''
    result= []
    for num in lst :
        if num % 2 == 0 :
            result.append(num)
    return result

def get_even_list_1(lst1):
    '''
    Determina daca elementele din  a doua lista de numere sunt pare
    :param lst1: O lista de numere
    :return: O lista de numere pare
    '''
    result1=[]
    for num in lst1 :
        if num % 2 == 0 :
            result1.append(num)
    return result1

def test_get_even_list():
    assert get_even_list([ 1, 2, 4, 5, 8]) == [2,4,8]
    assert get_even_list([ 1,3,5])  == []
    assert get_even_list([4,8,10]) == [4,8,10]

def test_get_even_list_1():
    assert get_even_list_1([ 5,6,7,8]) == [6,8]
    assert get_even_list_1([ 1]) == []
    assert get_even_list_1([ 50,70,80]) == [50,70,80]
def show_even_lists(lst,lst1):
    nr = 0
    nr1 = 0
    for num in lst :
        nr = nr + 1
    for num in lst1 :
        nr1 = nr1 +1
    if nr == nr1 :
        return True
    return False

def get_common_numbers(lst,lst1):
    '''
    Determina daca numerele din prima lista se afla si in a doua lista
    :param lst: Lista de numere din prima lista
    :param lst1: Lista de numere din a doua lista
    :return: O lista de numere cu elementele comune din prima si a doua lista
    '''
    result=[]
    lst.sort()
    lst1.sort()
    for num in lst and lst1:
        if lst == lst1 :
            result.append(num)
    return result

def test_get_common_numbers():
    assert get_common_numbers([3,4,5],[3,4,5]) == [3,4,5]
    assert get_common_numbers([ 30,20,21],[50,22,44]) == []
    assert get_common_numbers([ 211,444, 567],[321,424,525]) == []

def show_common_numbers(lst,lst1):
    result = get_common_numbers(lst,lst1)
    print(f' Prima lista de numere : {lst} si a doua lista de numere {lst1} au elementele comune : {result}')



def main():
    lst=[]
    lst1=[]
    while True:
        show_menu()
        option= input('Alegeti optiunea: ')
        if option == '1' :
            lst=read_list()
            lst1=read_list_1()
        elif option == '2' :
            print(show_even_lists(lst,lst1))
        elif option == '3' :
            show_common_numbers(lst,lst1)
        elif option == '4' :
            pass
        elif option == '5' :
            pass
        elif option == 'x' :
            break
        else:
            print('Optiune invalida')


if __name__ == '__main__' :
    test_get_even_list()
    test_get_even_list_1()
    test_get_common_numbers()
    main()
