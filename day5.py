
# #problem1
# p1 = 2**3
# p2 = 3**2
# if p1 > p2:
#     print("pervaya bolshaya")
# else:
#     print("vtoraya bolshaya")

# #problem2
# s = int(input())
# if 0 < s < 21 or 57 < s < 100:
#     print("duris")
# else: print("duris emes")

# #problem3
# s = int(input())
# if s%2==0:
#     print("четный")
# else: print("He четный")
# if s%3==0:
#     print("Delitcya")
# else: print("Ne delitcya")
# if s**2>1000:
#     print("bolshe")
# else: print("Ne bolshe")

#problem4
# s = int(input())
# if True:
#     print("duris")

#problem5
# a = 10//5
# b = 10/5
# if a == b:
#     c = a  + b
#     print(c)
# else: print("ne rovny")


#problem6
# a = int(input())
# if a < 0:
#     print(a)
# else: print("ne otricatelno")

#problem7
# a = 10
# b = 5
# if a > 0 and b > 0:
#     print("polojitelno")
# else: print("ne polojitelno")

#problem8
# a = int(input())
# b = int(input())
# if a > 0:
#     print(a + 2)
# else: print(b + 2)

#problem9
# a = int(input())
# if a > 0:
#     print("polojitelno")
# elif a < 0:
#     print("otrecatelno")
# else: print(a)

#problem10
# y = int(input())
# if y >= 18:
#     print("sovershennoletni")
# elif y <= 4:
#     print("rebenok")
# else: print("nesovershennoletni")

#problem11
# a = 45 
# b = 6
# if a % b == 0:
#     print("bolinedi")
# else: print("bolinbidi")

#problem12
# g = int(input())
# t = 2023
# if g == t:
#     print("tekushi god")
# elif g > t:
#     print("god proshol")
# else: print("god eshe ne nastupil")

#problem13
# y = int(input())
# y = 2023 - y
# if y >= 18:
#     print("sovershennoletni")
# elif y <= 4:
#     print("rebenok")
# else: print("nesovershennoletni")

#problem14
# a = int(input())
# b = int(input())
# c = int(input())
# # if a > b and a > c:
# #     print("ulken a")
# # elif b > a and b >c:
# #     print("ulken b")
# # else : print("ulken c")

# # if a < b and a < c:
# #     print("kishi a")
# # elif b < a and b < c:
# #     print("kishi b")
# # else : print("kishi c")

# min_num = a if a < b < c else b if b < a < c else c
# max_num = a if a > b > c else b if b > a > c else c

# print(f"min_num = {min_num}, max_num = {max_num}")

#problem15
# a = 17391
# b = 546
# c = 934
# a = a % 17
# b = b % 17
# c = c % 17
# if a < b and a < c:
#     print("kishi a")
# elif b < a and b < c:
#     print("kishi b")
# else : print("kishi c")

#problem16
# x = 13
# x = x ** 2
# if x < 172:
#     print("menshe")
#     x == x ** 2
#     print(x)
# else: print("bolshe")

# a = "hello world world hello"
# mid = len(a) // 2
# b = a[:mid]
# print(b[::-1] + a[mid:])


# #kalkularor
# a = int(input("1 san = "))
# b = int(input("2 san = "))
# c = input("amaldar = ")
# if c == "+":
#     print(a + b)
# elif c == "-":
#     print(a - b)
# elif c == "*":
#     print(a * b)
# elif c == "/":
#     if a == 0 or b == 0:
#         print("error")
#     else: print(a / b)
# elif c == "%":
#     print(a % b)
# elif c == "**":
#     print(a ** b)
# elif c == "//":
#     print(a // b)
# else: print("error")

#ploshadpryamaugolnika
# a = int(input())
# b = int(input())
# print("Площадь прямоугольника = ", a * b,"sm^")


#pifagor
# a = int(input())
# b = int(input())
# print(a**2+b**2)

#okrujnost
# from math import pi
# r = int(input("radius = "))
# print("okrujnost = ", pi * r * 2, "sm^")


#procent
# a = int(input())
# b = int(input())
# print((a * b) / 100, "%")




# tuple
# list
# a = [1, 2, 3, 4, 5, 6, 7]
# a.append(8) #биреу косады
# a.extend([9, 10, 11, 12, 13]) #коп косады косады
# a.count(8) #количество издиди
# a.remove(2) #удалить первый элемент
# a.pop(9) #удалить по индексу
# a.index(7) #найти элемент по индексу
# print(a)



#list and tuple

# #problem1
# list_1 = []
# list_2 = []
# for i in range(5):
#     a = int(input())
#     if a % 2 == 0:
#         list_1.append(a)
#     else:
#         list_2.append(a)
# print("Четные числа = ", list_1)
# print("Нечетные числа = ", list_2)

#problem2
# list_1 = []
# for i in range(5):
#     a = int(input())
#     list_1.append(a)
# max=list_1[0]
# for i in range(5):
#     if list_1[i] > max:
#         max = list_1[i]
# # max = max(list_1)
# min = min(list_1)
# sum =  sum(list_1)/len(list_1)
# print("Максимальное", max, "Минимальное", min, "Сумма", sum)

#problem3
# product = ["яблоко", "груша", "арбуз", "банан", "мандарин"]
# print(product)
# print("Введите индекс товара которого хотите удалить")
# index = int(input()) - 1
# if index >= 0 and index < len(product):
#     product.pop(index)
#     print(product)
# else: print("Неверный индекс")

