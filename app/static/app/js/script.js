
const bar = document.getElementById('bar');
const nav = document.getElementById('navbar');


if(bar.onclick){
}


function showNav(){
    nav.style.right=0;

}

function closeNav(){
    console.log('closed')
    nav.style.right ='-310px'
}