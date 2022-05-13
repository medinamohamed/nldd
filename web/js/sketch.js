let doubleScreenX = [];
let doubleScreenY = [];

let n = 2;
function preload(){

  screenXY =  loadJSON('../data/archive/screen/mylene.json')

}
function setup() {
  
  var canvas = createCanvas(windowWidth, windowHeight);
  canvas.parent('canvasForHTML');

  console.log(screenXY);

  frameRate(1);

  console.log(screenXY.x.length)
 
  for (let i=0 ; i<screenXY.x.length; i++){
    doubleScreenX.push(screenXY.x[i]*n)
  }

 
  for (let i=0 ; i<screenXY.x.length; i++){
    doubleScreenY.push(screenXY.y[i]*n)
  }

}

function draw() {
  translate(350, 0);

  stroke('#61AA0E'); // Change the color
  strokeWeight(4); // Make the points 10 pixels 


  for (let i=1 ; i<screenXY.y.length; i++){
    point(doubleScreenX[i], doubleScreenY[i])
  }
  
  line(doubleScreenX[frameCount], doubleScreenY[frameCount], doubleScreenX[frameCount+1], doubleScreenY[frameCount+1])
  // let shuffleScreenXY = shuffleXY(screenXY.x,screenXY.y)

}

function mousePressed() {
  redraw();
}

function shuffleXY(arrayX, arrayY) {
  var copyX = [], copyY = [], n = arrayX.length, i;

  // While there remain elements to shuffle…
  while (n) {

    // Pick a remaining element…
    i = Math.floor(Math.random() * arrayX.length);

    // If not already shuffled, move it to the new array.
    if (i in arrayX) {
      copyX.push(arrayX[i]);
      //delete arrayX[i];

      copyY.push(arrayY[i]);
      //delete arrayY[i];
      n--;
    }
  }

  return {x: copyX, y:copyY};
}