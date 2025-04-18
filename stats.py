def num_of_words(path):
    with open(path) as f:
        count = 0
        file_contents = f.read()
        words = file_contents.split()
        for i in words:
            count += 1
        return count

def char_counter(text):
    dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in dict:
            dict[lowered] += 1
        else:
            dict[lowered] = 1
    return dict

def sort_on(dict):
    return dict["num"]

def sort_dict(char_dict):
    list = []
    for ch in char_dict:
        list.append({"char": ch, "num": char_dict[ch]})
    list.sort(reverse=True, key=sort_on)
    return list

