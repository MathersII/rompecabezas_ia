const socket = io();


var espacio_solucion = document.getElementById('espacio-solucion');
var conseguir_solucion = document.getElementById('conseguir-ruta');


conseguir_solucion.addEventListener('click', function(){

	var posiciones = [];
	var arg=""

	posiciones[0] = document.getElementById('pos-1').value;
	posiciones[1] = document.getElementById('pos-2').value;
	posiciones[2] = document.getElementById('pos-3').value;
	posiciones[3] = document.getElementById('pos-4').value;
	posiciones[4] = document.getElementById('pos-5').value;
	posiciones[5] = document.getElementById('pos-6').value;
	posiciones[6] = document.getElementById('pos-7').value;
	posiciones[7] = document.getElementById('pos-8').value;
	posiciones[8] = document.getElementById('pos-9').value;

	console.log(posiciones);

	posiciones.forEach(function(element) {
		arg = arg+element;
	});

	arg = arg + " 123456780";
	console.log(arg);

	socket.emit('request', arg);

});

socket.on('response', function(message){
	console.log("Desde python: "+message);
	ruta = message.split(" ");
	var contador = 0;
	ruta.forEach(function(element){
		contador = contador + 1;

		var box = document.createElement("DIV");
		box.classList.add('box');

		items = element.split(",")

		items.forEach(function(i){
			var item = document.createElement("DIV");
			item.classList.add('item');
			var text = document.createElement("P");
			text.innerHTML = i;

			item.appendChild(text);
			box.appendChild(item);
		});

		if (contador < ruta.length){
			espacio_solucion.appendChild(box);
		}
	})
});