#problem4
# points = 0
# vopros = [("5 + 5", "a = 10", "b = 5", "c = 6"), ("5 + 2", "a = 10", "b = 7", "c = 6"), 
#           ("4 + 3", "a = 7", "b = 9", "c = 6"), ("1 + 2", "a = 1", "b = 2", "c = 3")]
# otvet_pravilny = [10, 7, 7, 3]
# otvet_vvod = []
# for i in range(len(vopros)):
#     print(vopros[i])
#     a = int(input())
#     if a == otvet_pravilny[i]:
#         points += 1
#         otvet_vvod.append(a)
#         print("otvet pravilny")
#     else: print("otvet ne pravilny")
#     print()
# print("Vash points = ", points)
# if points >= 3:
#     print("vi proshli test!")
# else: print("vi ne proshli test!")



#problem5
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# q = int(input("введите число от 1 до 9 = "))
# print(a[q:])

#problem6
# users = []
# for i in range(10):
#     login_i = input("Введите логин: ")
#     password_i = input("Введите пароль: ")
#     password_i2 = input("Введите пароль еще раз: ")

#     if not login_i.isdigit() and not login_i.isalpha():
#         print(login_i)

#         if password_i == password_i2:
#             users.append((login_i, password_i))
            
#             p = input("Вы хотите выйти = Y/N: ")
#             if p == "N": continue
#             elif p == "Y": break
#         else: print("Пароли не совпадают")
#         p = input("Вы хотите выйти = Y/N: ")
#         if p == "N": continue
#         elif p == "Y": break
#     else: print("Неверный логин, он должен состойть из букв и цифр")
#     p = input("Вы хотите выйти = Y/N: ")
#     if p == "N": continue
#     elif p == "Y": break
# print(users)





# s = []
# # for _ in range(5):
# #     num = int(input())
# #     if num not in s:
# #         s.append(num)
# #     else: print("Такой число уже существ")
# # print(s)

# while len(s) < 5:
#     num = int(input())
#     if num not in s:
#         s.append(num)
#     else: print("Такой число уже существ")
# print(s)






#for while
# #problem1
# lang1 = "Rust"
# languages = ["go", "java", "python", "php", "javascript", "ruby", "Rust"]
# if lang1 in languages:
#     print("this language is in the list")


# #problem2
# for i in range(10):
#     print(i)


# #problem3
# for i in range(20):
#     if i % 2 == 0:
#         print(i)

# # #problem4
# sum = 0
# for i in range(100):
#     sum += i
# print(sum)



# #problem5
# for i in range(10):
#     print(i, "* 5 = ", i * 5)

# #problem6
# f = 1
# t = int(input())
# for i in range(1, t+1):
#     f *= i
# print(f)

#problem7
# for i in "Hello, world!":
#     print(i)

#problem8
# sum = 0
# s = [1, 2, 3, 4, 5]
# for i in s:
#     sum += i
# print(sum)




#problem9
# s = [1, 2, 2, 3, 4, 4,5]
# # for i in s:
# #     unique_numbers = list(set(s))
# unique_numbers = list(set(s))
# print(unique_numbers)



#problem10
# my_list = []
# for i in range(1, 11):
#     my_list.append(i)

# for i in range(len(my_list)-1 , -1, -1):
#     print(my_list[i])

# for i in range(10, 0, -1):
#     print(i)





#problem11
# for i in range(1, 100):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)



# #problem2.1
# languages = ["go", "java", "python", "php", "javascript", "ruby", "Rust"]
# for i in languages:
#     if i == "php":
#         break
#     print(i)


#problem3
# s = 7
# sum = 1
# for i in range(5):
#     sum *= s
# print(sum)

#problem4
# languages = ["go", "java", "python", "php", "javascript", "ruby", "Rust"]
# for i in range(len(languages)):
#     print(i, ":", languages[i])

#problem6
# names = ["Maksat", "Lazzat", "Danyar", "Vasya", "Aslan", "Bayan", "Aza"]
# for i in range(len(names)):
#     if i % 2 == 0:
#         print(i, ":", names[i])

#problem7
# names = ["Maksat", "Lazzat", "Danyar", "Vasya", "Aslan", "Bayan", "Aza"]
# for i in range(0, len(names),2):
#     print(i, ":", names[i])


#problem8
# lest_my = [894, 64, 68, 846,569, 984, 654, 64848, 684, 35241, 384]
# for i in lest_my:
#     if 100 < i < 999:
#         print("Число", i, "трехзначный")
#     if 0 <= i and i % 2 == 0:
#         print("Число", i, "четное и полажительный")
#     if i % 31 == 0:
#         print("Число", i, "делится на 31 без остатка")
#     if 100 < i and i % 17 == 0 or 150 < i and i == 13 ** 2:
#         print("++++")

#problem9
# import random
# lits_s = []
# for i in range(200):
#     lits_s.append(random.randint(-100, 100))
# print(lits_s)
# ind = 0
# sum1 = 0
# sum2 = 0
# for i in lits_s:
#     ind += 1
#     if i % 13 == 0:
#         print(i, "четное и его квадрат = ", i ** 2) 
#         sum1 += 1
#     if ind % 7 == 0 and i % 2 == 1:
#         print(i, "нечетное и его индекс = ", ind)
#         sum2 += 1
# print("Число первой = ", sum1)
# print("Число второй = ", sum2)






#hacaton
#problem8
# p = []
# for i in range(1, 21):
#     p.append(i)
#     if i % 2 == 0 and i % 3 != 0:
#         print(i)
# print(p)

#problem9
# p = []
# sum = 0
# for i in range(1, 101):
#     p.append(i)
#     sum += i
# print(sum)


# problem10
# s = input("Введите слово: ")
# s = s.split(" ")
# for i in s:
#     print(i)


