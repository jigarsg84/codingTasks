# alternative.py

def alternate_case_char(string):
    result = ''
    for i, char in enumerate(string):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

def alternate_case_words(string):
    words = string.split()
    result = ''
    for i, word in enumerate(words):
        if i % 2 != 0:
            result += word.lower()
        else:
            result += word.upper()
        result += ' '  # Add space between words
    return result[:-1]  # Remove trailing space

# Test alternate_case_characters function
input_string = input("Enter a string: ")        # I am studying Data Science
result_output = alternate_case_char(input_string)
print("Alternate case characters:", result_output)      # I Am sTuDyInG DaTa sCiEnCe.

# Test alternate_case_words function
input_string = input("Enter a string: ")
result_words = alternate_case_words(input_string)
print("Alternate case words:", result_words)
