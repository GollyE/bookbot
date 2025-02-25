def word_count(input_text):
    num_of_words = len(input_text.split())
    return num_of_words

def char_dict(input_text):
    character_dict = {}
    for letter in input_text:
        letter = letter.lower()
        try:
            character_dict[letter]+=1
        except Exception:
            character_dict[letter] = 1
    return character_dict

def sort_on(dict):
    return dict["num"]

def sorted_list_dict(character_count_dict):
    s_list = []
    for key in character_count_dict:
        s_list.append({"key":key, "num": character_count_dict[key]})
    s_list.sort(reverse=True, key=sort_on)
    return s_list

