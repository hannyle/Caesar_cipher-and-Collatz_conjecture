def get_cycle_length(n):
    """ 
    takes an integer 0 < n < 10000
    returns the number of steps it
    will take to get to 1
    by performing n // 2 if n is even
    and n * 3 + 1 if n is odd
    int -> int
    print(get_cycle_length(5)) -> 6
    print(get_cycle_length(1)) -> 1
    print(get_cycle_length(197)) -> 27
    """
    # remove this pass statement and write the body of your function
    
    if n <= 0 or n>=10000 or type(n)!=int:
       return 'Error'

    count=1
    while n > 1 and n<10000:
        if n % 2 == 0:
         n = n / 2
         count+=1
        else:
            n = n * 3 + 1
            count+=1
    return count


def get_cycle_length_range(start, end):
    """ 
    takes 2 integers 0 < start, end < 10000
    finds the number for which it takes
    the maximum amount of steps to get to
    1 and returns the length of that cycle

    int, int -> int
    print(get_cycle_length_range(5, 100)) -> 119
    print(get_cycle_length_range(200, 100)) -> 125
    print(get_cycle_length_range(1, 2)) -> 2
    """
    # remove this pass statement and write the body of your function
    if start<=0 or start>=10000 or type(start)!=int or end<=0 or end>=10000 or type(end)!=int:
        return 'Error'
    
    if start>end:
        temp = start
        start = end
        end = temp
    
        
    maximum = 0
    for i in range(start,end):
        cycle = get_cycle_length(i)
        if cycle>maximum:
            maximum=cycle
    return maximum




    
