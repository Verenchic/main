def dopusk():
    numbers = int(input('Число учеников - '))
    for i in range(numbers):
        while numbers != 0:
            i = int(input())
            if i > 50:
                numbers -=1
                print('True')
            else:
                numbers -=1
                print('False')


dopusk()