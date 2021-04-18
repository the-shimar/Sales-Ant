//MainFrame Properties
window.TempMFrameProperties = {};

function TempElementSelected(objid, id) {
    var x = document.getElementById('TemplateProperties');
    TempMFrameProperties.id = objid;
    console.log('TClicked'+TempMFrameProperties.id);

} 

// Template Box Properties
function TemplateBoxFontSize(currentInput) {
    obj = document.getElementById(MFrameProperties.id);
    obj.style.fontSize  =  document.getElementById(currentInput).value;
}

function TemplateBoxFontColor(currentInput) {
    obj = document.getElementById(TempMFrameProperties.id);
    obj.style.color =  document.getElementById(currentInput).value;
}

function TemplateBoxBGColor(currentInput) {
    console.log("BG Color: "+currentInput);
    obj = document.getElementById(TempMFrameProperties.id);
    obj.style.backgroundColor =  document.getElementById(currentInput).value;
}

function TemplateBoxHeight(propertyName, currentInput) {
    obj = document.getElementById(TempMFrameProperties.id);
    // obj.style.window[propertyName] = document.getElementById(currentInput).value;
    obj.style.height =  document.getElementById(currentInput).value;
}

function TemplateBoxWidth(propertyName, currentInput) {
    obj = document.getElementById(TempMFrameProperties.id);
    obj.style.width =  document.getElementById(currentInput).value;
}



//Align Properties
function tpTAlign(align) { //objectId = Object in MainFrame. align = "left|right|center|justify|initial|inherit"
    obj = document.getElementById(TempMFrameProperties.id); //TempMFrameProperties.id is automatically changes, when obj selected in the mainFrame
    obj.style.textAlign  = align;
}

function pFColor(objectId, InputBoxID) { //objectId = Object in MainFrame. InputBoxID = value entered in inputbox to change
    obj = document.getElementById(objectId.id); //TempMFrameProperties.id is automatically changes, when obj selected in the mainFrame
    obj.style.color =  document.getElementById(InputBoxID).value;
}

function pBgColor(objectId, InputBoxID) { //objectId = Object in MainFrame. InputBoxID = value entered in inputbox to change
    obj = document.getElementById(objectId.id); //TempMFrameProperties.id is automatically changes, when obj selected in the mainFrame
    obj.style.backgroundColor =  document.getElementById(InputBoxID).value;
}

function TemplatespDelete(){
    obj = document.getElementById(TempMFrameProperties.id); //TempMFrameProperties.id is automatically changes, when obj selected in the mainFrame
    document.getElementById(obj.id).remove();
}