# #problem5
# q = int(input("Введите число = "))
# for i in range(1, q+1):
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     print(i)


# #problem1
# words = ['Anna', 'civic', 'kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку',]
# for i in words:
#     if i == i[::-1]:
#         print(i)

# #problem10
# words = ['Anna', 'civic', 'kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку',]
# max = int(len(words[0]))
# for i in words:
#     if len(i) > max:
#         max = len(i)
#         max_s = i
# print("слово", max_s, ", самый длинный, состоит из = ", max,  " слов")

# #problem9
# soz = input(" = ")
# list_s = set(soz)
# #считаем буквы
# arip = []
# for i in list_s:
#     arip.append((soz.count(i), i))
# arip.sort(reverse=True)
# print(arip)
# print(arip[0][1], arip[0][0])



#4
# while True:
#     a = int(input("1 san = "))
#     b = int(input("2 san = "))
#     c = input("amaldar = ")
#     if c == "+":
#         print(a + b)
#     elif c == "-":
#         print(a - b)
#     elif c == "*":
#         print(a * b)
#     elif c == "/":
#         if a == 0 or b == 0:
#             print("error")
#         else: print(a / b)
#     elif c == "%":
#         print(a % b)
#     elif c == "**":
#         print(a ** b)
#     elif c == "//":
#         print(a // b)
#     else: print("error")
#     p = input("Вы хотите выйти = Y/N: ")
#     if p == "N": continue
#     elif p == "Y": break


# #problem7
# solem = input()
# solem_1 = solem.split(" ")
# per = len(solem_1[0])
# for i in solem_1:
#     if per < len(i):
#         print(i)

#problem6
# glasnse_b = ["a", "e", "i", "o", "u", "y"]
# soz = input(" = ")
# list_s = set(soz)
# arip = []
# for i in list_s:
#     arip.append((soz.count(i), i))

#problem8
# sum = 0
# solem = input()
# solem_1 = solem.split(".")
# sum_o = len(solem_1)
# for i in solem_1:
#     soz = i.split(" ")
#     sum += len(soz)
# print(sum/sum_o)






#set and dict

#problem000
# menu = {
#     "besh_barmak": "130 som",
#     "borsh": "100 som"
# }
# menu.update({"lagman": "130 som"})
# menu.pop("borsh")
# print(menu)


#problem10
# menu = {
#     "lagman": "120",
#     "plov": "120",
#     "borsh": "120"
# }
# menu.update({"drinks": ["Coca-Cola", "Sprite", "Fanta"]})
# print(menu)

#problem020
# methods = {"add", "remove", "clear", "update", "difference","discard", "intersection", "intersection_update", "pop"}
# methods2 = {"clear", "keys", "items", "get", "values", "update"}
# print(methods.intersection(methods2))
# print((methods.difference_update(methods2)))
# print(methods)

#problem31








#faill
# with open("text.txt", "w") as f:
#     for i in range(1, 100):
#         f.write(f"{i} \n")

# with open("text.txt", "r") as f:
#     text = f.read()
#     print(text)

#problem1
# with open("directories.txt", "r") as f:
#     text = f.read()
#     print(text)

#problem2
# with open("users.txt", "a") as f:
#     login = input("Введите логин: ")
#     password = input("Введите пароль: ")
#     f.write(f"\n \nlogin =  {login} \npassword = {password}  \n")

# with open("users.txt", "r") as f:
#     text = f.read()
#     print(text)

#problem3
# with open("text2.txt", "w") as f:
#     text = input("text: ")
#     f.write(text)

# with open("text2.txt", "r") as f:
#     text = f.read()
#     if "w" in text:
#         print("yes")
#     else:
#         print("not")

#problem4
# t_words = []
# with open("python.txt", "r") as f:
#     text = f.read()
#     for i in text.split():
#         if "t" in i or "T" in i:
#             t_words.append(i)
#         else:
#             continue
# print(t_words)

#problem5
# login = input("Введите логин: ")
# password = input("Введите пароль: ")
# with open("database.txt", "r") as f:
#     text = f.read()
#     if login in text:
#         print("такой логин и пароль уже существует")
#     else:
#         with open("database.txt", "a") as f:
#             f.write(f"\n \nlogin =  {login} \npassword = {password}  \n")

#problem6
# from pathlib import Path
# with open("reg_ph.txt", "w") as f:
#     login = input("Введите логин: ")
#     password = input("Введите пароль: ")
#     photo = input("Введите путь к фото: ")
#     if Path(photo).is_file() and Path(photo).suffix == ".jpg" or Path(photo).suffix == ".jpeg" or Path(photo).suffix == ".png":
#         f.write(f"login =  {login} \npassword = {password}  \nphoto = {photo} \n")
#         print("Регистрация прошла успешно!!!")
#     else:
#         print("Такой файл не существует или его оканчание не .jpg .jpeg .png")
# # /home/bayan/Загрузки/Python-logo-notext.png
# with open("reg_ph.txt", "r") as f:
#     text = f.read()
#     print(text)

#problem7
# from pathlib import Path
# with open("reg_ph.txt", "r") as f:
#     text = f.read()
#     images1 = input("Введите путь до картины хотите изменить: ")
#     images2 = input("Введите путь На каоторую хотите изменить: ")
#     if Path(images1).is_file() and Path(images2).is_file():
#         text = text.replace(images1, images2)
#         print("успешно")
#         print(text)
#         with open("reg_ph.txt", "w") as f:
#             f.write(text)
#     else: print("Такой файл не существует")


