string_one = 'i am the number one sting'
string_two = 'string number two'

if(string_one.endswith('test') or string_two.endswith('test')):
    print('found test')
else:
    print('no test')


    list_of_numbers = [2,5,9,17]

    for number in list_of_numbers:
        if(number > 10):
            print('large', number)
        elif(number < 10):
            print('not large', number)