#*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
#В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
#А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
#Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
#Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

latin_letters = {
    '1': ['A','E','I','O','U','L','N','S','T','R'],
    '2': ['D','G'],
    '3': ['B','C','M','P'],
    '4': ['F','H','V','W','Y'],
    '5': ['K'],
    '8': ['J','X'],
    '10': ['Q','Z']
}
cirilic_letters = {
    '1': ['А','В','Е','Н','О','Р','С','Т'],
    '2': ['Д','К','Л','М','П','У'],
    '3': ['Б','Г','Ё','Ь','Я'],
    '4': ['Й','Ы'],
    '5': ['Ж','З','Х','Ц','Ч'],
    '8': ['Ш','Э','Ю'],
    '10': ['Ф','Щ','Ъ']
}

def match_latin(text, alphabet=set('abcdefghijklmnopqrstuvwxyz')):
    return not alphabet.isdisjoint(text.lower())

def get_key(dic,value):
    for key, values in dic.items():
        if value in values:
            return key
        
print("Введите слово на английском или русском языках для расчёта его стоимости: ")

word = input()

if match_latin(word) is True:
    temp = 0
    for letter in word:
        temp = temp + int(get_key(latin_letters, letter.upper()))
    print(temp)
else:
    temp = 0
    for letter in word:
        temp = temp + int(get_key(cirilic_letters, letter.upper()))
    print(temp)

