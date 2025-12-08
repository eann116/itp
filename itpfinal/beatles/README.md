# Lyric Generation Machine

As a final project, I thought to create a machine learning system that can generate lyrics based off datasets.
Here are the steps I took, many failed, to get there.

### First Idea
Though, as you will see, this ended to be a very complicated and confusing method for an amateur coder, and ultimately will get scrapped.
Taylor Swift Generation using .csv file and training. My brief understanding of this is that the code reads the csv file, and continuosly trains itself to formulate entirely new lyrics for you.

Some vocabulary:
*tokenization* : Taking pieces of code and turning them in tokens

In this one, I would install an engine called pyenv (using Homebrew), and run a lyric generation function.
`pip3 install Homebrew`
`pip3 install pyenv`
`pyenv install lyric generation`

I came through small problems like being in the right `pwd` or installing into the right sections, but for the most party this was the easiest part.


### Second Idea: Markov Chain Model
With a suggestion from my friend Chris, he said that the Markov Model would prove to be a lot easier with similar results. In this scenario, we use the Markov model to predict the next words in dataset, which creates essentially a new line of lyrics.

The BIGGER the dataset, the more variety of lyrics there can be.

Here is where the biggest errors occurred.

#### .csv file into .txt file into *neither*
In order to transition from the Taylor Swift model to the Markov Chain Model, the code uses a `corpus_text` file, a .txt file instead of a .csv file. The code takes out solely the text/lyric portions of the csv file, as the rest is not needed.

![alt text](Screenshot%202025-11-25%20at%2012.55.28 AM.png)

Here is where the biggest issues occured. The markov chain needs to understand where sentences begin and where sentences end inside of the file, regardless whether it was a csv or a txt file. In simple terms, I needed punctuation and indents in my .txt file, something it did not have.

I tried a variety of python functions here to fix this issue, `deepmultilingualpunctuator` or `punctuator` to name two. However they both ended up not working, and in all honesty, for reasons I could not even get an understanding of.

##### SOLUTION
I took another approach, going to https://genius.com and taking lyrics from their database, and putting them in one by one myself. The code works!

