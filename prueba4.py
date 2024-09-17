def test_roman_to_int_II():
    assert roman_to_int('II') == 2


def roman_to_int(roman):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10
    }

    total = 0
    for char in roman:
        total += roman_numerals[char]
    return total
