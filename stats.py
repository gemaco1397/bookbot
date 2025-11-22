
def sort_on(items):
    return items["num"]

def get_book_words(book):
    words_array = book.split()
    return len(words_array)

def get_letters_used(book):
    letters_used = {}
    for letter in book:
        current_letter = letter.lower()
        
        if current_letter not in letters_used:
            letters_used[current_letter] = 1
        letters_used[current_letter] += 1
    sort_dictionary(letters_used)
    return letters_used

def sort_dictionary(dict_to_sort):
    sorted_list = []
    for characters in dict_to_sort:
        sorted_list.append({"char": characters, "num": dict_to_sort[characters]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
