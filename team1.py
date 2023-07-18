# #1
# def san(func):
#     def wrapper(*args, **kwargs):
#         a = func(*args, **kwargs)
#         unique_l = list(set(a))
#         return unique_l
#     return wrapper

# @san
# def unique_elements(input_list):
#     return input_list

# input_list = [1, 2, 2, 3, 4, 4, 5]
# result = unique_elements(input_list)
# print(result)  

#2
# def find_common_elements(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
#     common_elements = list(set1.intersection(set2))
#     return common_elements
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# result = find_common_elements(list1, list2)
# print(result)  

#3
# def count_character_occurrences(input_string, target_character):
#     count = input_string.count(target_character)
#     return count
# input_string = "Hello, world!"
# target_character = "l"
# result = count_character_occurrences(input_string, target_character)
# print(result) 

# 4
# def count_vowels_and_consonants(input_string):
#     vowels = 'aeiouAEIOU'
#     consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
#     vowel_count = 0
#     consonant_count = 0
    
#     for char in input_string:
#         if char in vowels:
#             vowel_count += 1
#         elif char in consonants:
#             consonant_count += 1
    
#     return vowel_count, consonant_count

# input_string = "Hello, world!"
# vowel_count, consonant_count = count_vowels_and_consonants(input_string)
# print("Vowels:", vowel_count)  
# print("Consonants:", consonant_count)

# 5
# def factorial(func):
#     def wrap(number):
#         n = func(number)
#         if n == 0 or n == 1:
#             return 1
#         else:
#             result = 1
#             for i in range(2, n + 1):
#                 result *= i
#             return result
#     return wrap

    
# @factorial
# def dim(number):
#     return number
    
# print(dim(6))

# 6. Напишите функцию, которая принимает число и возвращает True, если оно является простым, и False, если нет.
# def prime(number):
#     if number < 2:  
#         return False
#     return True

# number = -10
# print(prime(number))
# number = 5
# print(prime(number))


#7. Напишите функцию, которая принимает список чисел и возвращает их среднее значение.
# def calculate_average(numbers):
#     if len(numbers) == 0:
#         return 0  
#     return sum(numbers) / len(numbers)

# list = [8, 30, 15, 4, 5]
# print(calculate_average(list))  



#8. Напишите функцию, которая принимает список и возвращает элемент с наибольшим количеством вхождений.
# def most_number(list):
#     counts = {}
#     for i in list:
#         if i in counts:
#             counts[i] += 1
#         else:
#             counts[i] = 1
    
#     most_number = max(counts, key=counts.get)
#     return most_number

# my_list = [1, 4, 5, 2, 2, 4, 5, 5, 1, 5]
# print(most_number(my_list))  

# >>>>>>>9
# def dek(func):
#     def wrapper(*args, **kwargs):
#         a = func(*args, **kwargs)
#         return a [::-1]
#     return wrapper

# @dek
# def dim(a):
#     return a
# print(dim([1,"dimash",3,4,5]))

# # >>>>>10
# def slovo(func):
#     def wrapper(*args, **kwargs):
#        a = func(*args, **kwargs)
#        return a [::-1]
#     return wrapper

# @slovo
# def dim(a):
#     return a

# print(dim("dimash"))

#11
# def palindrome_slovo(word):
#     reverse_word = word[::-1]
#     return word == reverse_word


# 12 
# def ag_elemet(word):
#     return list(set(word))
    
# 13  
# def check(func):
#     def wrapper(number):
#         if number % 2 == 0:
#             return True
#         return False
#     return wrapper
# @check
# def chetnoe(number):
#     pass

# print(chetnoe(20))


# 14
# def ulken(func):
#     def wrapper(*args, **kwargs):
#         a = func(*args, **kwargs)
#         return a.capitalize()
#     return wrapper
# @ulken
# def b_string(strings):
#     return  strings
# print(b_string('мен казакпын'))

# 15
# def san(func):
#     def wrapper(*args, **kwargs):
#         a = func(*args, **kwargs)
#         return "en uzak = " + str(a)
#     return wrapper

# @san
# def find_longest_string(strings):
#     longest_string = ""
#     for string in strings:
#         if len(string) > len(longest_string):
#             longest_string = string
#     return longest_string
# strings = ["apple", "banana", "cherrrrry", "durian"]
# result = find_longest_string(strings)
# print(result) 

#16
# def san(func):
#     def wrapper(*args, **kwargs):
#         a = func(*args, **kwargs)
#         return "Ortak bolingish sandar = " + str(a)
#     return wrapper

