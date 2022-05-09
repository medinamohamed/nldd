
function preload(){

  screenXY =  loadJSON('../../data/archive/screen/hans_02.json')

}
function setup() {
  
  var canvas = createCanvas(1000, 500);
  canvas.parent('canvasForHTML');

  console.log(screenXY);

  frameRate(0.75);
  

}

function draw() {

  translate(550, 75);

  stroke('#61AA0E'); // Change the color
  strokeWeight(4); // Make the points 10 pixels 

 
  for (let i=1 ; i<screenXY.x.length; i++){
    point(screenXY.x[i], screenXY.y[i])
  }

  
  let shuffleScreenXY = shuffleXY(screenXY.x,screenXY.y)

  line(screenXY.x[frameCount], screenXY.y[frameCount], screenXY.x[frameCount+1], screenXY.y[frameCount+1])



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