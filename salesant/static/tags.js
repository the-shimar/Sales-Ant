function TriggerNameClk(value) {
    document.getElementById('TriggerNamebtn').innerText = value;
    document.getElementById('TriggerNameField').value = value; //Form
}

function ApiKeyClk(value) {
    document.getElementById('ApiKeybtn').innerText = value;
    document.getElementById('ApiKeyField').value = value; //Form
}

function TagGenerate() {
    document.getElementById('TagGenerateForm').submit(); 
}

function DeleteCode(triggername) {
    document.getElementById('CodeDeleteValue').value = triggername;
    document.getElementById('CodeDeleteForm').submit(); 
}
