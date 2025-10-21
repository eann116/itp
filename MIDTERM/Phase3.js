Creating the function 'drawObject' for code
function setup() {
  createCanvas(400, 400);
  noStroke();
}

function drawObject(x, y, s){
   push();
  translate(x, y);
  scale(0.5);
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
  drawObject (0, 0, 1)
  drawObject (0, 200, 1)
}