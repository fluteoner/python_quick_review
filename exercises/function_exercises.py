def lesser_of_two_evens(*args):
    '''
    Write a function that returns the lesser of two given numbers if both numbers are even,
    but returns the greater if one or both numbers are odd
    '''
    assert(len(args) > 0)
    l = [even for even in args if even % 2 == 0]
    if len(l) == len(args):
        # All are even
        return min(l)
    else:
        return max(args)

#print(lesser_of_two_evens())
print(lesser_of_two_evens(2))
print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5, 1, 4, 6))

def animal_crackers(text):
    '''
    Write a function takes a two-word string and returns True if both words begin with same letter
    '''
    assert(len(text) > 0)
    l = text.split(' ')
    for word in l:
        if l[0][0] != word[0]:
            return False
    return True

#print(animal_crackers(''))
print(animal_crackers('Levelheaded'))
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))


def old_macdonald(name):
    '''
    write a function that capitalizes that the first and fourth letters of a name
    '''
    assert(len(name) >= 4)
    return name[0].upper() + name[1:3] + name[3].upper() + name[4:]

#print(old_macdonald('mac'))
print(old_macdonald('macd'))
print(old_macdonald('macdonald'))

def master_yoda(text):
    '''
    Given a sentence, return a sentence with the words reversed
    '''
    if len(text) == 0:
        return text
    l = text.split(' ')
    l.reverse()
    return ' '.join(l)

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

def laugther(pattern, text):
    '''
    Write a function that counts the number of times a given pattern appears in a string,
    including overlap
    '''
    assert(len(pattern) > 0)
    size = len(pattern)
    cnt = 0

    for i in range(len(text)-size+1):
        if text[i:i+size] == pattern:
            cnt += 1
    return cnt

#print(laugther('', 'asdf'))
print(laugther('hah', ''))
print(laugther('hah', 'hahahah'))
print(laugther('432', '239872409827345432'))

def paper_doll(text):
    '''
    Given a string, return a string where for every character in the original there are three characters
    '''
    result = ''
    for c in text:
        result += c+c+c
    return result

print(paper_doll(''))
print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

def blackjack(*args):
    '''
    Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
    If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum(even
    after adjustment) exceeds 21, return 'BUST'
    '''
    card_sum = sum(args)
    elevent_cnt = args.count(11)
    if card_sum <= 21:
        return card_sum
    elif elevent_cnt > 0:
        return card_sum - 10*elevent_cnt
    else:
        return 'BUST'

print(blackjack())
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))
print(blackjack(11,11,9,9,11))

def summer_69(list_nums):
    '''
    Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and
    extending to the next 9(every 6 will be followed by at least one 9). Return 0 for no numbers.
    '''
    is_summer = False
    sum_of_nums = 0

    for num in list_nums:
        if num == 6:
            is_summer = True
            continue
        elif num == 9:
            is_summer = False
            continue
        if is_summer == False:
            sum_of_nums += num 
    return sum_of_nums

print(summer_69([]))
print(summer_69([1,3,5]))
print(summer_69([4,5,6,7,8,9]))
print(summer_69([2,1,6,9,11]))

def spy_game(list_nums):
    '''
    Write a function that takes in a list of integers and returns True if it contains 007 in order
    '''
    pattern = [0,0,7]

    if len(pattern) > len(list_nums):
        return False

    prev_index = -1

    for p in pattern:
        index = list_nums.index(p)
        if index < prev_index:
            return False
        prev_index = index

    return True

print(spy_game([]))
print(spy_game([0,0,7]))
print(spy_game([7,0,0]))
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

def is_prime(num):
    '''
    Write a function that returns whether it's a prime number
    '''
    if num % 2 == 0:
        return False

    upper_bound = int(num**0.5)
    for v in range(2 ,int(num**0.5)+1):
        if num % v == 0:
            return False
    return True

def count_primes(num):
    '''
    Write a function that returns the number of prime numbers that exist up to and inculding a given
    number
    '''
    num_of_primes = 0
    for v in range(2, num+1):
        if is_prime(v):
            num_of_primes += 1
    return num_of_primes + 1 # plus one because 2 is not included

print(is_prime(2))
print(is_prime(6))
print(is_prime(7))
print(count_primes(100000))

def unique_list(input_list):
    '''
    [1,1,1,2,2,3,3,3,3,4] -> [1,2,3,4]
    '''
    if len(input_list) == 0:
        return input_list

    result = [input_list[0]]

    for v in input_list[1:]:
        if v == result[-1]:
            continue
        else:
           result.append(v)
    return result

print(unique_list([]))
print(unique_list([1]))
print(unique_list([1,1,1,2,2,3,3,3,3]))

def palindromme(input_string):
    '''
    Check if it's palindrome, ex. abcdedcba
    '''
    if len(input_string) == 0:
        return True
    
    forward_index = 0
    backward_index = len(input_string)-1
    while backward_index > forward_index:
        if input_string[forward_index] != input_string[backward_index]:
            return False
        forward_index += 1
        backward_index -= 1

    return True

print(palindromme(''))
print(palindromme('a'))
print(palindromme('ab'))
print(palindromme('aba'))
print(palindromme('1221'))
print(palindromme('12321'))
