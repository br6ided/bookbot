def get_num_words(text):
    w = len(text.split())
    return w

def char_frequency(t):
    t = t.lower()
    char_dict = {}
    for char in t:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def dict_to_list(n):
    l_of_dict = []
    for k,v in n.items():
        l_of_dict.append({"char": k, "num": v})
    return l_of_dict

def sort_on(i):
    return i["num"]
