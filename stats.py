def get_num_words(text):
    num_words = len(text.split())
    return f"Found {num_words} total words"

def count_characters(text):
    char_counts = {}

    for t in text.lower():
        if t.isalpha():
            if t not in char_counts:
                char_counts[t] = 1
            else:
                char_counts[t] += 1
    
    return char_counts

def sort_on(dict):
    return dict["num"]

def dict_sort(text):
    char_list = [{"char": key, "num": value} for key, value in count_characters(text).items()]

    return sorted(char_list, reverse=True, key=sort_on)