# reads file
def read_file(file_path):
    strings = []
    with open(file_path, 'r') as file:
        strings = file.read()
    return strings.split('\n')

# makes file type  = lists of lists (making a list from every string)


def get_lists_of_strings(strings):
    new_lists = list(map(str.split, strings))
    return new_lists

# choose words that i have to delete from my lists


def build_list_to_delete(lists_to_delete):
    for i in range(len(lists_to_delete)):
        lists_to_delete[i] = list(filter(lambda x: (5 >= len(x) >= 3), lists_to_delete[i]))
    return lists_to_delete


# checking if there is a odd number of these words - if otherwise i remove one word of "list to delete"
def check_if_odd(lists_to_delete):
    for i in range(len(lists_to_delete)):
        if len(lists_to_delete[i]) % 2 != 0:
            del lists_to_delete[i][-1]
    return lists_to_delete


# deleting words from 'lists to delete' from my lists
def making_new_lists(users_lists, users_lists_to_delete):
    for i in range(len(users_lists)):
        users_lists[i] = list(set(users_lists[i]) - set(users_lists_to_delete[i]))
    return users_lists


# failed attempt to make strings from lists
def make_data_str_type(file_data):
    string_file_data = list(map(lambda x: str(x) + '\n', file_data))
    return string_file_data


def turn_lists_into_strings(file_data):
    file_data = ''.join(file_data)
    return file_data


def write_to_file(file_path, file_data):
    with open(file_path, 'w') as file:
        file.writelines(file_data)


users_strings = read_file('test_file2')
print(read_file("test_file2"))
new_lists = get_lists_of_strings(users_strings)
print(new_lists)
list_to_delete = build_list_to_delete(new_lists)
print(list_to_delete)
odd_lists_to_delete = check_if_odd(list_to_delete)
print(odd_lists_to_delete)
new_lists = get_lists_of_strings(users_strings)
print(new_lists)
proper_words_list = making_new_lists(new_lists, odd_lists_to_delete)
print(proper_words_list)
proper_words_list_str = make_data_str_type(proper_words_list)
print(proper_words_list_str)
proper_lists = turn_lists_into_strings(proper_words_list_str)
print(proper_lists)


write_to_file('test_file3', proper_lists)