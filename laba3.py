from collections import Counter


def transpose(mat):  # задача 1
    # [list(i) for i in zip(*mat)]
    return list(zip(*mat))

def assign_pets(lst):  # задача 2
    pets_dict = {}
    for tup in lst:
        owner = '{0} {1}'.format(tup[2], tup[3])
        pets = '{0}, возраст - {1}'.format(tup[0], tup[1])
        # pets_dict.setdefault(owner, list()).append(pets)
        if owner not in pets_dict:
            pets_dict.setdefault(owner, pets)
        else:
            pets_dict.update({owner: pets_dict.get(owner) + '; ' + pets})
    return pets_dict


def rarest_word(string):  # задача 3
    if not string or string.isdigit():
        return 'Нет слов'
    new_string = ''
    for i in string:
        if i.isalpha() or i.isspace():
            new_string = new_string + i.lower()

    split_string = new_string.split()
    word_freqs = Counter(split_string)

    if not word_freqs:
        return 'Нет слов'
    words = [i for i in word_freqs if word_freqs.get(i) == min(word_freqs.values())]
    return sorted(words)[0]


def most_frequent_word(string):  # задача 4
    if not string or string.isdigit():
        return 'Нет букв'
    new_string = ''.join(filter(str.isalpha, string.lower()))

    letters = Counter(new_string)

    if not letters:
        return 'Нет букв'

    max_value = max(letters.values())
    max_letters = [i for i in letters if letters[i] == max_value]
    return sorted(max_letters)[0]


def palindrome(string):  # задача 5
    string = string.replace(' ', '')

    result = True
    if len(string) > 1:
        if string[0].lower() == string[-1].lower():
            result = palindrome(string[1:-1])
        else:
            result = False
    return result


def freq_sort(array):  # задача 6
    nums = Counter(array)

    inverse_nums = {}
    for key, value in nums.items():
        inverse_nums.setdefault(value, list()).append(key)

    sorted_nums = dict(sorted(inverse_nums.items()))

    result = []
    for key, value in sorted_nums.items():
        for numbers in value:
            result.extend([numbers for i in range(key)])
    return result


def three_conseq_words(string):  # задача 7
    array = string.split()
    count = 0
    for i in range(len(array)):
        count += 1
        if not array[i].isalpha():
            count = 0
        if count == 3:
            return True
    return False


def max_consequence(string):  # задача 8
    string = string.lower()
    count = 1
    save = 0
    for i in range(len(string) - 1):
        if string[i] == string[i + 1] and string[i].isalpha():
            count += 1
            save = count if save < count else save
        else:
            count = 1
    return save


def math_expression(string):  # задача 9
    try:
        return eval(string)
    except Exception as e:
        return e


def summed_dict(list_of_dicts):  # задача 10
    new_dict = {}

    for dic in list_of_dicts:
        for key in dic.keys():
            if key not in new_dict.keys():
                new_dict.setdefault(key, dic.get(key))
            else:
                new_dict.update({key: new_dict.get(key) + dic.get(key)})
    return new_dict