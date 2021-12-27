def get_period(day, N, backwards=False):
    backwards_flag = -1 if backwards else 1
    # get the list with in the timedelta format
    datelst = [
        datetime.strptime(day, '%Y-%m-%d') + backwards_flag 
        * timedelta(days=x) for x in range(N)
    ]
    # convert the list to the string forrmat
    datelst = [x.strftime('%Y-%m-%d') for x in datelst]
    
    return datelst
