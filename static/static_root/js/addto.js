$('#icon-cart-product').on('click',function(event){
    event.preventDefault();
    addtoCart();
});
$('#icon-fav-product').on('click',function(event){
    event.preventDefault();
    addtoFav();
});


function addtoCart() {
    if($('#cart-form').attr("user_id") == '' || !$('#cart-form').attr("user_id")){
        alert('please log in');
    }
    else{
        console.log($('#cart-form').attr("cart-url"));
        $.ajax({
            url : $('#cart-form').attr("cart-url"), // the endpoint
            type : "POST", // http method
            dataType: 'json',
            data : { user_id : $('#cart-form').attr("user_id"), product_id : $('#cart-form').attr("product_id") }, // data sent with the post request
            // handle a successful response
            success : function(json) {
                console.log("success"); // another sanity check
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                console.log("errrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr");
                // console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }
};

function addtoFav() {
    if($('#cart-form').attr("user_id") == '' || !$('#cart-form').attr("user_id")){
        alert('please log in');
    }
    else{
        console.log($('#fav-form').attr("fav-url"));
        $.ajax({
            url : $('#fav-form').attr("fav-url"), // the endpoint
            type : "POST", // http method
            dataType: 'json',
            data : { user_id : $('#fav-form').attr("user_id"), product_id : $('#fav-form').attr("product_id") }, // data sent with the post request
            // handle a successful response
            success : function(json) {
                console.log("success"); // another sanity check
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                console.log("errrrrrrrfffffffffffffffffffffffffffffffffffffffffff");
                // console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }
};
// using jQuery
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
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