# @san
# def spisok_del(a, b):
#     deliteli = []
#     if a >= b:
#         max = a
#     else:
#         max = b
#     for i in range(1, max):
#         if a % i == 0 and b % i == 0:
#             deliteli.append(i)
#     return deliteli
# print(spisok_del(100, 200))

#17
# def san(func):
#     def wrapper(*args, **kwargs):
#         a = func(*args, **kwargs)
#         return "Kolishestvo slov = " + str(a)
#     return wrapper

# @san
# def dim_len(text: str) -> int:
#     count = 0
#     for _ in text.split( ):
#         count += 1
#     return count
# s = "Dimsh shamid dimd"

# print(dim_len(s))

#18
# def san(func):
#     def wrapper(*args, **kwargs):
#         a = func(*args, **kwargs)
#         return "Ortak ulken san = " + str(a)
#     return wrapper

# @san
# def obc_bol(a, b):
#     if a >= b:
#         min = b
#     else:
#         min = a
#     mm = 0
#     for i in range(2, min):
#         if a % i == 0 and b % i == 0:
#             mm = i
#     return mm
# print(obc_bol(50, 500))

#19
# def san(func):
#     def wrapper(*args, **kwargs):
#         a = func(*args, **kwargs)
#         return "Ortak kish san = " + str(a)
#     return wrapper

# @san
# def obc_mal(a, b):
#     if a >= b:
#         min = b
#     else:
#         min = a
#     mm = 0
#     for i in range(min, 2, -1):
#         if a % i == 0 and b % i == 0:
#             mm = i
#     return mm
# print(obc_mal(25, 500))



#20 - мына функциянын артыкшылыгы рандомна корсетпиди как сет а по проядку
# def san(func):
#     def wrapper(*args, **kwargs):
#         a = func(*args, **kwargs)
#         return "Bez dublikatov aripter = " + str(a)
#     return wrapper

# @san
# def bez_dulikatov(word):
#     q = []
#     s = []
#     for i in word:
#         q.append(i)
#     m = list(set(q))
#     for i in range(len(q)):
#         for j in range(len(m)):
#             if q[i] == m[j] and q[i] not in s:
#                 s.append(m[j])
#     return (''.join(s))

# print(bez_dulikatov("qweadswdqdp"))



#21
# def san(func):
#     def wrapper(*args, **kwargs):
#         a = func(*args, **kwargs)
#         return "Sandardin kosindisi = " + str(a)
#     return wrapper

# @san
# def sum_c(a):
#     summ = 0
#     for i in a:
#         summ += i
#     return summ
# print(sum_c([1,2,3,4,5,6,7,8,9,10]))

#22
# def san(func):
#     def wrapper(*args, **kwargs):
#         a = func(*args, **kwargs)
#         return "Sandardin kvadraty = " + str(a)
#     return wrapper

# @san
# def sum_c(a):
#     summ = 0
#     b = []
#     for i in a:
#         b.append(i*i)
#     return b
# print(sum_c([1,2,3,4,5,6,7,8,9,10]))

#23
# def san(func):
#     def wrapper(*args, **kwargs):
#         a = func(*args, **kwargs)
#         return "Ulken sandar = " + str(a[0]) + "\nKishi sandar " + str(a[1])
#     return wrapper

# @san
# def sum_c(a):
#     count_A = 0
#     count_a = 0
#     for i in a:
#         if i.isupper():
#             count_A += 1
#         elif i.islower():
#                 count_a += 1
#     return count_A, count_a
# print(sum_c("AAbbF"))

#24
# def san(func):
#     def wrapper(*args, **kwargs):
#         a = func(*args, **kwargs)
#         return "Barlik sannin kobitindisi = " + str(a)
#     return wrapper

# @san
# def sum_c(a):
#     summ = 1
#     for i in a:
#         summ *= i
#     return summ

# print(sum_c([1,2,3,4,5,6,7,8,9,10]))

#25
# def rimm_san(func):
#     def wrapper(*args, **kwargs):
#         a = func(*args, **kwargs)
#         return "Rim sani = " + a
#     return wrapper

# @rimm_san
# def rim_san(n):
#     return(''.join((
#     ('', 'M', 'MM', 'MMM'                                      )[n // 1000 % 10], 
#     ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM')[n //  100 % 10], 
#     ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC')[n //   10 % 10], 
#     ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')[n         % 10] 
#     )))

# print(rim_san(2023))