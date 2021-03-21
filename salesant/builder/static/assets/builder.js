function SizeBuildFrame() {
    var height = document.getElementById('BuildFrameHeight').value;
    var width = document.getElementById('BuildFrameWidth').value;

    document.getElementById('BuildFrame').setAttribute('style', 'height: '+height+'; width: '+width+'; background-color: #ffffff;  max-width: 100%; max-height: inherit;');
}

function BuildFrameSelected(id) {
    document.getElementById('FrameProperties').setAttribute('aria-expanded','true');
}

//MainFrame Properties
window.MFrameProperties = {};

function ElementSelected(objid, id) {
    var x = document.getElementById('NormalProperties');
    MFrameProperties.id = objid;
    console.log('Clicked'+MFrameProperties.id);
} 

function IBFocusoutImg(id) {
    var x = document.getElementById(id).value;
    MFrame = document.getElementById('BuildFrame');
    MFrame.style.backgroundImage = "url('"+x+"')";
}

function IBFocusoutColor(id) {
    var x = document.getElementById(id).value;
    MFrame = document.getElementById('BuildFrame');
    MFrame.style.backgroundColor  = x;
}

// Normal Box Properties
function NormalBoxHeight(propertyName, currentInput) {
    obj = document.getElementById(MFrameProperties.id);
    // obj.style.window[propertyName] = document.getElementById(currentInput).value;
    obj.style.height =  document.getElementById(currentInput).value;
}

function NormalBoxWidth(propertyName, currentInput) {
    obj = document.getElementById(MFrameProperties.id);
    obj.style.width =  document.getElementById(currentInput).value;
}

//Properties Functions
function pHeight(objectId, InputBoxID) { //objectId = Object in MainFrame. currentInput_Id = value entered in inputbox to change
    obj = document.getElementById(objectId.id);
    obj.style.height =  document.getElementById(InputBoxID).value;
}

function pWidth(objectId, InputBoxID) { //objectId = Object in MainFrame. InputBoxID = value entered in inputbox to change
    obj = document.getElementById(objectId.id);
    obj.style.width =  document.getElementById(InputBoxID).value;
}
//Align Properties
function pTAlign(align) { //objectId = Object in MainFrame. align = "left|right|center|justify|initial|inherit"
    obj = document.getElementById(MFrameProperties.id); //MFrameProperties.id is automatically changes, when obj selected in the mainFrame
    obj.style.textAlign  = align;
}

function pFColor(objectId, InputBoxID) { //objectId = Object in MainFrame. InputBoxID = value entered in inputbox to change
    obj = document.getElementById(objectId.id); //MFrameProperties.id is automatically changes, when obj selected in the mainFrame
    obj.style.color =  document.getElementById(InputBoxID).value;
}

function pBgColor(objectId, InputBoxID) { //objectId = Object in MainFrame. InputBoxID = value entered in inputbox to change
    obj = document.getElementById(objectId.id); //MFrameProperties.id is automatically changes, when obj selected in the mainFrame
    obj.style.backgroundColor =  document.getElementById(InputBoxID).value;
}

//FlexBox
function pFlexAlign(align) { //objectId = Object in MainFrame. align = "stretch|center|flex-start|flex-end|baseline|initial|inherit"
    obj = document.getElementById(MFrameProperties.id); //MFrameProperties.id is automatically changes, when obj selected in the mainFrame
    obj.style.alignItems = align;
}


