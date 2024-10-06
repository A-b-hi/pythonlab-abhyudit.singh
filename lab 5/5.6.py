sequence = "Programming"

def process_char(char):
    return (char.upper(), char.lower())

unique_chars = set(sequence)

result = list(map(process_char, unique_chars))

print(result)