#problem8
# sum_o = 0
# p = 0
# with open("ai.txt", "r") as f:
#     for i in f:
#         line = i.split()
#         print(line[0], line[1])
#         if line[0] == "May" or line[0] == "July" or line[0] == "September" or line[0] == "November":
#             sum_o += int(line[1])
#             p += 1
#     print(sum_o/p)


#problem9
# with open("maxmin.txt", "r") as f:
#     for i in f:
#         line = i.split()
#         max = int(i.split(" ")[0])
#         min = int(i.split(" ")[0])
#         for j in line:
#             if max < int(j):
#                 max = int(j)
#             if min >= int(j):
#                 min = int(j)
#         print(max)
#         print(min)


#problem10
# with open("pr10.txt", "a") as f:
#     while True:
#         text = input("Введите данные: ")
#         f.write(f"{text} ")
#         if text == " ":
#             break

# with open("pr10.txt", "r") as f:
#     text = f.read()
#     print(text)

#os
# import os
# path = "/home/"
# print(os.path.exists(path))
# os.system('cat day5.py')



#enumerate
#map
#filter
#zip
#all
#any
#eval
#round
#abs
#pow


#enumerate
# a = ['Asel', 'Mansur', 'Alim', "Vlad"]
# for i, v in enumerate(a):
#     print(i, v)


#map
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = []
# for i in a:
#     b.append(str(i))
# print(''.join(b))

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = [str(i) for i in a]
# print(b)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = list(map(str, a))
# print(b)


# numbers = input('введите числа через пробел: ').split()
# numbers = list(map(int, numbers))
# print(numbers)

# def pow_m(x):
#     return 2 ** x
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = list(map(pow_m, a))
# print(a)



#filter
# a = [1, 5, 9, 8, 2, 3, 4, 5, 6, 7, 8, 9]
# b = []
# for i in a:
#     if i > 5:
#         b.append(i)
# print(b)


# a = [1, 5, 9, 8, 2, 3, 4, 5, 6, 7, 8, 9]
# b = [i for i in a if i > 5]
# print(b)


# a = [1, 5, 9, 8, 2, 3, 4, 5, 6, 7, 8, 9]
# list_filter = list(filter(lambda x: x > 5, a))
# print(list_filter)


# def main_f(x):
#     if x % 3 == 0 or x % 5 == 0:
#         return True
# a = [1, 5, 9, 8, 2, 3, 4, 5, 6, 7, 8, 9]
# list_filter = list(filter(main_f, a))
# print(list_filter)


# a = [1, 5, 9, 8, 2, 3, 4, 5, 6, 7, 8, 9]
# list_filter = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, a))
# print(list_filter)





#zip
# a = [1, 2, 3, 4, 5]
# b = ['a', 'b', 'c', 'd', 'e']
# print(list(zip(a, b)))


#all and any
# a = [True, False, False, False]
# b = [12, 13, 14, 15, 668, 56, 60]
# c = [True if i % 2 == 0 else False for i in b]
# print(all(c))
# print(any(c))


#abc
# a = -946
# print(abs(a))

#round
# s = 54.45424
# print(round(s))


#eval
# while True:
#     print(eval(input(">>> ")))



#problem1
# a = [1, 2, 3, 4, 5, 6, 7, "hello", 99, "world"]
# a = list(map(str, a))
# b = [True if i.isdigit() else False for i in a]
# print(b)
# print(all(b))
# print(any(b))


#problem2
# a = input('введите числа через пробел: ').split()
# a = list(map(int, a))
# min = a[0]
# for i in a:
#     if min > i:
#         min = i
# print(min)


#newproblem1
# s = input('Введите слово: ')
# def main_f(x):
#     glasnse_b = ["a", "e", "i", "o", "u", "y"]
#     for i in glasnse_b:
#         if x == i:
#             return 1
# for i in s:
#     list_filter = list(filter(main_f, s))
# print(len(list_filter))


#newproblem2
# a = [1, 2, 3, 4, 5, 6, 7]
# def pow_m(x):
#     return 2 ** x
# a = list(map(pow_m, a))
# print(a)

#newproblem3
# def pol(x):
#     if x > 0:
#         return x
# numbers = [-2, -5, 0, 7, -1, 9, 4]
# for i in numbers:
#     list_filter = list(filter(pol, numbers))
# print(list_filter)

#newproblem4
# a = ["alice", "bob", "charlie"]
# b = [25, 30, 35]
# print(list(zip(a, b)))


#newproblem5
# def cet(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
# numbers = [2, 4, 6, 8, 9]
# a = list(map(cet, numbers))
# print(a)
# print(all(a))
# print(any(a))


#newproblem6
# while True:
#     print(eval(input(">>> ")))


#newproblem7
# i = float(input("Введите число с точкой: "))
# print(round(i, 2))


#prostye cisla
# def prost(x):
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True
# list_filter = list(filter(prost, range(1, 101)))
# print(list_filter)


#fibionaci
# def fib(n):
#     if n in (1,2):
#         return 1
#     return fib(n-1) + fib(n-2)
# for i in range(2, 15):
#     print(fib(i))     





#try error
# a = {
#     'name': 'Vlad'
# }
# try:
#     print(a['name'])
# except KeyError as e:
#     print("error: " + str(e))
# except NameError as e:
#     print("Вы не создали переменную", e)
# else: print("okey")
# finally:
#     print("finally")


# zero_except = 0
# while True:
#     try:
#         print(eval(input(">>> ")))
#     # except:
#     #     pass
#     except ZeroDivisionError as e:
#         zero_except += 1
#         print("Деление на 0 невозможно", e)
#     except TypeError as e: 
#         print("Вы пытаетесь работать с разными типами данных", e)
#     except KeyboardInterrupt as e:
#         print("Вы пытаетесь завершить работу", e)
#     except SyntaxError as e:
#         print("Ошибка синтаксиса", e)
#     if zero_except == 3:
#         print("вы уже 0 делили 3 раза")
#         break


