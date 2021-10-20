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
            pass
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
    main()
