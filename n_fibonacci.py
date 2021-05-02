#looping repeated n number of times

def first_n_fibonacci_while(n):
    prev_num = 0
    curr_num = 1
    count = 2

    print(prev_num)
    print(curr_num)
    
    while count <= n:
        next_num = curr_num + prev_num
        print(next_num)
        prev_num = curr_num
        curr_num = next_num
        count += 1

def first_n_fibonacci_for(n):
    prev_num = 0
    curr_num = 1
    
    print(prev_num)
    print(curr_num)
    
    for count in range(2, n + 1):
        next_num = curr_num + prev_num
        print(next_num)
        prev_num = curr_num
        curr_num = next_num

first_n_fibonacci_while(7)