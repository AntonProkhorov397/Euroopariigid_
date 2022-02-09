import random
slovar = {'Estonia': 'Tallinn', 'Russia' : 'Moscow', 'Tallinn' : 'Estonia', 'Moscow' : 'Russia', 'Riga': 'Latvia', 'Latvia': 'Riga', 'Finland': 'Helsinki', 'Helsinki': 'Finland', 'Sweden': 'Stockholm', 'Stockholm': 'Sweden', 'Germany': 'Berlin', 'Berlin': 'Germany', 'France': 'Paris', 'Paris': 'France','Italy': 'Rome', 'Rome': 'Italy','Belarus': 'Minsk','Minsk': 'Belarus','China': 'Pekin','Pekin': 'China','Japan': 'Tokyo','Tokyo': 'Japan','USA': 'Washington', 'Wasgington':'USA','Brasilia': 'Brasilia','Portugal': 'Lissabon', 'Lissabon': 'Portugal'}
def dobavit_v_slovar():
    riik = input('Dobavte stranu: ')
    linn = input('Dobavte gorod: ')
    slovar[riik] = linn
    slovar[linn] = riik
def change(town):
    del slovar[town]
    new_slovar_value=input('Izmenite slovo: ')
    slovar[town] = new_slovar_value
    slovar[new_slovar_value] = town
def test():
    count = 0
    list=[]
    for element in slovar.keys():
        list.append(element)
    for i in range(10):
        random_element = random.sample(list, 1)[0]
        print(random_element)
        test_write = input('Napishite: ')
        i += 1
        if test_write == slovar[random_element]:
            print('Verno!')
            count=count+1
        else:
            print('Ne verno')
    print('Vi zavershili test s ',count*10,'%.')

while True:
    print('Napishite "1" esli hotite napisat stranu ili gorod / gorod ili stranu ')
    print('Napishite "2" esli hotite proverit svoi znanija ')
    valik=input()
    if valik=='1':
        linn = input('Napishite stranu ili gorod: ')
        if linn in slovar.keys():
            output = slovar[linn]
            print(output)  
            print('Esli tut est oshibka, to vi mozete ee ispravit \nyes or no?')
            a=input()
            while True:
                if a=='yes':
                    change(linn)
                    break
                elif a == 'no':
                    break
                else:
                    print('vvedeno nepravilno!')
                    a=input('povtorite ese raz: ')
        else:
            print('Takogo ne sushestvuet.')
            print('Napishite "1" esli hotite dobavit v spisok ')
            print('Napishite "1" esli ne hotite dobavit v spisok ')
            valik=input()
            while True:
                if valik=='1':
                    dobavit_v_slovar()
                    break
                elif valik=='2':
                    break
                else:
                    print('vvedeno nepravilno!')
                    valik=input('povtorite ese raz: ')
                    break
    elif valik=='2':
        test()
    else:
        print('vvedeno nepravilno!')
        valik=input('povtorite ese raz: ')
