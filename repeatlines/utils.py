import re
import sys
import PyPDF2

# Default punctuation used to distinguish sentences
DEFAULT_PUNCTUATION = '!.:;?'


def pdf_to_text(filename):
    text = []
    with open(filename, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        for page in pdf.pages:
            text.append(page.extractText())

    text = '\n'.join(text)
    text = re.sub('  +', '\n', text)
    text = filter(None, '\n'.join([l.strip() for l in text.splitlines()]))
    return text


def repeat_text(text, n, punctuation=DEFAULT_PUNCTUATION):
    if n == 0:
        return ''
    if n == 1:
        return text
    text_blocks = re.split('\n\n\n+', text)
    return '\n\n\n'.join(repeat_text_block(tb, n, punctuation) for tb in text_blocks)


def repeat_text_block(text_block, n, punctuation=DEFAULT_PUNCTUATION):
    splitted_sentences = split_sentences(text_block, punctuation)
    repeated_sentences = repeat_list_elements(splitted_sentences, n)
    return '\n'.join(repeated_sentences)


def repeat_list_elements(l, n):
    repeated_l = []
    for el in l:
        for _ in range(n):
            repeated_l.append(el)
    return repeated_l


def split_sentences(text, punctuation=DEFAULT_PUNCTUATION):
    """
    Splits the given text into sentences according to the given punctuation.
    If multiple punctuation characters appear together they are taken as one.
    Leading and trailing spaces are stripped from each sentence.
    Ex:
    split_sentences('Foo... Bar?! Hello.') == ['Foo...', 'Bar?!', 'Hello']
    """
    sentences = []
    last_sentence_end = 0
    state = 'in_text'
    for i, c in enumerate(text):
        if c in punctuation:
            state = 'in_punctuation'
        elif state == 'in_punctuation':
            if c.islower():
                # Found a lowercase letter after punctuation, so we're still
                # in the same sentence and should ignore the last punctuation found.
                state = 'in_text'
            elif c.isupper():
                # Found a uppercase letter after punctuation,
                # so the last sentence is over.
                sentence = text[last_sentence_end:i].strip()
                sentences.append(sentence)
                last_sentence_end = i
                state = 'in_text'
            # If the character is not a letter we just keep going until we find one.
    last_sentence = text[last_sentence_end:len(text)].strip()
    if last_sentence:
        sentences.append(last_sentence)
    return sentences

