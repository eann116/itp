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


![Alt text](Screenshot 2025-11-25 at 12.55.46 AM)