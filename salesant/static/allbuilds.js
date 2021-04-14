function BuildDelete(buildName) {
    document.getElementById('BuildName_del').value = buildName;
    console.log('buildname: '+document.getElementById("BuildName_del").value )
    document.getElementById('BuildDelete').submit();
}

function BuildFrameEdit(buildName) {
    document.getElementById('form_buildName_navigator').value = buildName;
    document.getElementById('BuildFrameEdit').submit();
}