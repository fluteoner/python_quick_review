'''
This is a demo for all python baics and functions
'''
def numbers():
    '''
    Basic number operations
    '''
    print('#########################')
    print('######## NUMBERS ########')
    print('#########################')

    print('1/2 = {}'.format(1/2))
    print('2.1 % 2.0 = {}'.format(2.1 % 2.0))

    print('2**3 = {}'.format(2**3))
    print('2**3.1 = {}'.format(2**3.1))
    print('pow(2, 4) = {}'.format(pow(2, 4)))
    print('pow(2, 4, 3) = {}'.format(pow(2, 4, 3))) # (2**4) % 3 = 1


    print('hex(512) = {}'.format(hex(512)))
    print('bin(1234) = {}'.format(bin(1234)))
    print('abs(-3) = {}'.format(abs(-3)))

    print('round(3.14159) = {}'.format(round(3.14159)))
    print('round(3.14159,) = {}'.format(round(3.14159, 4)))

def variables():
    '''
    Basic variables
    '''
    print('###########################')
    print('######## VARIABLES ########')
    print('###########################')
    int_a = 5
    print('a = 5, type(a) = {}'.format(type(int_a)))
    float_b = 2.1
    print('b = 2.1, type(b) = {}'.format(type(float_b)))

def string_slice_indexing():
    '''
    String Slice and Indexing
    '''
    print('#########################################')
    print('######## STRING SLICE & INDEXING ########')
    print('#########################################')
    s1 = 'Hello "Jonathan"!'
    s2 = "This's is also a string\n"
    print(s1)
    print(s2)

    # String Slice & Indexing
    s = '0123456789'
    print('s = {}'.format(s))
    print('len(s) = {} => "\\0" NOT INCLUDED!!'.format(len(s)))
    print('s[9] = {}'.format(s[9]))
    print('s[-1] = {}'.format(s[-1]))
    print('s[0:5] = {}'.format(s[0:5]))
    print('s[:5] = {}'.format(s[:5]))
    print('s[-2:-1] = {}'.format(s[-2:-1]))
    print('s[::] = {}'.format(s[::]))
    print('s[::2] = {}'.format(s[::2]))
    print('s[::-1] = {}'.format(s[::-1]))

def string_useful_functions():
    '''
    Useful String Functions
    '''
    print('##################################')
    print('######## STRING FUNCTIONS ########')
    print('##################################')
    my_name = "My name is "
    sam = "Sam"
    x = my_name + sam
    print('x = {}'.format(x))

    # Useful String Functions
    print('x.upper() = {}'.format(x.upper()))
    print('x.lower() = {}'.format(x.lower()))
    print('x.capitalize() = {}'.format(x.capitalize()))
    print('x.count(' ') = {}'.format(x.count(' ')))
    print('x.find(' ') = {}'.format(x.find('is')))
    print('x.split() = {}'.format(x.split()))
    print('x.split("is") = {}'.format(x.split('is')))
    print('x.partition("name") = {}'.format(x.partition('name')))
    print('x.center(20, "$") = {}'.format(''.center(20, "$")))
    print('x.center(20, "$") = {}'.format(x.center(20, "$")))
    print('x.center(20, "$") = {}'.format(''.center(20, "$")))

    s = 'ABCD1234'
    print('s.isalnum() = {}'.format(s.isalnum()))
    print('s.isalpha() = {}'.format(s.isalpha()))
    print('s.islower() = {}'.format(s.islower()))
    print('s.isupper() = {}'.format(s.isupper()))
    print('s.endswith("1234") = {}'.format(s.endswith('1234')))

    s = '     '
    print('s.isspace("     ") = {}'.format(s.isspace()))
    s = '  x  '
    print('s.isspace("  x  ") = {}'.format(s.isspace()))

    s = "This Is Title!!"
    print('s.istitle({}) => {}'.format(s, s.istitle()))
    s = "This is not title!!"
    print('s.istitle({}) => {}'.format(s, s.istitle()))

    print('There is a tab\t\there')



