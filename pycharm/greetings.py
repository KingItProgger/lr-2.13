def func(tip):
    if tip == 'list':
        def InsideFunc(s):
            return list(map(int,s.split(' ')))
    else:
        def InsideFunc(s):
            return tuple(map(int,s.split(' ')))
    return InsideFunc
