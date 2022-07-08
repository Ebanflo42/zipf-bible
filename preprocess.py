import pdfplumber as pdf
from tqdm import tqdm


# a lot of this nastiness I found just by looking at
# what was lying around in the raw text
def clean_text(text: str):

    cleaned_text = text.replace('\n', ' ')
    cleaned_text = cleaned_text.replace('-', ' ')
    cleaned_text = cleaned_text.replace('—', ' ')
    cleaned_text = cleaned_text.replace('.', ' ')
    cleaned_text = cleaned_text.replace(',', ' ')
    cleaned_text = cleaned_text.replace(';', ' ')
    cleaned_text = cleaned_text.replace('?', ' ')
    cleaned_text = cleaned_text.replace('!', ' ')

    cleaned_text = cleaned_text.replace(':', '')
    cleaned_text = cleaned_text.replace('(', '')
    cleaned_text = cleaned_text.replace(')', '')
    cleaned_text = cleaned_text.replace('\'', '')
    cleaned_text = cleaned_text.replace('’', '')
    cleaned_text = cleaned_text.replace('‘', '')
    cleaned_text = cleaned_text.replace('"', '')
    cleaned_text = cleaned_text.replace('“', '')
    cleaned_text = cleaned_text.replace('”', '')
    cleaned_text = cleaned_text.replace('/', '')

    for i in range(10):
        cleaned_text = cleaned_text.replace(str(i), '')

    cleaned_text = cleaned_text.replace(' b ', ' ')
    cleaned_text = cleaned_text.replace(' c ', ' ')
    cleaned_text = cleaned_text.replace(' d ', ' ')
    cleaned_text = cleaned_text.replace(' e ', ' ')
    cleaned_text = cleaned_text.replace(' f ', ' ')
    cleaned_text = cleaned_text.replace(' g ', ' ')
    cleaned_text = cleaned_text.replace(' h ', ' ')
    cleaned_text = cleaned_text.replace(' j ', ' ')
    cleaned_text = cleaned_text.replace(' k ', ' ')
    cleaned_text = cleaned_text.replace(' l ', ' ')
    cleaned_text = cleaned_text.replace(' m ', ' ')
    cleaned_text = cleaned_text.replace(' n ', ' ')

    cleaned_text = cleaned_text.replace('A D', 'AD')
    cleaned_text = cleaned_text.replace('B C', 'BC')

    return cleaned_text


if __name__ == '__main__':

    print('Extracting text from PDF . . .')

    with open('raw_text.txt', 'a') as tfile:
        with pdf.open('bible.pdf') as pfile:
            for i in tqdm(range(13, 1596)):
                text = pfile.pages[i].extract_text()
                tfile.write(text + '\n')

    print('Cleaning text file . . .')

    with open('raw_text.txt', 'r') as f:
        text = f.read()
    cleaned_text = clean_text(text)
    with open('cleaned_text.txt', 'w') as f:
        f.write(cleaned_text)