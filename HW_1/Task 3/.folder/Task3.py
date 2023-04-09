#Задача 6: Вы пользуетесь общественным транспортом?
#Вероятно, вы расплачивались за проезд и получали билет с номером. 
#Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
#*Пример:*
#385916 -> yes
#123456 -> no

print('Проводим проверку на счастливый билет. Введите номер билета: ')

TicketNum = input()

if len(TicketNum) < 6:
    print('Неправильный ввод. Номер билета должен состоять из 6 цифр.')
else:
    temp = 0
    for i in TicketNum[0:3]:
        temp = temp + int(i)
    LeftSideNum = temp

    temp = 0
    for i in TicketNum[3:6]:
        temp = temp + int(i)
    RightSideNum = temp

    if LeftSideNum == RightSideNum:
        print('Отличные новости, народ. Билет счастливый.')
    else:
        print('Плохие новости, народ. Сегодня ретроградный Меркурий, билет не счастливый. Сегодня не твой день.')