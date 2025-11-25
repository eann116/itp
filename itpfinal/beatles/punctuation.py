from punctuator import Punctuator

# Load the model
p = Punctuator()

# Open the input file and read its content
with open('all_lyrics_onlytwo.txt', 'r') as infile:
    text = infile.read()

# Add punctuation to the text
punctuated_text = p.punctuate(text)

# Write the result to a new file
with open('all_lyrics_onlythree.txt', 'w') as outfile:
    outfile.write(punctuated_text)