# import random
# from random import randint, randrange, choice, shuffle

# users = ["a", "b", "c", "d", "c", "d", "e", "f", "g", "h", "i"]
# shuffle(users) # shuffle - поменять местами
# print(users)
# print(choice(users))
# print(random.randrange(1, 10, 2))


#zadaca1
# import random
# from random import randint, randrange, choice, shuffle
# while True:
#     a = randint(1, 10)
#     try:
#         b = int(input("Введите число от 1 до 10: "))
#         if a == b:
#             print("Вы угадали!")
#         else:
#             print("Вы не угадали!")
#     except TypeError:
#         print("Вы ввели не число")
#     except ValueError:
#             print("Вы ввели не число")


#zadaca2
# import random
# from random import randint, randrange, choice, shuffle
# bukva = ["a", "b", "c", "d", "e", "i", "o", "p", "m", "n", "o", "p", "m"]
# print(choice(bukva))

#zadaca3
# import random
# from random import randint, randrange, choice, shuffle
# a = randint(1, 1000)
# while True:
#     try:
#         b = int(input("Введите число от 1 до 1000: "))
#         if a == b:
#             print("Вы угадали!")
#         elif a > b:
#              print("число должно быть больше")
#         elif a < b:
#                     print("число должно быть меньше")
#         else:
#             print("Вы не угадали!")
#     except TypeError:
#         print("Вы ввели не число")
#     except ValueError:
#             print("Вы ввели не число")

#zadaca4
# import random
# from random import randint, randrange, choice, shuffle
# san = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# try:
#     print(choice(san))
# except IndexError:
#     print("Список пустой")


#zadaca5
# import random
# x = random.random()
# y = random.random()
# print(x , y)

#zadaca6
# import random
# from random import randint, randrange, choice, shuffle
# try:
#     spisok = [1, 2, 3, 4, 5, "sdfs", "sdf", "asdfawd", ("sdf", "asd"), в, ]
#     print(choice(spisok))
# except TypeError:
#     print("Вы ввели не число")
# except SyntaxError:
#     print("синтаксическое ошибка")
# except NameError:
#     print("Вы не создали переменную")

#zadaca7
# import random, string
# password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(10))
# print(password)

#zadaca8
# import random
# from random import randint, randrange, choice, shuffle
# try:
#     d = int(input("Введите положительное число: "))
#     s = randint(1, d)
#     print(s)
# except ValueError:
#     print("Выберите положительное числа")

#zadaca9
# import random
# from random import randint, randrange, choice, shuffle
# try:
#     o = int(input("Введите число от: "))
#     d = int(input("Введите число до: "))
#     s = randint(o, d)
#     print(s)
# except ValueError:
#     print("Выберите положительное числа")



#zadaca10
# import random
# from random import randint, randrange, choice, shuffle
# try:
#     spisok = [1, 2, 3, 4, 5, "sdfs", "sdf", "asdfawd", ("sdf", "asd")]
#     print(int(choice(spisok)))
# except TypeError:
#     print("Вы ввели не число")
# except SyntaxError:
#     print("синтаксическое ошибка")
# except NameError:
#     print("Вы не создали переменную")
# except ValueError:
#     print(choice(spisok))
#     print("Элемент из списка не может преобразован в int")


#zadaca11
# import random
# from random import randint, randrange, choice, shuffle
# users = ['Edil', 'Bekarys', 'Beka', 'Dimash', 'Bayan', 'Me', 'Ruslan', 'Ilana', 'Alexandra', 'Ibragim']
# team1 = []
# team2 = []
# a = 0
# while len(team1) != 5 or len(team2) != 5:
#     a += 1
#     try:
#         x = choice(users)
#         if x not in team1 and len(team1) < 5:
#             team1.append(x)
#         elif x not in team2 and x not in team1 and len(team2) < 5:
#             team2.append(x)
#     except IndexError:
#         break
# print(team1)
# print(team2)
# shuffle(users)
# for i in users:
#     if len(team1) != 5:
#         team1.append(i)
#     else: team2.append(i)
# print(team1,"        ", team2)










#time datatime

# import time, datetime

# today = datetime.date.today()
# now = datetime.datetime.now()
# print(today)
# print(now)

# now = datetime.datetime.now()
# formatted_date = now.strftime("%d.%m.%Y %H:%M:%S")
# print(formatted_date)

# date = datetime(2000, 1, 28)
# date1 = datetime(2000, 1, 28)
# difference = date - date1
# print(difference.days)


# from datetime import datetime
# date_string = "28.01.2000 00:00:00"
# parsed_date = datetime.strptime(date_string, "%d.%m.%Y %H:%M:%S")
# print(type(parsed_date))

# import sys
# print(sys.version)

# import sys
# import os
# print(os.name)
# print(sys.platform)



#problem1
# import my_module

#problem2
# from random import randint, randrange, choice, shuffle
# names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
# shuffle(names)
# names_a = names[:4]
# print(names_a)

#problem3
# import sys
# import os
# print(os.name)
# print(sys.platform)

#problem4
# import os
# from random import choice
# from string import ascii_letters, digits
# d = []
# for i in range(5):
#     text = ''
#     while len(text) < 5:
#         text += choice(ascii_letters + digits)
#     d.append(text+".txt")
# print(d)
# for i in d:
#     os.system("touch rand/"+ i)