def string_join():
    '''
    String Join Function
    '''
    print('#############################')
    print('######## STRING JOIN ########')
    print('#############################')
    mylist = ['a', 'b', 'c']
    print('-'.join(mylist))
    print(' '.join(mylist))

def print_functions():
    '''
    print Function
    '''
    print('#################################')
    print('######## PRINT FUNCTIONS ########')
    print('#################################')
    print('A = {2}, B = {1}, C = {0}, a = {2}'.format('C', 'B', 'A'))
    print('A = {a}, B = {b}, C = {c}'.format(a='AAA', b='BBB', c='CCC'))
    result = 100/777
    print('result = {r}'.format(r=result))
    print('result = {r:1.3f}'.format(r=result))
    print('result = {r:10.3f}'.format(r=result))

    # New "f string" Method
    name = 'Jonathan'
    print(f'Hello, his name is {name}')

def lists():
    '''
    list
    '''
    print('######################')
    print('######## LIST ########')
    print('######################')
    list1 = [1, 2, 3]
    list2 = ['STRING', 100, 23.2]
    list3 = [5, 4, 3, 2, 1]
    list4 = [1, 1, 1, 1, 0, 1, 0, 1]
    print('list1 = {}'.format(list1))
    print('list2 = {}'.format(list2))
    print('list3 = {}'.format(list3))
    print('list4 = {}'.format(list4))

    print('len(list1) = {}'.format(len(list1)))
    print('list1[1] = {}'.format(list1[1]))
    print('list2[1:] = {}'.format(list2[1:]))
    print('list1 + list2 = {}'.format(list1 + list2))

    print('STRINGs are immutable')
    # String Immutabie
    #sam[0] = 'P' Cannot do this!
    print('LISTs are mutable')
    list1[0] = 10
    print('After list1[0] = 10, list1 = {}'.format(list1))
    list1.append(4) # return None
    print('list1.append(4) = {}'.format(list1))
    pop_item = list1.pop()
    print('list1.pop() = {}'.format(list1))
    pop_item = list1.pop(1)
    print('list1.pop(1) = {}'.format(list1))
    list3.sort() # return None
    print('list3.sort() = {}'.format(list3))
    list3.reverse() # return None
    print('list3.reverse() = {}'.format(list3))
    print('list4.count(1) = {}'.format(list4.count(1)))

    # Extend
    list6 = [1, 2, 3]
    list7 = [1, 2, 3]
    list6.append([4, 5])
    list7.extend([4, 5])
    print(list6)
    print(list7)

    # Index
    print('index = {}'.format(list6.index(3)))
    #print('index = {}'.format(list6.index(10))) # ValueError

    # Insert
    list6.insert(2, 'inserted')
    print(list6)
    list6.remove('inserted') # Only remove first found element from list
    print(list6)
    list6.pop(3) # pop index 3
    print(list6)

def dictionaries():
    '''
    dictionaries
    '''
    print('##############################')
    print('######## DICTIONARIES ########')
    print('##############################')
    d1 = {'key1':'value1', 'key2':'value2'}
    d2 = {'k1':123, 'k2':[0, 1, 2], 'k3':"abc"}
    print('d1 = {}'.format(d1))
    print('d2 = {}'.format(d2))
    print('d1["key1"] = {}'.format(d1['key1']))
    #print('d1["no_key"] = {}'.format(d1['no_key'])) => Error!!
    print('d2["k2"] = {}'.format(d2['k2']))
    print('d2["k3"][2] = {}'.format(d2['k2'][2]))
    print('d2["k3"][2].upper() = {}'.format(d2['k3'][2].upper()))

    d1['key1'] = 'new value'
    print('After d1["key1"] = "new value", d1 = {}'.format(d1))
    print('key100 doesn\'t exist:' + str('key100' in d1.keys()))

    print('d2.keys() = {}'.format(d2.keys()))
    print('d2.values() = {}'.format(d2.values()))
    print('d2.items() = {}'.format(d2.items()))

    d3 = {x: x**2 for x in range(10)}
    d4 = {k: v**2 for k, v in zip(['a','b'], range(10))}
    for i in d3.items():
        print(i)
    for v in d4.values():
        print(v)
    for k in d4.keys():
        print(k)

