function onDragStart(event) {
    event
      .dataTransfer
      .setData('text/plain', event.target.id);
    
      event.dataTransfer.effectAllowed = "copy";
  }

function onDragOver(event) {
event.preventDefault();
}

function onDrop(event) {

    // var span = document.createElement('span');
    // span.innerHTML = "<h1>Hi Shimar</h1>"

    // const dropzone = event.target;
    // dropzone.appendChild(span);

    // var span = document.createElement('span');
    // span.innerHTML = "<h1>Hi Shimar</h1>"

    const id = event
    .dataTransfer
    .getData('text');

    //console.log("ID: "+id);

    var date = new Date();
    var id_date = date.getHours()+":"+date.getMinutes()+":"+date.getSeconds();

    var obj = window[id]();
    obj.id = id_date;

    obj.style.height = 'auto';
    obj.style.width = 'auto';
    obj.style.maxHeight = '100%';
    obj.style.maxWidth = '100%';

    // obj.setAttribute("onclick", "ElementSelected("+ obj.id+","+ id +")"); //Here id = Type, this for options
    
    //For Image
    if (id == 'DragImg') {
        obj.setAttribute("onclick", "ElementSelected('"+ obj.id+"','"+ "NBIMAGE_Row" +"')"); //Here id = Type, this for options
    }
    else {
    obj.setAttribute("onclick", "ElementSelected('"+ obj.id+"','"+ id +"')"); //Here id = Type, this for options
    }

    obj.classList.add('Element');
    
    const dropzone = event.target;  
    dropzone.appendChild(obj);

    //Delete Button:Hover
    console.log('Hellooo: '+obj.id)
    // var span = document.createElement('span');
    // span.innerHTML = "<button class='delete' onclick=RemoveSpecificObj('"+ obj.id + "')>Delete</button>"
    // document.getElementById(obj.id).appendChild(span)

  }

function DeleteElement(event) {
    const id = event
    .dataTransfer
    .getData('text/html');

    var myobj = document.getElementById(id);
    myobj.remove();
}

function RemoveSpecificObj(param_id) {
    var myobj = document.getElementById(param_id);
    myobj.remove();
}

//var a ='<button class="delete" onclick="RemoveSpecificObj("'+ param_idOfDroppedElement +'")">Delete</button>'

//var b = "<button class='delete' onclick=RemoveSpecificObj('"+ param_idOfDroppedElement + "')>Delete</button>"



//Dragable Items Function
function yes_form() {
    var div = document.createElement('div');
    div.innerHTML = document.getElementById('yes_form_temp').innerHTML;

    return div;
}
function DragRow(){
//Backup
    // var span = document.createElement('span');
    // span.innerHTML = "<h1>Hi Shimar</h1>";
    //     //console.log('Triggered');
    // return span;

//Second Try
    // var div = document.createElement('div');
    // div.className = 'row'
    // div.innerHTML = "<div class='col'><h1 class='text-center' >Heading</h1></div>"

    var div = document.createElement('div');
    div.classList.add('row');
    div.style.backgroundColor = 'gray';
    div.style.height = 'auto';
    div.style.width = 'auto';
    div.innerHTML = "  Row  ";

    return div;
}

function DragCol(){
    var div = document.createElement('div');
    div.classList.add('col');
    div.innerHTML = "  Column  ";

    return div;
}

function DragImg(){
    var div = document.createElement('img');
    div.src = "https://media.sproutsocial.com/uploads/2017/02/10x-featured-social-media-image-size.png";
    // div.style.height = 'auto';
    // div.style.width = 'auto';
    // div.style.maxHeight = '100%';
    // div.style.maxWidth = '100%';
    return div;
}

function DragH1(){
    var div = document.createElement('H1');
    div.innerHTML = 'Heading';
    div.contentEditable = 'True';

    return div;
}

function DragBtn(){
    var div = document.createElement('Button');
    div.innerHTML = 'Button';

    return div;
}

function Dragparagraph(){
    var div = document.createElement('p');
    div.innerHTML = 'Text';
    div.contentEditable = 'True';

    return div;
}

function DragH2(){
    var div = document.createElement('h2');
    div.innerHTML = 'Heading';
    div.contentEditable = 'True';

    return div;
}

function DragH3(){
    var div = document.createElement('h3');
    div.innerHTML = 'Heading';
    div.contentEditable = 'True';

    return div;
}

function DragH4(){
    var div = document.createElement('h4');
    div.innerHTML = 'Heading';
    div.contentEditable = 'True';

    return div;
}

function DragH4(){
    var div = document.createElement('h4');
    div.innerHTML = 'Heading';
    div.contentEditable = 'True';

    return div;
}

function DragH5(){
    var div = document.createElement('h5');
    div.innerHTML = 'Heading';
    div.contentEditable = 'True';

    return div;
}

function DragH6(){
    var div = document.createElement('h6');
    div.innerHTML = 'Heading';
    div.contentEditable = 'True';

    return div;
}