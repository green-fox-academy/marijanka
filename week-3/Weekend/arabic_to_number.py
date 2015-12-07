roman_numerals = (
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
)

def encode(n):
    if n > 0 and n < 4000:
        encoded = ""
        for symbol, value in roman_numerals:
            while n >= value:
                encoded += symbol
                n -= value
        return encoded
    else:
        return "Please type other number."