def tuples():
    '''
    tuples
    '''
    print('########################')
    print('######## TUPLES ########')
    print('########################')
    print('Tuples are immutable Lists')

    tuple1 = (1, 2, 3)
    tuple2 = ('a', 'a', 'b')
    list1 = [1, 2, 3]

    print('tuple1 = {}'.format(tuple1))
    print('tuple2 = {}'.format(tuple2))
    print('len(tuple1) = {}'.format(len(tuple1)))
    print('tuple1[1] = {}'.format(tuple1[1]))
    print('tuple1[-1] = {}'.format(tuple1[-1]))
    print('tuple1[0:2] = {}'.format(tuple1[0:2]))
    print('tuple2.count("a") = {}'.format(tuple2.count('a')))
    print('tuple2.index("a") = {}'.format(tuple2.index('a')))
    print('tuple2.index("b") = {}'.format(tuple2.index('b')))

def sets():
    '''
    sets
    '''
    print('######################')
    print('######## SETS ########')
    print('######################')

    set1 = set()
    #set2 = {1, 1, 1, 1, 2, 2, 3, 3, 3, 4}
    set2 = set([1, 1, 1, 1, 2, 2, 3, 3, 3, 4]) # can use list to init a set.
    set1.add(1)
    set1.add(2)
    set1.add(2)
    set2.discard(4)
    set2.discard(5) # discard non-exist element won't be an error
    print('set1 = {}'.format(set1))
    print('set2 = {}'.format(set2))

    set1.clear()
    set3 = set2.copy()
    set4 = {2, 3, 4}
    print('set1 = {}'.format(set1))
    print('set2 = {}'.format(set2))
    print('set3 = {}'.format(set3))
    print('set4 = {}'.format(set4))
    print('set3.intersection(set4) = {}'.format(set3.intersection(set4)))
    print('set3.difference(set4) = {}'.format(set3.difference(set4)))
    set5 = {1, 2, 3}
    set6 = {1, 4, 5}
    print('set5 = {}'.format(set5))
    print('set6 = {}'.format(set6))
    set3.intersection_update(set4)
    print('After set3.intersection(set4)')
    print('set3 = {}'.format(set3))
    set5.difference_update(set6)
    print('After set5.differrence_update(set6)')
    print('set5 = {}'.format(set5))

    set7 = {1, 2}
    set8 = {1, 2, 4}
    set9 = {5}
    print('set7 = {}'.format(set7))
    print('set8 = {}'.format(set8))
    print('set9 = {}'.format(set9))
    print('set7.isdisjoint(set8) = {}'.format(set7.isdisjoint(set8)))
    print('set7.isdisjoint(set9) = {}'.format(set7.isdisjoint(set9)))
    print('set7.issubset(set8) = {}'.format(set7.issubset(set8)))
    print('set8.issuperset(set7) = {}'.format(set8.issuperset(set7)))
    print('set8.union(set9) = {}'.format(set8.union(set9)))
    

def if_elif_else_comparison():
    '''
    if_elif_else_comparison
    '''
    print('#########################')
    print('######## If-Else ########')
    print('#########################')
    if not True:
        print('not(True) = {}'.format(not True))
    elif True and True:
        print('True and True = {}'.format(True and True))
    elif True or False:
        print('True or False = {}'.format(True and False))
    else:
        print('else')
    if 2 == 2.0:
        print('2 == 2.0'.format(2 == 2.0))

