import time
from math import sqrt


def time_it(fn, *args, repetitions= 1, **kwargs):

    assert isinstance(repetitions, int), 'Value for repetitions is invalid'
    assert repetitions > 0, 'Value for repetitions is invalid'

    t0 = time.perf_counter()

    if fn == print:
        sep1 = kwargs.get('sep')
        end1 = kwargs.get('end')

        assert bool(args), 'No arguments given to print'

        for i in range(0,repetitions):
            print(*args, sep = sep1, end = end1)
        a = None

    else:
        for i in range(0,repetitions):
            a = fn(args, kwargs)
            print(a)

    t1 = time.perf_counter()

    return (t1 - t0)/repetitions, a


def squared_power_list(args, kwargs):

    assert bool(args), 'No arguments given to print'
    assert len(args) == 1, 'More than one arguments given'
    assert isinstance(args[0], int), 'Argument needs to be an integer'

    n = args[0]
    start = kwargs.get('start')
    end = kwargs.get('end')
    final = []

    assert end > start, 'Please ensure end value is greater than start value'
    assert end > start >= 0, 'Please ensure start and end values are greater than zero'

    for i in range(start, end+1):
        final.append(n**i)


    return final


def polygon_area(args, kwargs):

    assert bool(args), 'No arguments given to calculate area'
    assert len(args) == 1, 'More than one arguments given'
    assert isinstance(args[0], int), 'Argument needs to be an integer'


    l = args[0]
    side = kwargs.get('sides')

    assert l > 0, 'Please enter a valid length of side'
    assert side in (3,4,5,6), 'Please choose #sides between 3 and 6'

    if side == 3:
        a = (l**2)/2
    elif side == 4:
        a = l**2
    elif side == 5:
        a = (sqrt(5*(5+ (2* sqrt(5)))) * l**2 )/4
    elif side ==6:
        a = (3* sqrt(3)* l**2) /2

    return a


def temp_converter(args, kwargs):

    assert bool(args), 'No arguments given to convert'
    assert len(args) == 1, 'More than one arguments given'
    assert isinstance(args[0], int), 'Argument needs to be an integer'

    v = args[0]
    unit = kwargs.get('temp_given_in')

    assert unit in ('f','c'), 'Please give temperature in "f" or "c" units only'

    if unit == 'f':

        assert v > -459, 'Value needs to be greater than -459 in farenheit scale'

        f_v = (v - 32)  *5 /9

    elif unit == 'c':

        assert v > -273, 'Value needs to be greater than -273 in celsius scale'

        f_v = (v * 9 /5) + 32

    return f_v


def speed_converter(args, kwargs):

    assert bool(args), 'No arguments given to convert'
    assert len(args) == 1, 'More than one arguments given'
    assert isinstance(args[0], int), 'Argument needs to be an integer'


    dist = {'km':1, 'm':1000, 'ft':3280.84, 'yrd': 1093.61}
    time = {'ms':3600000, 's':3600, 'min':60, 'hr':1, 'day':1/24}

    d_unit = kwargs.get('dist')
    t_unit = kwargs.get('time')

    assert d_unit in ('km','m','ft','yrd'), 'Invalid distance unit entered'
    assert t_unit in ('ms','s','min','hr', 'day'), 'Invalid time unit entered'


    d_fact = dist.get(d_unit)
    t_fact = time.get(t_unit)

    v = args[0]

    fin_v = (v * d_fact)/ t_fact

    return fin_v