import numpy as np
from tqdm import tqdm


if __name__ == '__main__':

    with open('cleaned_text.txt', 'r') as f:
        text = f.read()

    # get rid of case sensitivity and empty strings
    words = [word.lower() for word in text.split(' ') if len(word) > 0]

    freq_dict = {}
    word_set = set()
    for word in tqdm(words):
        # plurals and possessives are considered to be the same word
        if word in word_set:
            freq_dict[word] += 1
        elif word + 's' in word_set:
            freq_dict[word + 's'] += 1
        elif word.endswith('s') and word[:-1] in word_set:
            freq_dict[word[:-1]] += 1
        else:
            word_set.add(word)
            freq_dict[word] = 1

    word_list = []
    freq_list = []
    for word, freq in freq_dict.items():
        word_list.append(word + '\n')
        freq_list.append(freq)

    np.save('frequencies', freq_list)
    with open('words.txt', 'w') as f:
        f.writelines(word_list)