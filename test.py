import string

def remove_punctuation(input_string):
    # Create a translation table that maps each punctuation character to None
    translator = str.maketrans('', '', string.punctuation)
    # Use the translate method to apply the translation table
    return input_string.translate(translator)

# Example usage
sentence = "step-brother's workload"
cleaned_sentence = remove_punctuation(sentence)
print(cleaned_sentence)
