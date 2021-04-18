function Save(ObjId) {
    console.log('OK Save');
    x = document.getElementById(ObjId).outerHTML;
    console.log(x);
    document.getElementById('BName').value = 'new';
    document.getElementById('BHtml').value = x;
    document.getElementById('BUser').value = 'admin';

    document.getElementById('BSaveForm').submit();
}