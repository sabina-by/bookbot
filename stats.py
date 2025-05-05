def get_num_words(book_text):
    return len(book_text.split())

def get_num_char(book_text):
    char_dict = {}
    for char in book_text:
        lowered = char.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict
    # lower_char = book_text.lower()
    # for char in lower_char:
    #     char_dict[char] = lower_char.count(char)
    # return char_dict

def sort_on(dict):
    return dict["num"]

def get_sorted_list(char_dict):
    dict_list = []
    for key in char_dict:
        dict_list.append({"char": key, "num": char_dict[key]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list    
