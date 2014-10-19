import re
import sys
import PyPDF2

PUNCTUATION = '!().:;?'

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


def repeat_text(text, n):
    text_blocks = re.split('\n\n\n+', text)
    return '\n\n\n'.join(repeat_text_block(tb, n) for tb in text_blocks)

def repeat_text_block(text_block, n):
    sentences = split_sentences(text_block)
    repeated_sentences = []
    for s in sentences:
        for _ in xrange(n):
            repeated_sentences.append(s)
    return '\n'.join(repeated_sentences)

def split_sentences(text):
    sentences = []
    last_sentence_end = 0
    for i, c in enumerate(text):
        if c in PUNCTUATION:
            sentences.append(text[last_sentence_end:i + 1])
            last_sentence_end = i + 1
    sentences.append(text[last_sentence_end:len(text)])
    return sentences

