// Adding and removing items from cart
$(document).ready(function () {

var cartItems = []

window.onload = function () {
	if (cartItems.length < 1) {
		$('#cart').append("<strong class='text-muted'>You have not added anything to cart</strong><br>");
	}
	document.getElementById("track-product-button").onclick = function fun() {
		if (document.getElementById('product').value != "") {
			var item = document.getElementById('product').value;
			cartItems.push(item);
			count = cartItems.length - 1;
			if (cartItems.length == 1) {
				$('#cart').html('')
			}
			$('#cart').append("<div class='justahack-" + cartItems[count] + "' id='newCartItem'>📌 " + cartItems[count] + "<b id='remove'>❌</b></div>");
		}


		// FIXME Removes the wrong item
	}
	$('#cart').on('click', '#remove', function () {
		console.log(cartItems)
		itemToRemove = $('#newCartItem').attr('class');
		toRemove = itemToRemove.split('justahack-')[1];
		cartItems = cartItems.filter(item => item !== toRemove)
		$('#newCartItem').remove();
		console.log(cartItems)
	});
}

  
    // REVIEW: Changed make ajax POST on checkout button to be revisited
		
		// Sending item to view using ajax
    $('#checkout').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        create_post();
    });
    
    // AJAX for posting
    function create_post() {
				console.log(JSON.stringify(cartItems))
				console.log("create post is working!") // sanity check
			clientPhone = ($('#clientphone').val());

        $.ajax({
            url : "/ajax", // the endpoint
            type : "POST", // http method
					data: { 'phone': clientPhone, 'trackedItem': JSON.stringify(cartItems)}, // data sent with the post request
            // handle a successful response
            success : function(json) {
                $('#product').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                var emptystr = ''
                $("#notfound").replaceWith(emptystr)
                $("#show").prepend("<strong id='newCartItem'>👉  "+json.item+" <b id='remove'>❌</b></strong><br>");
                console.log("success"); // another sanity check
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };
    
    
    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    
    /*
    The functions below will create a header with csrftoken
    */
    
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});