import re

def search_func():
    print('#################')
    print('## re.search() ##')
    print('#################')
    patterns = ['term1', 'term2']

    text = 'This is a string with term1, but not the other term'

    # If a pattern is found, it will return a object
    match = re.search('hello', 'hellow world!')
    print(match)
    print(match.start())
    print(match.end())

    # else, return none.
    not_match = re.search('loha', 'hellow world!')
    print(not_match)


def split_func():
    print('################')
    print('## re.split() ##')
    print('################')
    split_term = '@'
    phrase = 'What is your email, is it hellow@gmail.com?'
    split_result = re.split(split_term, phrase)
    print(split_result)


def findall_func():
    print('###################')
    print('## re.findall() ##')
    print('###################')
    test_patterns = ['ab*',     # a followed by zero or more b's
                     'ab+',     # a followed by one or more b's
                     'ab?',     # a followed by zero or one b's
                     'ab{3}',   # a followed by three b's
                     'ab{2,3}', # a followed by two ro three b's
                     '[1a]',    # either 1 or a
                     '9[1a]+',  # 9 followed by one or more 1 or a
                    ]
    text = '123456789abbcdefgabcdeabbbc'

    found = re.findall('ab*', text)
    print(found)
    found = re.findall('ab+', text)
    print(found)
    found = re.findall('ab?', text)
    print(found)
    found = re.findall('ab{3}', text)
    print(found)
    found = re.findall('ab{2,3}', text)
    print(found)
    found = re.findall('[1a]', text)
    print(found)
    found = re.findall('9[1a]+', text)
    print(found)

    text = 'ABC 123,Def@456*Ghi$789'
    found = re.findall('[^ ,@*$]+', text)
    print(found)
    found = re.findall('[A-Z][a-z]+', text)
    print(found)

    found = re.findall(r'\d+', text)     # Find sequence of digits
    print(found)
    found = re.findall(r'\D+', text)     # Find sequence of non-digits
    print(found)
    found = re.findall(r'\s+', text)     # Find sequence of whitespace
    print(found)
    found = re.findall(r'\S+', text)     # Find sequence of non-whitespace
    print(found)
    found = re.findall(r'\w+', text)     # Find sequence of non-whitespace
    print(found)
    found = re.findall(r'\W+', text)     # Find sequence of non-whitespace
    print(found)

if __name__=='__main__':
    search_func()
    split_func()
    findall_func()
