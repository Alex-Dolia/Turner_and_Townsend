def Roman_Numerals(Roman_Numbers):
    mapping = {"I": 1,
               "V": 5,
               "X": 10,
               "C": 100,
               "M": 1000
              }
    #
    number = 0
    #
    if len(Roman_Numbers.strip()) == 0:
       raise ValueError("Roman number is empty string") 
    #
    for letter in Roman_Numbers:
        if letter in mapping:
           number += mapping[letter]
        else:
           raise ValueError("All symbols should be from the list ['I', 'V', 'X', 'C', 'M']")   
    #
    return number