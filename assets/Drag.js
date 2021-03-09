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
    // obj.setAttribute("onclick", "ElementSelected("+ obj.id+","+ id +")"); //Here id = Type, this for options
    obj.setAttribute("onclick", "ElementSelected('"+ obj.id+"','"+ id +"')"); //Here id = Type, this for options
    obj.classList.add('Element');
    
    const dropzone = event.target;  
    dropzone.appendChild(obj);

    //Delete Button:Hover
    console.log('Hellooo: '+obj.id)
    var span = document.createElement('span');
    span.innerHTML = "<button class='delete' onclick=RemoveSpecificObj('"+ obj.id + "')>Delete</button>"
    document.getElementById(obj.id).appendChild(span)

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

    return div;
}

function DragH1(){
    var div = document.createElement('H1');
    div.innerHTML = 'Heading';

    return div;
}

function DragBtn(){
    var div = document.createElement('Button');
    div.innerHTML = 'Button';

    return div;
}