function dumptodatabase(payload){
	var req = return jQuery.ajax({
        url: "https://blinding-inferno-9101.firebaseio.com/bro.json",
        type: PUT,
        data: payload,
        success: function(){
        	console.print(req.content);
        }
    });
};