#problem5
# from random import shuffle
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat", 'sultan']
# team1 = []
# team2 = []
# team3 = []
# team4 = []
# shuffle(names)
# for i in names:
#     if len(team1) != (len(names)//4):
#         team1.append(i)
#     elif len(team2)!= (len(names)//4):
#             team2.append(i)
#     elif len(team3)!= (len(names)//4):
#         team3.append(i)
#     elif len(team4)!= (len(names)//4):
#          team4.append(i)
#     else:
#         print("bez komani", i)
# print(team1)
# print(team2)
# print(team3)
# print(team4)
# print(len(names))

#problem6
# import sys
# print(sys.argv)

#problem7
# import sys

# aa = input("Введите строку: ")
# aaa = input("Введите строку: ")
# if sys.getsizeof(aa)> sys.getsizeof(aaa):
#     print(sys.getsizeof(aa),aa)
# else:
#     print(sys.getsizeof(aaa), aaa)

#problem8
# from random import choice
# from string import ascii_letters, digits
# a = int(input("Введите число: "))
# password = ''
# while len(password) <= a:
#     password += choice(ascii_letters + digits)

# print(password)


#problem9
# from random import randint, randrange, choice, shuffle
# print(randrange(6,12,2))
# print(randrange(5, 105, 10))

#problem10
# import datetime
# now = datetime.datetime.now()
# plus_d = now + datetime.timedelta(days=100)
# print(plus_d)

#problem11
# NUMBERS = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]
# for i in range(len(NUMBERS)):
#     print(NUMBERS[i]+NUMBERS[i+1])


#problem12
# import datetime
# now = datetime.datetime.now()
# print(now)

#problem13
# import time
# for i in range(10):
#     print(i)
#     time.sleep(i)


#problem14
# LIST1 = [1,3,5,7,9,11,13]
# LIST2 = [2,4,6,8,10,12,14]
# for i,j in zip(LIST1, LIST2):
#     print(i, j)

#personTG1
# import os
# now = datetime.datetime.now()
# formatted_date = now.strftime("%Y_%m_%d_%H_%M_%S")
# print(os.system("mkdir accaa" + formatted_date))

#personTG2
# import os
# from random import choice
# from string import ascii_letters, digits
# text = ''
# while len(text) < 5:
#     text += choice(ascii_letters + digits)
# os.system("touch "+ text + ".txt")

#personTG3
# import os
# a = []
# a1 = len(os.system("ls"))
# a2 = os.system("ls")
# for i in range(15):
#     print(os.system("ls"))




#1
# import random
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat", 'sultan']
# team1 = []
# team2 = []
# team3 = []
# team4 = []
# for i in (team1, team2, team3, team4):
#     for _ in range(3):
#         i.append(names.pop(random.randint(0, len(names)-1)))
# print(team1)
# print(team2)
# print(team3)
# print(team4)
# print(names)


#2
# import random
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat", 'sultan']
# print([[names.pop(random.randint(0, len(names)-1)) for _ in range(3)] for _ in range(4)])
# print(names)



#problem1
# def kvadrat(x):
#     x = x**2
#     return x
# print(kvadrat(20))



#problem2
# def mass(x):
#     from random import randint
#     l = []
#     for i in range(x):
#         l.append(randint(0,100))
#     return(l)

# print(mass(10))


#problem3
# def obratno(x):
#     return x[::-1]
# print(obratno("sadfadfa"))

#problem4
# def sum_mass(x):
#     summ = 0
#     for i in x:
#         summ += i
#     return summ
# a = [1, 5, 10, 15, 99, 55]
# print(sum_mass(a))

#problem5
# def palindrom(x):
#     if x == x[::-1]:
#         return True
#     else:
#         return False
# print(palindrom("ata"))

#problem6
# def ekilik(x):
#     b = ""
#     while x > 0:
#         b = str(x % 2) + b
#         x = x // 2
#     return b
# print(ekilik(55))

#problem7
# def salistiru(x, y):
#     if x == y:
#         return 0
#     elif x > y:
#         return 1
#     else: return -1
# print(salistiru(11, 10))

#problem8
# def podcet(x):
#     count = 0
#     for i in x:
#         count += 1
#     return count
# print(podcet("asfasfaf"))

#problem9
# def spl(x):
#     aa = []
#     for i in x.split():
#         aa.append(i)
#     return aa
# print(spl("esf sef  drg"))


#slideproblem1
# def llist(q):
#     x = q[:len(q)//2]
#     x_r = q[len(q)//2:]
#     return x[::-1] + x_r[::-1]
# n = ['name', 'age', '1', '19']
# print(llist(n))

#slideproblem2
# def fib(n):
#     if n in (1,2):
#         return 1
#     return fib(n-1) + fib(n-2)
# for i in range(2, 10):
#     print(fib(i))   

#slideproblem3
# def kosu(x):
#     return x+2
# def alu(x):
#     return x-5
# def kobeutu(x, y):
#     x_k = kosu(x)
#     x_a = alu(y)
#     return x_k*x_a
# print(kobeutu(5, 9))


#slideproblem4
# def fail_sozd(x):
#     import os
#     os.system("touch "+ x)

# sozdat = fail_sozd
# imya = input("Название файла = ")+".txt"
# sozdat(imya)

#slideproblem5
# def gen_numbers():
#     from random import choice
#     n = '0444'
#     nom = ''
#     aa = ["1", "4", "5", "7", "9", "0"]
#     for i in range(7):
#         nom += choice(aa)
#     n += nom
#     return n
# print(gen_numbers())



#telegaproblems3
# a = 140
# b = 96
# while True:
#     if a % b != 0:
#         b = a % b
#         a = b
#         print(a, b)
#         continue
#     else:
#         # print(a, b)
#         break


