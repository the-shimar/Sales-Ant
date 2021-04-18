//Modal
function triggerValue(value){
    document.getElementById('TriggerValueInput').value = value;
}
function buildValue(value){
    document.getElementById('BuildValueInput').value = value;
}


//Triggers Save
function SaveTrigger() {
    console.log('OK Save');
    document.getElementById('TriggerSaveForm').submit();
}

function DeleteTrigger() {
    document.getElementById('TriggerDelete').submit();
}
