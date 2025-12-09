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

![alt text](https://github.com/eann116/itp/blob/main/itpfinal/beatles/Screenshot%202025-11-25%20at%2012.55.46%E2%80%AFAM.png)

Here is where the biggest issues occured. The markov chain needs to understand where sentences begin and where sentences end inside of the file, regardless whether it was a csv or a txt file. In simple terms, I needed punctuation and indents in my .txt file, something it did not have.

I tried a variety of python functions here to fix this issue, `deepmultilingualpunctuator` or `punctuator` to name two. However they both ended up not working, and in all honesty, for reasons I could not even get an understanding of.

##### SOLUTION
I took another approach, going to https://genius.com and taking lyrics from their database, and putting them in one by one myself. The code works!

Here is the code!
![alt text](https://github.com/eann116/itp/blob/main/itpfinal/beatles/Screenshot%202025-12-08%20at%202.41.34%E2%80%AFPM.png)


### Step 2: Make a GUI for the lyric generation code
I wanted to create a little interface where you can generate and hear the lyrics that were created. The interface would have a button to generate the lyrics, and then a button to listen to it once it is created. I tried using the built in `tkinter,` however I would keep getting the error of the module tkinter not existing. I realized it was because the tkinter runs on the version 3.14.2 of python, while all of my other code was running on python 3.11.4. Instead, I used a python installation called `pyqt6` to create buttons and create audio files for my lyrics. The code is in the gui.py file.

I couldn't figure out how to utilize the buttons, as many times the buttons ended up not producing anything. After failing many times, I made the bold guess as to take my entire model.py code and put it into the pyqt6 code I had. That way, the buttons ended up running the code for me. Boom!





##### Credits
- My friend Chris Miyai, a computer science major from Boston University
- Google Gemini for troubleshooting
	- Biggest takeaways from using AI was being able to see what was missing from my code, as well as creating error message prints. For example, if you don't generate the lyrics before hitting the listen button, Gemini suggested a print function to produce the message "Error: Audio file '{audio_file}' not found. Generate lyrics first."
- Other research articles




