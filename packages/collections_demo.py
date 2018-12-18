from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple

def Counter_demo():
    '''
    Counter is a module convert a list into a dictionary
    '''
    print('##############################')
    print('######## Counter Demo ########')
    print('##############################')

    num =  [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3]
    chars = 'asdfasdasdfasdfasdadfasdf'
    words = 'jonathan may may penny jonathan may penny penny'

    num_counter   = Counter(num)
    chars_counter = Counter(chars)
    words_counter = Counter(words.split())

    print(num_counter)
    print(num_counter.values())
    print(list(num_counter))

    # Returns a list of tuples indicating 2 most common elements.
    print('most_common()')
    print(num_counter.most_common(2))
    # Returns a list of tuples indicating all least common elements.
    print(num_counter.most_common()[::-1])

    print(sum(num_counter.values()))

    print(num_counter.clear())
    print(num_counter)

    print(chars_counter)
    print(dict(chars_counter))
    print(words_counter)
    print(set(words_counter))
    print(words_counter.items())

def defaultdict_demo():
    '''
    defaultdict is dict that has default value
    '''
    print('##################################')
    print('######## defaultdict Demo ########')
    print('##################################')

    # For normal dict, if you invoke a key which isn't exist,
    # it will throw an KeyError.
    d = {'k1': 1}
    try:
        d['k2']
    except KeyError as e:
        print('KeyError')

    # Ny using defaultdict(), there won't be such problem.
    # Since you can assign a default value for those non-existing keys.
    df_dict = defaultdict(lambda: -1)
    df_dict['one']
    df_dict['two']
    df_dict['three'] = 3
    print(df_dict)

def OrderedDict_demo():
    '''
    OrderDict is dict that keeps their added order
    '''
    print('##################################')
    print('######## OrderedDict Demo ########')
    print('##################################')

    #od1 = dict()
    od1 = OrderedDict()
    od1['a'] = 1
    od1['b'] = 2
    od1['c'] = 3
    od1['d'] = 4
    od1['e'] = 5

    #od2 = dict()
    od2 = OrderedDict()
    od2['e'] = 5
    od2['d'] = 4
    od2['c'] = 3
    od2['b'] = 2
    od2['a'] = 1

    for k, v in od1.items():
        print(k, v)

    # They are not equal since their added orver
    print(od1 == od2)

def namedtuple_demo():
    '''
    namedtuple is s tuple has names as well as indexes for every entry
    '''
    print('#################################')
    print('######## namedtuple Demo ########')
    print('#################################')
    ## If's pretty like creating a class callled Dog
    Dog = namedtuple('Dog', 'age breed name')
    may = Dog(age=7, breed='Schnauzer', name='MayMay')
    print(may.age)
    print(may[0])

if __name__ == '__main__':

    Counter_demo()
    defaultdict_demo()
    OrderedDict_demo()
    namedtuple_demo()
    # Others
    # - deque
    # - ChainMap
    # - UserDict
    # - UserList
    # - UserString
