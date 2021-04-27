# reads file
def read_file(file_path):
    strings = []
    with open(file_path, 'r') as file:
        strings = file.read()
    return strings.split('\n')


'''makes file type  = lists of lists (making a list from every string)'''


def get_lists_of_strings(strings):
    new_lists = list(map(str.split, strings))
    return new_lists


'''choose words that i have to delete from my lists'''


def build_list_to_delete(lists_to_delete):
    for i in range(len(lists_to_delete)):
        lists_to_delete[i] = list(filter(lambda x: (5 >= len(x) >= 3), lists_to_delete[i]))
    return lists_to_delete


'''checking if there is a odd number of these words - if otherwise i remove one word of "list to delete'''


def check_if_odd(lists_to_delete):
    for i in range(len(lists_to_delete)):
        if len(lists_to_delete[i]) % 2 != 0:
            del lists_to_delete[i][-1]
    return lists_to_delete


''' deleting words from 'lists to delete' from my lists '''


def making_new_lists(users_lists, users_lists_to_delete):
    for i in range(len(users_lists)):
        users_lists[i] =[item for item in users_lists[i] if item not in users_lists_to_delete[i]]
    return users_lists


''' making data a string type: it is it's final form before rewriting it'''


def make_data_str_type(file_data):
    string_file_data = "".join(map(lambda x: str(" ".join(x)) + '\n', file_data))
    return string_file_data


def write_to_file(file_path, file_data):
    with open(file_path, 'w') as file:
        file.writelines(file_data)


def main(file_path):
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
    write_to_file('test_file2', proper_words_list_str)


if __name__ == '__main__':
    main('test_file2')