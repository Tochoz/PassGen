from gen import new_pass
from base_relations import *

def save(pas):
    rcse = input('Enter the service (without spaces), witch connect with it:\n')
    add_pack([pas, rcse])

def add():
    pas = new_pass()
    print("Your password was generate succes:\n\n{0}\n".format(pas))
    ask = input("Do you want to add this pass into the base? [Y/N]\n").lower()

    while ask != 'y' and ask != 'n':
        ask = input('ERROR: Enter 1 in 2 letters: "y" or "n"\n')

    if ask == 'y':
        save(pas)
    #else:
    #    input('PRESS "ENTER" TO EXIT')



ask1 = input('WELCOME (prod. BY ./TOCHOZ/.) \n'
             'If you want get a new password, enter: "1"\n'
             'If you want to remind password, enter: "0"\n'
             'Here: ')

while ask1 != '1' and ask1 != '0':
    ask1 = input('ERROR: Enter: "1" or "0"\n')


if ask1 == "1":
    add()
else:
    print('Enter nuber:')

    for i in range(last_id() + 1):
        list = get_resouces()
        print('{0}) - {1}'.format(i + 1, list[i], end=""))
    print('\n{0}'.format(get_pass(int(input())-1)))
print('\n')
input('PRESS "ENTER" TO EXIT')