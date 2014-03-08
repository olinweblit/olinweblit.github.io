$(document).ready(function(){

	// Main Firebase, here for reference
	var ref = new Firebase("https://olinweblit.firebaseio.com/users");
	var myUser = -1;
	
	//AJAX auth
	var authClient = new FirebaseSimpleLogin(ref, function (error, user) {
		if (error) {
		    alert(error);
		    return;
		}
		if (user) {
			//Display logout
			$("#login").css("display", "none");
			$("#settings").css("display", "inline-block");
			$("#logout").css("display", "inline-block");
			
		    // User is already logged in
		    myUser = user;
		    updatePage(user.name);
		    console.log('logged in: ' + user.name);
		    		    
		} else {
		    // User is logged out.
		    
		    //Display logout
		    $("#settings").css("display", "none");
			$("#logout").css("display", "none");
			$("#login").css("display", "inline-block");
		    
		    console.log('logged out');
	    }
	});
	
	//Main login function for facebook
	function loginFacebook() {
	    authClient.login('facebook', {
		  rememberMe: true,
		  scope: 'basic_info'
		});
	};
	//Logout
	function logoutFacebook(){
		authClient.logout();
	};	
	//Login button
	$("#login").click(function(){
		loginFacebook();
	});
	//Logout button
	$("#logout").click(function(){
		logoutFacebook();
	});
	$("#settings").click(function(){
		var disp = $('#settings-box').css('display');
		if (disp == 'none'){
			$("#settings-box").css("display", "block");
		}
		else {
			$("#settings-box").css("display", "none");
		}
	});
	
	//Update page based on log in stuff
	function updatePage(){
		$("#myname").html(myUser.name);
		
		if (myUser){
			var myRef = new Firebase("https://olinweblit.firebaseio.com/users/" + myUser.id + "/aboutme");
			myRef.on('value', function(snapshot) {
				var snap = snapshot.val();
				
				$('#myabout').html(snap);
			
			});
		}
	};
	
	
	//Update about
	$("#editabout").click(function(){
		if (myUser){
			var myRef = new Firebase("https://olinweblit.firebaseio.com/users/" + myUser.id + "/aboutme")
				, about = $("#myabouttext").val();
			myRef.set(about);
		}
	});
	
});