from deepmultilingualpunctuation import PunctuationModel

deepmultilingualpunctuation = PunctuationModel()

input_filepath = ('all_lyrics_onlytwo.txt')
output_filepath = ('all_lyrics_onlythree.txt')

def punctuate_file(input_filepath, output_filepath):
    # Load the model (you can specify different models here)
    model = deepmultilingualpunctuation()
    
    # 1. Read the text file
    with open(input_filepath, 'r', encoding='utf-8') as f:
        text = f.read()
        
    # 2. Restore punctuation
    restored_text = model.restore_punctuation(text)
    
    # 3. Write the punctuated text to the output file
    with open(output_filepath, 'w', encoding='utf-8') as f:
        f.write(restored_text)
    
        print("Punctuation restoration complete. Output saved to {output_filepath}")