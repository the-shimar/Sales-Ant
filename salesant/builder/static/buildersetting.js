//Build Save
function BuildSave(ObjId='BuildFrame') {
    console.log('OK Save');
    x = document.getElementById(ObjId).outerHTML;
    // document.getElementById('BName').value = 'new';
    document.getElementById('BuildHtml').value = x;

    document.getElementById('BSaveForm').submit();
}