# a = 96
# while True:
#     if a % 10 == 0:
#         a = a % 10
#         continue
#     else:
#         print(a)
#         break

# def no_boring_zeros(n):
#     if n == 0:
#         return n
#     while n % 10 == 0:
#         n = n // 10
#     return n
# print(no_boring_zeros(0))

# def str_count(strng, letter):
#     count = 0
#     if len(strng) == 0:
#         return 0
#     for i in strng:
#         if i == letter:
#             count += 1
#     return count
        
# print(str_count("hellow", "l"))


#problems1
# def add(x, y):
#     return x + y
# def subtract(x, y):
#     return x - y
# def multiply(x, y):
#     return x * y
# def divide(x, y):
#     return x / y
# print(add(1, 2), subtract(1, 2), multiply(1, 2), divide(1, 2))


#problems2
# def len2(strng):
#     count = 0
#     for i in strng:
#         count += 1
#     return count
# print(len2("hellddddo"))


#problems3
# def dict2(**kwargs):



#problems4
# def menu(eat, drink):
#     with open("menu.txt", "w") as f:
#         f.write(eat+"\n")
#         f.write(drink)
# eat = input("Eat: ")
# drink = input("Drink: ")
# menu(eat, drink)

#problems5
# def new_f(x):
#     import os
#     os.system("touch "+ x+".txt")
# txt = input("Enter file name: ")
# new_f(txt)

#problems6
# def funcc1():
#     def funcc2():
#         return "ya vlojenny"
#     return "ya glavny \n" + funcc2()

# print(funcc1())


#problems7
# def funcc1(**kwargs):
#     val = tuple(kwargs.values())
#     ke = tuple(kwargs.keys())
#     return val, ke
# print(funcc1(name = "Vladimir", age = 25))


#problems8
# def prost(x):
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True
# print(prost(101))

#problems9
# def n_list(x, y):
#     a = []
#     a.append(x)
#     a.append(y)
#     return a

# print(n_list(1, 2))


#problems10
# def n_list(x):
#     for i in range(x-1):
#         print(x)
#     return x
# print(n_list(5))

#problems11
# def zp(x, y = 5000):
#     name = x
#     selarray = y
#     return (name, selarray)

# print(zp("Vladimir"))


#problems12
# def gen_list(n):
#     from random import randint
#     a = []
#     for i in range(n):
#         a.append(randint(0,100))
#     return a
# print(gen_list(10))


# def duty_free(price, discount, holiday_cost):
#   a = (price/100)*discount
#   q = holiday_cost//a
#   return q

# print(duty_free(12, 50, 1000))



# def enough(cap, on, wait):
#     a = cap - on
#     if a == 0:
#         return wait
#     else:
#         b = wait - a
#         if b < 0:
#             return 0
#         return b
    
# print(enough(73,73,36))



# def triple_trouble(one, two, three):
#     a = ''
#     for i in range(len(one)):
#         a += one[i] + two[i] + three[i]
#     return a


# def position(alphabet):
#     a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     for i in range(len(a)):
#         if alphabet == a[i]:
#             return "Position of alphabet: " + str(i+1)
        
# print(position('z'))

# a = [[[[[[[[[[[[[[[[[[[[[[[[5]]]]]]]]]]]]]]]]]]]]]]]]
# while a != 5:
#     a = a[0]
# print(a)

# def rec(a):
#     if a == 5:
#         return 5
#     return rec(a[0])
# print(rec(a))

# a = [[[[[[[1,3,[[[[[[[[[4,[[[[[[[[5]]]]]]]],4]]]]]]]],7]]]]],8]]]
# b = []
# for i in a:
#     if type(i) == int:
#         b.append(i)
#     else:
#         for j in i:
#             if type(j) == int:
#                 b.append(j)
#             else:
#                 for k in j:
#                     if type(k) == int:
#                         b.append(k)
# print(b)


# a = [[[[[[[1,3,[[[[[[[[[4,[[[[[[[[5]]]]]]]],4]]]]]]]],7]]]]],8]]]
# b = []

# def rec(a):
#     for i in a:
#         if type(i) == int:
#             b.append(i)
#         else:
#             rec(i)
#     return b
# print(rec(a))

# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fib(n-1) + fib(n-2)

# print(fib(70))



#problem1
# def sum_ob(a):
#     if a != 1:
#         return sum_ob(a-1) + a
#     else: return a
# print(sum_ob(10))


#problem2
# def sum_ob(a: int):
#     if a >= 9:
#         return sum_ob(a//10) + 1
#     else: return 1
# print(sum_ob(5))


#problem3
# def stepp(x, y):
#     if y == 0:
#         return 0
#     elif y == 1:
#         return x
#     else:
#         return stepp(x, y-1) * x

# print(stepp(9, 3))

#problem4
# def min_san(a):
#     if len(a) == 0:
#         return 0
#     elif len(a) == 1:
#         return a[0]
#     else: 
#         min = a[0]
#         if min > a[1]:
#             a.pop(0)
#             return min_san(a)
#         else:
#             a.pop(1)
#             return min_san(a)
# print(min_san([1005, 6,89, 88, 99]))


#problem5
# def count_list(a):
#     cc = 0
#     if not a:
#         return 0
#     else:
#         cc += 1
#         a.pop(0)
#         return cc + count_list(a)
# print(count_list([1005, 6, 89, 88, 66, 88]))

#2v
# def count_list(a):
#     if not a:
#         return 0
#     else:
#         return count_list(a[:-1])+1
# print(count_list([1005, 6, 89, 88, 66, 88]))


