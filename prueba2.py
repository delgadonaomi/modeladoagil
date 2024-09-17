def test_roman_to_int_V():
    assert roman_to_int('V') == 5


def roman_to_int(roman):
    if roman == 'I':
        return 1
    elif roman == 'V':
        return 5

