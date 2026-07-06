function updateClock(){

let now=new Date();

document.getElementById("clock").innerHTML=

"📅 "+now.toLocaleDateString()+"<br>🕒 "+now.toLocaleTimeString();

document.getElementById("date").innerHTML=

now.toDateString();

}

setInterval(updateClock,1000);

updateClock();

let seconds=60;

setInterval(function(){

seconds--;

document.getElementById("countdown").innerHTML=

seconds+" sec";

if(seconds<=0){

location.reload();

}

},1000);