#problem6
# def count_list(a):
#     new = []
#     b = a.copy()
#     new.append(a[-1])
#     a.pop(-1)
#     if len(new) == len(b):
#         return new
#     else:
#         return new + count_list(a)
# print(count_list([1005, 6, 89, 88]))



#problem7
# def proverka_el(a, s):
#     if not s:
#         return "no"
#     if a == s[0]:
#         return "yes"
#     else:
#         s.pop(0)
#         return proverka_el(a, s)
# print(proverka_el(9, [50, 8, 50]))


#problem8
# def poldednovatelnos(a, b):
#     q = []
#     if a == b:
#         return q
#     else:
#         q.append(a)
#         return q + poldednovatelnos(a+1, b)
# print(poldednovatelnos(5, 10))

#problem9
# def rev_s(a):
#     q = ''
#     if not a:
#         return 0
#     elif len(q) == 4:
#         return q
#     else:
#         q += a[-1]
#         return rev_s(a[:-1])+1 + q
# print(rev_s("1234"))








#lambda decorator
#problem1
# x = int(input("x = "))
# y = int(input("y = "))
# z = int(input("z = "))
# a = (lambda x, y, z: x*y*z)(x, y, z)
# print(a)



#problem2
# from datetime import datetime, date
# now = date.today()
# old_year = date(2023, 1, 1)
# new_year = date(2023, 12, 31)
# proshlo = now - old_year
# proshlo = int(proshlo.days)
# a = (lambda x: 365 - x)(proshlo)

# print(a)


#problem3
# def ne_cet(x):
#     if x % 2 == 1:
#         return x
#     return ne_cet(x+1)

# print(ne_cet(6))



#problem4
# def seet(a):
#     print(a)
#     if not a:
#         return "bitti"
#     else:
#         a.pop(0)
#         return seet(a)
    
# print(seet([1005, 6, 89, 88, 66, 88]))


#problem5
# def udali(func):
#     def wrapper(*args, **kwargs):
#             func(*args, **kwargs)
#             a = list(set(func(*args, **kwargs)))
#             return a
#     return wrapper

# @udali
# def rand(a, b):
#     c = []
#     from random import randint
#     for i in range(a, b):
#         c.append(randint(a, b))
#     return c

# print(rand(1, 100))


#problem6

# def chif_ras(func):
#     def wrapper(*args, **kwargs):
#         ch = func(*args, **kwargs)
#         chif = ''.join(map(str, ch[0]+ ch[1]))
#         z = ' '.join(map(str, ch[0]+ ch[1]))
#         e = []
#         for i in z.split(' '):
#             e.append(''.join(map(str,chr(int(i)))))
#         return chif, e
#     return wrapper

# @chif_ras
# def reg(l, p):
#     a = []
#     b = []
#     for i in l:
#         a.append(ord(i))
#     for i in p:
#         b.append(ord(i))
#     return a, b
# print(reg("Bayan", "Akhmet"))


#problem7
# a = [1745345,98726,439872634,7312,64872,123687126,9312,4124,231,3123,34,3453]
# b = []
# for i in a:
#     b.append((lambda x: x*1.185)(i))
# print(b)


# def who_is_paying(name):
#     if len(name) <= 2:
#         return [name]
#     elif len(name) >= 3:
#         return [name , name[:2]]
    
# print(who_is_paying(""))
    


# def get_military_time(time):
#     for i in range(len(time)):
#         if time[i] == 'A':
#             time = time[:-2]
    
# time = '12:00:01AM'
# # time = '11:46:47PM'

# if 'A' in time:
#     time = time[:-2]
#     time = int(time[:2] + time[3:5] + time[6:8])
#     time -= 120000
#     time = str(time)
#     while len(time) != 6:
#         time = "0" + time
#     time = time[:2] +":"+ time[2:4] +":"+ time[4:6]
# elif 'P' in time:
#     time = time[:-2]
#     time = int(time[:2] + time[3:5] + time[6:8])
#     time += 120000
#     time = str(time)
#     time = time[:2] +":"+ time[2:4] +":"+ time[4:6]
# print(time)

# def get_military_time(time):
#     if 'A' in time:
#         time = time[:-2]
#         time = int(time[:2] + time[3:5] + time[6:8])
#         time -= 120000
#         time = str(time)
#         while len(time) != 6:
#             time = "0" + time
#         time = time[:2] +":"+ time[2:4] +":"+ time[4:6]
#     elif 'P' in time:
#         time = time[:-2]
#         time = int(time[:2] + time[3:5] + time[6:8])
#         time += 120000
#         time = str(time)
#         time = time[:2] +":"+ time[2:4] +":"+ time[4:6]
#     return time
# print(get_military_time('12:00:01AM'))

# def wheres_wally(string):
#     if "Wally" in string:
#         for i in range(0, len(string)):
#             if string[i] == 'W':
#                 if string[i+1] == 'a':
#                     if string[i+2] == 'l':
#                         if string[i+3] == 'l':
#                             if string[i+4] == 'y':
#                                 return i
#     else:
#         return -1
# print(wheres_wally(" "))

import string
def is_valid_HK_phone_number(number):
    if len(number) == 9:
        if number[4]==" ":
            number = number.replace(" ", "")
            if number.isdigit():
                if len(number) == 8:
                    return number
    return False

def has_valid_HK_phone_number(number):
    for i in range(0, len(number)):
        if number[i].isdigit():
            if is_valid_HK_phone_number(number[i:i+9]) == True:
                return True
        return False

print(is_valid_HK_phone_number("1234 5678"))
print(has_valid_HK_phone_number("Hello, my phone number is 1234 5678"))


