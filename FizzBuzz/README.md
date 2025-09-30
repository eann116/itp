#FizzBuzz Homework

####First Step
- I wrote the code for a list of numbers 1-100

`for (let i = 0; i <= 100; i += 1) {`
  `console.log(`${i}`);`
  `}`
  
- Now I had to figure out how to single out the multiples for 3 and 5
I used the line:

`for (let i = 0; i <= 100; i++) {
  if (i % 3 === 0) {
    console.log("fizz");
    }`
	
- I then repeated the code for numbers divisible by 5 and then numbers divisible both by 3 and 5
- Although this worked, it did not replace the multiples of 3 and 5, but rather put them all at the end
- I then put in an `else` function to try to get rid of the excess numbers
- it worked for the multiples of 3, but not the others

I put in the code `if (i=0); {console.log ("");}` to try to get rid of the words in the beginning
Eloquent JavaScript Crashed.

####Second Try
To solve the problem of having the excess words in the beginning, I changed i to = 1 instead to change the range.

My code now is 
`for (let i = 1; i <= 100; i+=1) {
  if (i % 3 === 0) {
    console.log("fizz");
    }
  if (i % 5 === 0) {
    console.log ("buzz");
    } 
  if (i % 3 === 0 && i % 5 === 0) {
    console.log ("fizzBuzz"); 
    }
  else {
    console.log(`${i}`);
    }
}`

PROBLEMS: The numbers where fizz and buzz and fizzBuzz are are still there, and when there are multiples of 3 and 5, all words are present.

