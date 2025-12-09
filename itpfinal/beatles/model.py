import markovify
 
def load_lyrics(corpus_path):
    with open(corpus_path, 'r', encoding='utf-8') as f:
        return f.read().split('\n')
    
def generate_lyrics(corpus_path, genre, num_lines):
    lyrics = load_lyrics(corpus_path)

    corpus_text = "\n".join(lyrics)

    if not corpus_text or len(corpus_text.split()) < 2:
        print("ERROR: corpus_text is empty or too short. Check your input file.")
        return None

    text_model = markovify.Text(corpus_text, state_size=2)

    generated_lines = []
    for _ in range(num_lines):
        line = text_model.make_sentence(tries=100)
        if line:
            generated_lines.append(line)

    title = f"Generated {genre} Lyrics"
    lyrics_str = "\n".join(generated_lines)
    return f"{title}\n\n{lyrics_str}"

corpus_path = 'all_lyrics_onlytwo.txt'
genre = 'pop' 
num_lines = 20  

result = generate_lyrics(corpus_path, genre, num_lines)
print(result)

from gtts import gTTS
import os

text_to_speak = (result)
tts = gTTS(text=text_to_speak, lang='en')
tts.save("lyricsbyeann.mp3")

