#Fahrenheit to Celcius 
####Notes
- First attempt, made the equation log and the fahrenheit const
- Once I ran code, it worked, so then I worked on the specifics
- Identified the two degrees and identified celcius
- Tried to use console.log(celcius.toFixed(0)); to make celcius a no decimal number, failed
- Put toFixed in console.log equation for celcius instead, it worked
- I kept trying to do things to identify celcius but nothing worked

- I could not figure it out, so I texted and facetimed my friend Analeah from Cornell. She helped me figure out how to identify celcius using a function, now I have two parts. One of the basic code to calculate celsius, and the second part of code to identify and store celcius with a RESUSABLE function. Thank you Analeah!
- I also added parseInt in this function to convert floating point to an integer

`const fahrenheit = 70;`

`console.log (((fahrenheit - 32)*(5/9)).toFixed(0));`

`function fahrenheitToCelsius(fahrenheit){return parseInt((fahrenheit - 32)*(5/9))};`
`let celcius = fahrenheitToCelsius(fahrenheit);`

`console.log(celcius)`

21
21