def for_loop():
    '''
    for loop
    '''
    print('##########################')
    print('######## For-Loop ########')
    print('##########################')

    for i in [1, 2, 3]:
        print(i)
    for i in (4, 5, 6):
        print(i)
    for c in 'Hello':
        print(c)

    for a, b in [(1, 2), (3, 4), (5, 6)]:
        print(a+b)
    for key in {'k1':1, 'k2':2, 'k3':3}:
        print(key)
    for tp in {'k1':1, 'k2':2, 'k3':3}.items():
        print(tp)
    for k, v in {'k1':1, 'k2':2, 'k3':3}.items():
        print((k, v))
    for v in {'k1':1, 'k2':2, 'k3':3}.values():
        print(v)

def while_loop():
    '''
    while loop
    '''
    print('############################')
    print('######## While-Loop ########')
    print('############################')
    x = 0
    while x < 3:
        x += 1
        #pass
        #continue
        #break
    else:
        print('jump out of while')

def for_with_range():
    '''
    for with range
    '''
    print('################################')
    print('######## For-with-Range ########')
    print('################################')
    for num in range(5):   # Not include 5
        print(num)
    for num in range(2, 5): # Not include 5
        print(num)
    for num in range(0, 10, 2): # Step size = 2
        print(num)

def for_with_enum():
    '''
    for with enum
    '''
    print('###############################')
    print('######## For-with-Enum ########')
    print('###############################')
    for item in enumerate('abcde'):
        print(item)

def list_comprehensions():
    '''
    list comprehensions
    '''
    print('#####################################')
    print('######## List-Comprehensions ########')
    print('#####################################')

    mystring = 'hello'

    mylist = [x for x in mystring]
    print(mylist)

    mylist = [x*10 for x in range(10, 20)]
    print(mylist)

    mylist = [x for x in range(10, 20) if x%2 == 0]
    print(mylist)

    celcius = [0, 10, 20, 34.5]

    fahrenheit = [((9/5)*temp+32) for temp in celcius]
    print(fahrenheit)

    mylist = []
    for x in [2, 4, 6]:
        for y in [1, 10, 100]:
            mylist.append(x*y)

    # Nested loop of list comprehension
    # Correct but hard to read
    mylist = [x*y for x in [2, 4, 6] for y in [1, 10, 100]]
    print(mylist)

def zip_operator():
    '''
    zip
    '''
    print('##############################')
    print('######## zip-Operator ########')
    print('##############################')
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    list3 = [100, 200, 300, -1, -1] # -1 will be ignored
    for item in zip(list1, list2, list3):
        print(item)

    print(list(zip(list1, list2, list3)))

def in_operator():
    '''
    in
    '''
    print('#############################')
    print('######## in-operator ########')
    print('#############################')
    print('x' in ['x', 'y', 'z'])
    print('x' in [1, 2, 3])
    print('a' in 'dcba')
    print('dog' in 'This is a dog')
    print('k2' in {'k1':1, 'k2':2, 'k3':3})
    print(1 in {'k1':1, 'k2':2, 'k3':3}.values())
    print(('k3', 3) in {'k1':1, 'k2':2, 'k3':3}.items())

def min_max_operator():
    '''
    max & min
    '''
    print('##################################')
    print('######## min-max-operator ########')
    print('##################################')
    num_list = [1, 2, 3, 4, 5]
    print(min(num_list))
    print(max(num_list))

def methods_help():
    '''
    methods help
    '''
    print('##############################')
    print('######## methods_help ########')
    print('##############################')
    my_list = [1, 2, 3]
    # 1. help(my_list.append)
    # 2. pydoc3 list.append

def args_function(*args):
    '''
    You can pass in any number of parameter
    It will treat it as a tuple
    '''
    print('#######################')
    print('######## *args ########')
    print('#######################')
    print(type(args))
    print(args)

