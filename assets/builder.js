function SizeBuildFrame() {
    var height = document.getElementById('BuildFrameHeight').value;
    var width = document.getElementById('BuildFrameWidth').value;

    document.getElementById('BuildFrame').setAttribute('style', 'height: '+height+'; width: '+width+'; background-color: #ffffff;  max-width: 100%; max-height: inherit;');
}

function BuildFrameSelected(id) {
    document.getElementById('FrameProperties').setAttribute('aria-expanded','true');
}

function ElementSelected(objid, id) {
    var x = document.getElementById('NormalProperties');
} 