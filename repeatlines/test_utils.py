from .utils import repeat_text


def test_repeat_once():
    result = repeat_text('Nothing should happen. to! this string.', 1)
    assert result == 'Nothing should happen. to! this string.'


def test_repeat_simple_sentence():
    result = repeat_text('This is a sentence.', 3)
    assert result == '''\
This is a sentence.
This is a sentence.
This is a sentence.'''


def test_repeat_simple_sentence_no_fullstop():
    result = repeat_text('This is a single sentence which does not end in a full stop', 3)
    assert result == '''\
This is a single sentence which does not end in a full stop
This is a single sentence which does not end in a full stop
This is a single sentence which does not end in a full stop'''


def test_repeat_simple_sentence():
    result = repeat_text('This is a sentence. This is another', 2)
    assert result == '''\
This is a sentence.
This is a sentence.
This is another
This is another'''


def test_paragraph():
    result = repeat_text('''\
This is a sentence.
This is another


This is a different paragraph!
And it has two sentences as well plus a trailing line.''', 2)
    assert result == '''\
This is a sentence.
This is a sentence.
This is another
This is another


This is a different paragraph!
This is a different paragraph!
And it has two sentences as well plus a trailing line.
And it has two sentences as well plus a trailing line.'''


def test_leading_and_trailing_newlines():
    result = repeat_text('\nThis is a sentence.\n\n\n\nThis is another\n', 2)
    assert result == '''\
This is a sentence.
This is a sentence.


This is another
This is another'''


def test_punctuation_all_together():
    result = repeat_text('This is a sentence... This is another?!\n\nAnd the last one.', 2)
    assert result == '''\
This is a sentence...
This is a sentence...
This is another?!
This is another?!
And the last one.
And the last one.'''


def test_default_punctuation():
    result = repeat_text('AAA! BBB( CCC) DDD. EEE: FFF; GGG?', 2)
    assert result == '''\
AAA!
AAA!
BBB(
BBB(
CCC)
CCC)
DDD.
DDD.
EEE:
EEE:
FFF;
FFF;
GGG?
GGG?'''