def kwargs_function(**kwargs):
    '''
    You can pass in any number of parameter with value
    It will treat it as a dictionary
    '''
    print('##########################')
    print('######## **kwargs ########')
    print('##########################')
    print(type(kwargs))
    print(kwargs)

def args_kwargs_function(*args, **kwargs):
    '''
    You can combine *args and **kwargs
    '''
    print('##################################')
    print('######## *args & **kwargs ########')
    print('##################################')
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)

def square(num):
    '''
    return square of a num
    '''
    return num**2

def check_even(num):
    '''
    Check wether it's even
    '''
    return num % 2 == 0

def map_function():
    '''
    map function
    '''
    print('##################################')
    print('######## map function ############')
    print('##################################')
    my_list = [1, 2, 3, 4, 5]
    print(list(map(square, my_list)))
    for n in map(square, my_list):
        print(n)

def filter_function():
    '''
    filter function
    '''
    print('#####################################')
    print('######## filter function ############')
    print('#####################################')
    my_list = [1, 2, 3, 4, 5]
    print(list(filter(check_even, my_list)))
    for n in filter(check_even, my_list):
        print(n)

def lambda_function():
    '''
    lambda function
    '''
    print('#####################################')
    print('######## lambda function ############')
    print('#####################################')
    my_list = [1, 2, 3, 4, 5]
    print(list(map(lambda num: num**2, my_list)))

def exceptions():
    '''
    All built-in Error Types
    https://docs.python.org/3.7/library/exceptions.html
    '''
    print('############################')
    print('######## Exceptions ########')
    print('############################')
    try:
        #2 + 'a'
        #f = open('non-exist-file', 'r')
        3/0
    except TypeError:
        print('TypeError Error')
    except OSError:
        print('OSError Error')
    except ZeroDivisionError:
        print('ZeroDivisionError Error')
    except Exception as e:
        print('Other Types of Error: ')
        print(e)
    else:
        print('No error occurrs')
    finally:
        print('finally always runs')

def gen_fibon(n):
    '''
    Generator for fibonnacci numbers
    '''
    print('Called gen_fibon()')
    a = 1
    b = 1
    for i in range(n):
        print('\tyield a')
        yield a
        print('\ta, b = b, a+b')
        a, b = b, a+b

def generator():
    '''
    range(N) is a genrator,
    instead of storing things in the list, it gives you the value one by one.
    How to create your own genrator? let's find out!
    '''
    print('###########################')
    print('######## Generator ########')
    print('###########################')
    a = gen_fibon(10)
    print('called next(a)')
    print(next(a))
    print('called next(a)')
    print(next(a))
    print('called next(a)')
    print(next(a))
    print('called next(a)')
    print(next(a))
    print('called next(a)')
    print(next(a))
    print('called next(a)')
    print(next(a))
    print('called next(a)')

    for a in gen_fibon(5):
        print(a)   
    print(list(gen_fibon(5)))   

    '''
    string object is not an iterator
    but you can use iter() to convert to it
    '''
    s = 'HELLO'
    s_iter = iter(s)
    print(next(s_iter))
    print(next(s_iter))
    print(next(s_iter))
    print(next(s_iter))
    print(next(s_iter))


if __name__ == '__main__':

    # Data Structures
    numbers()
    variables()
    string_slice_indexing()
    string_useful_functions()
    string_join()
    print_functions()
    lists()
    dictionaries()
    tuples()
    sets()

    # if-elif-else + comparison Operators
    if_elif_else_comparison()

    # Loop
    for_loop()
    while_loop()
    for_with_range()
    for_with_enum()
    list_comprehensions()

    # Useful Operators
    zip_operator()
    in_operator()
    min_max_operator()

    # Methods and functions
    methods_help()
    args_function(1, 2, 3)
    kwargs_function(a=1, b=2, c=3)
    args_kwargs_function(4, 5, 6, d=4, e=5, f=6)
    map_function()
    filter_function()
    lambda_function()

    # Exeption
    exceptions()

    # Generator
    generator()
