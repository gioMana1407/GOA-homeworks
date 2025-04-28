let p = document.querySelector("p")
p.style.color = "green"

let parentDiv = document.createElement('div');


parentDiv.style.display = 'flex';
parentDiv.style.flexDirection = 'row';
parentDiv.style.justifyContent = 'space-between';
parentDiv.style.width = '500px';
parentDiv.style.height = '250px';
parentDiv.style.margin = '50px auto';
parentDiv.style.border = '2px solid black';
parentDiv.style.padding = '10px';
parentDiv.style.boxSizing = 'border-box';

let redDiv = document.createElement('div');
redDiv.style.backgroundColor = 'red';
redDiv.style.width = '150px';
redDiv.style.height = '100%';
redDiv.style.borderRadius = '10px';

let greenDiv = document.createElement('div');
greenDiv.style.backgroundColor = 'green';
greenDiv.style.width = '150px';
greenDiv.style.height = '100%';
greenDiv.style.borderRadius = '10px';

parentDiv.appendChild(redDiv);
parentDiv.appendChild(greenDiv);

document.body.appendChild(parentDiv);

