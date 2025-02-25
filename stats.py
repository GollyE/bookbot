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

