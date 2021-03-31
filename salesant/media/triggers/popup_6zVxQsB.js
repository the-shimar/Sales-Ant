var modal = document.getElementById("PopUp-SalesAnt");

function onStart(){
    console.log('PopUp-SalesAnt');
    modal.style.display = "block";
}

// onStart();
setTimeout(onStart, 5000);

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}