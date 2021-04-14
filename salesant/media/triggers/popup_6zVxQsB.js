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

//YNF
console.log('YES')
function ynf_yes_fnc() {
  console.log('YES Function')
  document.getElementById('YNFT_first').style.display = 'none';
  document.getElementById('YNFT_second').style.display = 'inherit';
}

function ynf_no_fnc() {
  document.getElementById('YNFT_first').style.display = 'none';
  document.getElementById('YNFT_fourth').style.display = 'inherit';
}

function ynf_emailsubmit_fnc() {
  document.getElementById('YNFT_second').style.display = 'none';
  document.getElementById('YNFT_third').style.display = 'inherit';
}

//To not reload page while submiting form in ynf
// var form = document.getElementById("YNF_Form_SalesAnt");
// function handleForm(event) { event.preventDefault(); } 
// form.addEventListener('submit', handleForm);

// $(document).ready(function () {
//   // Listen to click event on the submit button
//   $('#button').click(function (e) {

//     e.preventDefault();

//     var name = $("#name").val();
//     var email = $("#email").val();

//     $.post("process.php", {
//       name: name,
//       email: email
//     }).complete(function() {
//         console.log("Success");
//       });
//   });
// });


$(document).ready(function () {
  // Listen to click event on the submit button
  $('#2nd_emailbutton').click(function (e) {

    e.preventDefault();

    var s_v = $("#s_v").val();
    var u_y = $("#u_y").val();
    var ng = $("#ng").val();
    var c_e = $("#2nd_emailinput").val();

    console.log('HEHE');
    $.post("http://127.0.0.1:8000/dc/fny_f", {
      s_v: s_v,
      u_y: u_y,
      ng: ng,
      c_e: c_e
    }).complete(function() {
        console.log("Success");
      });
  });
});