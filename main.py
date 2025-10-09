from stats import get_num_words,char_frequency,dict_to_list,sort_on
import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    f = sys.argv[1]


def get_book_text(fi):
    with open(fi) as f:
        contents = f.read()
    return contents

def refined_list(d):
    clist = []
    for dic in d:
        if dic["char"].isalpha():
            clist.append(dic)
    return clist

def nice_printout(d):
    for dic in d:
        print(f"{dic["char"]}: {dic["num"]}")
    return None

def main():
    filepath = f"{f}"
    text = get_book_text(filepath)
    words = get_num_words(text)
    frequency = char_frequency(text)
    char_dict_list = dict_to_list(frequency)
    char_dict_list = refined_list(char_dict_list)
    char_dict_list.sort(reverse=True, key=sort_on)
# lowkey a print section
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print(f"----------- Word Count ----------")
    print(f"Found {words} total words")
    print(f"--------- Character Count -------")
    nice_printout(char_dict_list)
    print(f"============= END ===============")

if __name__ == "__main__":
    main()