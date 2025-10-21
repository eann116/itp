function setup() {
  createCanvas(400, 400);
  noStroke();
}

function drawObject(x, y, s){
   push();
  translate(x, y);
  scale(0.35);
 fill(0);
  rect(40, 10,  70, 5); 
  rect(40, 105,  70, 5);
  rect(40, 10,  5, 100);
  rect(110, 10,  5, 100);
  ellipse(77.5, 40, 30, 30);
 ellipse(77.5, 80, 40, 40);
  pop();
}

function draw(){
  for (x = 0 ; x<=400 ; x+=40) {
      drawObject(x, 0, 1)
  for (y = 0 ; y<=400 ; y+=40){
    drawObject (x, y, 1)
  }
  }
  }