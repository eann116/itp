import pandas as pd

df = pd.read_csv('EdSheeran.csv')

lyrics = df["Lyric"].dropna().astype(str)

output_path = "all_lyrics_only.txt"
with open(output_path, "w" , encoding="utf-8") as f:
    for line in lyrics:
        f.write(line.strip() + "\n\n")
