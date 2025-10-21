#DOCUMENTATION FILE
####Midterm

#####Phase 2
- Drew the border of the speaker image, and played around with the height and width of the image.
- I knew the speaker should be taller than wider, so the width was 70 and the height was 100


`function setup() {
  createCanvas(150, 150);
  noStroke();
}
`
`function draw() {
 fill(0);
  rect(40, 10,  70, 5); 
  rect(40, 105,  70, 5);
  rect(40, 10,  5, 100);
  rect(110, 10,  5, 100);
  ellipse(77.5, 40, 30, 30);
 ellipse(77.5, 80, 40, 40);
}`

- I wanted to make the speaker holes the same shape but different sizes
- The top ellipse is smaller than the bottom one, hence 40 and 80
- the measurements are just what I played around with to make it seem as close to my image as possible

#####Phase 3
I created the function `drawObject` and placed all my code from phase 2 into it.
At first, I thought replacing draw with drawObject would work, but nothing appeared.

Then I copied this into the code
`function draw(){
  drawObject (0, 0, 1)
  drawObject (0, 200, 1)
}`
and the two images of the speaker appeared.
I wrote the rest of the code, including translate and scale, and for the time being used 0.5 as my scale for the image.

#####Phase 4
To create the nested-for loop part of the function, I used what I learned from the fizzBuzz assignment. 
I swapped out i for x and wrote my parameters for x. Knowing that the canvas was 400, I made sure x went up to 400, as well as y later on. Then I had the images move 40 pixels to the right next to each other. I also knew that the width of the speaker image was 70 pixels and the height was 100 pixels, so in order to scale it to a size where both sides will fit in a 40 x 40 pixel cell, I would have to scale it by a factor less than 0.4. I chose 0.35 to be close but not too close. At first I put the x and y nested-for loop in separate bracketed parts of the draw function.

- This resulted in only one line of images on the top horizontal and the left vertical.
After putting the two for loops together, the code produced the entire array of images like planned.

`function draw(){
  for (x = 0 ; x<=400 ; x+=40) {
      drawObject(x, 0, 1)
  for (y = 0 ; y<=400 ; y+=40){
    drawObject (x, y, 1)
  }
  }
  }`

