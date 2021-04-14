function ynf_build(to_show) {
    document.getElementById('YNFT_first').style.display = 'none';
    document.getElementById('YNFT_second').style.display = 'none';
    document.getElementById('YNFT_third').style.display = 'none';
    document.getElementById('YNFT_fourth').style.display = 'none';
    document.getElementById(to_show).style.display = 'inherit';
}