function onDeploy() {
    console.log('ONDeploy')
   document.getElementById('BuildFrame').onclick = '';
   document.getElementById('BuildFrame').ondragover = '';
   document.getElementById('BuildFrame').ondrop = '';
   
   document.getElementsByClassName('delete').remove();

}

onDeploy();