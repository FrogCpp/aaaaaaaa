#C:\Users\aleks\Desktop\jabascript\jabascript
all_objekt = {}
all_int = {}
all_str = {}
all_float = {}
def integer(b):
    for i in b[1:]:
        if i not in all_objekt:
            all_objekt[i] = 'int'
            all_int[i] = 0
        else:
            print('Error!0')
def string(b):
    for i in b[1:]:
        if i not in all_objekt:
            all_objekt[i] = 'str'
            all_str[i] = ''
        else:
            print('Error!0')
def real(b):
    for i in b[1:]:
        if i not in all_objekt:
            all_objekt[i] = 'float'
            all_float[i] = ''
        else:
            print('Error!0')
def formate(b):
    for i in all_objekt:
        if i == b[1]:
            if all_objekt[i] == 'int':
                if b[2].isdigit():
                    all_int[b[1]] = int(b[2])
                elif b[2] in all_int:
                    all_int[b[1]] = all_int[b[2]]
                else:
                    print('Error!1')
            elif all_objekt[i] == 'str':
                if not b[2].isdigit() and b[2][0] == '*' and b[2][len(b[2] - 1)] == '*':
                    all_str[b[1]] = b[2]
                else:
                    print('Error!1')
            elif all_objekt[i] == 'float':
                if b[2].split('.')[0].isdigit() and b[2].split('.')[1].isdigit():
                    all_float[b[1]] = float(b[2])
                elif b[2] in all_float:
                    all_float[b[1]] = all_float[b[2]]
                else:
                    print('Error!1')
            else:
                print('Error!2')
            break
def output(a):
    if a[1] == 'tl':
        if a[2] == 'text':
            print(*a[3:], end='')
        elif a[2] == 'ntext':
            for j in a[3:]:
                for i in all_objekt:
                    if i == j:
                        if all_objekt[j] == 'int':
                            print(all_int[j], end=' ')
                        elif all_objekt[j] == 'str':
                            print(all_str[j], end=' ')
                        elif all_objekt[j] == 'float':
                            print(all_float[j], end=' ')
                        else:
                            print('Error!2', end=' ')
    else:
        if a[1] == 'text':
            print(*a[2:])
        elif a[1] == 'ntext':
            for j in a[2:]:
                for i in all_objekt:
                    if i == j:
                        if all_objekt[j] == 'int':
                            print(all_int[j])
                        elif all_objekt[j] == 'str':
                            print(all_str[j])
                        elif all_objekt[j] == 'float':
                            print(all_float[j])
                        else:
                            print('Error!2')
function = {'int':integer, 'str':string, 'float':real, 'form':formate, 'print':output}
#=====================================================================================
def get_me_cod():
    main = input()
    f = open(f'{main}.txt', 'r')
    main = f.read()
    f.close()
    return main
main = get_me_cod().split('\n')
help_me = []
for i in main:
    help_me.append(i.split(':'))
main = help_me
#===============================
for i in main:
    for j in i:
        help_me = j.split('/')
        function[help_me[0]](help_me)