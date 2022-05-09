const menuBtn = document.querySelector('.menu-btn');
let menuOpen = false;
const div = document.getElementById('classe');
div.classList.add("to-hide");

menuBtn.addEventListener('click', ()=> {
    if(!menuOpen){
        div.classList.add("to-hide");
        menuBtn.classList.remove('open');
        
        menuOpen = true;
    } else{
        div.classList.remove('to-hide');

        menuBtn.classList.add('open');
        menuOpen = false;
    }
});


// //const button = document.getElementById('button'); // or classname, whatever. it is your link or any node element instead of it. 
//   const div = document.getElementById('classe');

//   function toggleDiv(e) {
//     // e - event object - {button}.
//     e.preventDefault(); // only if you use <a> as node.
//     if(!menuOpen){
//         div.classList.add("to-hide");
//         menuOpen = true;
//     } else{
//         div.classList.remove('to-hide');
//         menuOpen = false;
//     }
//     //div.classList.add("to-hide");
//   }

//   menuBtn.addEventListener('click', toggleDiv, false);