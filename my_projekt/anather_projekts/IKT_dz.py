# 1. Составьте три слова из фрагментов «гул», «отара», «том»
# 2. Вывести результат выражения: 5555+33*888, при условии, что входными данными являются строковые переменные A=‘5’ и D=‘3’
# 3. Дана строка S=‘Я памятник себе воздвиг нерукотворный’. Используя методы срезов, убрать из строки последнее слово
# 4. Пользователь вводит электронный адрес (формат ввода: адрес@servis.ru), необходимо вывести только адрес (то есть часть до знака @)
# 5. Пользователь вводит слово – необходимо вывести его наоборот (например, ввели слово «слон», вывод должен быть «нолс»).
import requests
class Qwestation():
    main = 0
    mass = ['гул', 'отара', 'том']

    def HTTP(self, arg):
        main_0 = requests.get(f'https://ru.wikipedia.org/w/index.php?go=%D0%9F%D0%B5%D1%80%D0%B5%D0%B9%D1%82%D0%B8&search={arg}&title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F%3A%D0%9F%D0%BE%D0%B8%D1%81%D0%BA&ns0=1')
        main_0 = main_0.text
        main_0 = main_0.split()
        if len(main_0) <= 2000: return arg
        else: return None

    def start(self):
        for i in self.mass:
            string_1 = i
            main_string = None
            while main_string == None:
                main_string = self.HTTP(string_1)
                i_0 = string_1
                string_1 = string_1[1:]
                string_1 = string_1 + i_0[0]
                if i == string_1:
                    string_1 = string_1[(len(string_1) // 2):] + string_1[0:(len(string_1) // 2)]
                    i = string_1
            print(main_string)
        print('каждое из слов проверялось в википедии и трактовку любого из них можно найти там')
        self.a_2()

    def a_2(self):
        a = 5
        d = 3
        print(int(a * 4) + int(d * 2) * int(str(eval(f'{a} + {d}')) * 3))
        self.a_3()

    def a_3(self):
        S = 'Я памятник себе воздвиг нерукотворный'
        S = S.split()
        print(*S[:len(S) - 1])
        self.a_4

    def a_4(self):
        a = input()
        print(a[0:a.index('@')])
        self.a_5()

    def a_5(self):
        a = input()
        print(a[len(a):0:-1])


obj = Qwestation()
obj.start()
obj.a_4()
obj.a_5()