
function preload(){

  screenXY =  loadJSON('../data/screen/mylene.json')

}
function setup() {
  
  createCanvas(1000,500);

  console.log(screenXY);

  frameRate(0.75);

  console.log(shuffleXY(screenXY.x,screenXY.y));

  

}

function draw() {

  translate(300, 75);


  stroke('#61AA0E'); // Change the color
  strokeWeight(4); // Make the points 10 pixels 

 
  for (let i=0 ; i<screenXY.x.length; i++){
    point(screenXY.x[i], screenXY.y[i])
  }

  
  let shuffleScreenXY = shuffleXY(screenXY.x,screenXY.y)



  // push()
  // for (let i=1 ; i<(screenXY.x.length-1)/2; i++){
  //   strokeWeight(4);
  //   //line(shuffleScreenXY.x[i], shuffleScreenXY.y[i], shuffleScreenXY.x[i+1], shuffleScreenXY.y[i+1])
  //   line(screenXY.x[i], screenXY.y[i], screenXY.x[i+1], screenXY.y[i+1])
    
  // }
  // pop()
  // // console.log("frameCount",frameCount)

  line(screenXY.x[frameCount], screenXY.y[frameCount], screenXY.x[frameCount+1], screenXY.y[frameCount+1])



  // push()


  // for (let i=0 ; i<screenXY.x.length-1; i++){
  //   strokeWeight(4);
  //   //line(screenXY.x[frameCount], screenXY.y[frameCount], screenXY.x[frameCount+1], screenXY.y[frameCount+1]

  //   //line(shuffleScreenXY.x[i], shuffleScreenXY.y[i], shuffleScreenXY.x[i+1], shuffleScreenXY.y[i+1])
  //   //line(screenXY.x[i], screenXY.y[i], screenXY.x[i+1], screenXY.y[i+1])
    
  // }
  // pop()
  

  // for (let i=0 ; i<screenXY.x.length-1; i++){
  //   line(shuffleScreenXY.x[i], shuffleScreenXY.y[i], shuffleScreenXY.x[i+1], shuffleScreenXY.y[i+1])
  // }


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