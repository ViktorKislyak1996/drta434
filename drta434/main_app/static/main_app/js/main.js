var counter = 1;
function add(){
    var input = document.createElement('input');
    var label = document.createElement('label');

    input.name = 'name' + counter;
    input.type = "text";
    input.id = "name" + counter;
    label.setAttribute("for","name" + counter);
    label.innerHTML = "name" + counter + ":";

    document.getElementById('form-group').appendChild(label);
    document.getElementById('form-group').appendChild(input);

    counter++;
}