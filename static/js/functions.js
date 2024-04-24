function sendData() { 
	var name = document.getElementById('input1').value;
	var text = document.getElementById('input2').value;
	$.ajax({ 
		url: '/process', 
		type: 'POST', 
		data: {'name': name,
				'text': text }, 
		success: function(response) { 
			document.getElementById('output').innerHTML = response; 
		}, 
		error: function(error) { 
			document.getElementById('output').innerHTML = error; 
		} 
	}); 
} 
function sendDataDelete() { 
	var name = document.getElementById('input1').value;
	var text = document.getElementById('input2').value;
	$.ajax({ 
		url: '/process', 
		type: 'POST', 
		data: {'action': 'delete'}, 
		success: function(response) { 
			document.getElementById('output').innerHTML = response;
			$('#input1,#input2').val('');
		}, 
		error: function(error) { 
			document.getElementById('output').innerHTML = `action failed, ${error}`
		} 
	}); 
} 