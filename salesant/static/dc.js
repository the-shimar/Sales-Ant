function TriggerNameClk_mu(value) {
    document.getElementById('mu_btn').innerHTML = value;
    document.getElementById('mu_triggers').value = value; //Form
}

console.log('DC')

function TriggerNameClk_subscribers(value) {
    document.getElementById('ss_button').innerHTML = value;
    document.getElementById('ss_triggers').value = value; //Form
}

function selected_website(value) {
    document.getElementById('selected_website').innerHTML = value;
    document.getElementById('mu_website').value = value; //Form
    document.getElementById('ss_website').value = value; //Form
}