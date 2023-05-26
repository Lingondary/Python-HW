#Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
#Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
#Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
#Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
#Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
#В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

def count_vowels(poem):
    return len([letter for letter in poem if letter.lower() in 'аиоуыэеёюя'])

def output(poem_vowels):
    if len(set(poem_vowels)) == 1:
        return 'Парам пам-пам'
    return 'Пам парам' # https://www.youtube.com/watch?v=ax1zuFT0Ibc&ab_channel=%D0%9D%D1%83%D0%B1%D0%B8%D0%BA%D0%9E%D0%BA%D1%83%D0%BD%D1%8C

    
best_poem_ever = list(map(count_vowels, input().split(' ')))

print(output(best_poem_ever))