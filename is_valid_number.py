def valid_number(num):
    num_string = str(num)
    
    is_valid = all(num_string[i] < num_string[i+1] for i in range(len(num_string)-1))

    if is_valid:
        print('{} is valid'.format(num))
    else:
        print('{} is not valid'.format(num))

valid_number(51)
valid_number(123)
valid_number(1231)
valid_number(10)