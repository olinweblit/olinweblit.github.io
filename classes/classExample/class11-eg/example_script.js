$(document).ready(function(){

	// Main Firebase, here for reference
	var ref = new Firebase("https://olinweblit.firebaseio.com");
	
	//Send stuff to Firebase
	$("#button").click(function(){
		var name = $("#myname").val()
			, to = $("#messto").val()
			, text = $("#mytext").val()
			, time = Date.now()
			, nuRef = new Firebase("https://olinweblit.firebaseio.com/" + to);
			
		nuRef.set({
			"time": time,
			"from": name,
			"text": text
		});
		
		$("textarea").val("");
	});
	
	
	//Function to update
	function pullData(name){
		if (name){
			var myRef = new Firebase("https://olinweblit.firebaseio.com/" + name);
			myRef.on('value', function(snapshot) {
				var snap = snapshot.val()	//Returns array
					, timestamp = new Date(snap.time);
					
				$('#chat-block').html('<div class="inbox"><h3>' + snap.from + '--' + timestamp + '</h3><p>' + snap.text + '</p></div>');
				
			});
		}
	}
	
	setInterval(function(){
		var name = $("#myname").val();
		pullData(name);
	}, 1000);
});