def test_roman_to_int_X():
    assert roman_to_int('X') == 10

def roman_to_int(roman):
    if roman == 'I':
        return 1
    elif roman == 'V':
        return 5
    elif roman == 'X':
        return 10

