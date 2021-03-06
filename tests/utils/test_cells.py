import pytest

from alive_progress.utils.cells import to_cells


@pytest.mark.parametrize('text, expected', [
    ('', ''),
    (None, ''),
    ('a text', 'a text'),
    ('\n', ' '),
    (' \n ', '   '),
    ('\n \n', '   '),
    ('\r', ' '),
    (' \r ', '   '),
    ('\r \n', '   '),
    ('asd\n', 'asd '),
    ('\nasd', ' asd'),
    ('asd1\nasd2', 'asd1 asd2'),
    ('asd1 \nasd2', 'asd1  asd2'),
    ('asd1 \r\nasd2', 'asd1   asd2'),
    ('\nasd1\n \r \nasd2\r', ' asd1     asd2 '),
])
def test_sanitize_text_normal_chars(text, expected, show_marks):
    result = to_cells(text)
    assert show_marks(result) == expected


@pytest.mark.parametrize('text, expected', [
    ('ðº', 'ðºX'),
    ('\nðº', ' ðºX'),
    ('ðº \n ðº', 'ðºX   ðºX'),
    ('\n ðº\nðº', '  ðºX ðºX'),
    ('asdðº\n', 'asdðºX '),
    ('ðº\nasd', 'ðºX asd'),
    ('asd1\rasd2ðº', 'asd1 asd2ðºX'),
    ('\nasd1ðº\nðº\n\rasd2\r', ' asd1ðºX ðºX  asd2 '),
])
def test_sanitize_text_wide_chars(text, expected, show_marks):
    result = to_cells(text)
    assert show_marks(result) == expected


@pytest.mark.parametrize('text, expected', [
    ('ok', 'ok'),
    ('ðº', 'ðºX'),
    ('ðºðº', 'ðºXðºX'),
    ('ðºokðº', 'ðºXokðºX'),
])
def test_sanitize_text_double(text, expected, show_marks):
    result = to_cells(text)
    assert show_marks(result) == expected
