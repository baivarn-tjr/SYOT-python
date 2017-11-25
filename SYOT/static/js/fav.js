// renderFavList()

function unfav(userid,productid,urlfav){
    // var productid = $(this).attr("product_id");
    // var userid = $(this).attr("user_id")
    console.log("check");
    console.log(productid+'  '+userid);
    $.ajax({
        url : $('#fav-form').attr("fav-url"), // the endpoint
        type : "POST", // http method
        dataType: 'json',
        data : { user_id : userid, product_id : productid }, // data sent with the post request
        // handle a successful response
        success : function(json) {
            console.log("success");
            $('li[product_id='+productid+']').remove();
            // renderFavList()
             // another sanity check
        },
        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log("errrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr");
            // console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });

    // $.post($(this).attr("fav-url"), {user_id: userid , product_id: productid}, function(data) {
    //     if(data.status == 'success'){
    //         console.log("success");
    //         $('#item-in-fav').removeChild($('div[product_id='+productid+']'));
    //     } else{
    //         console.log("error");
    //     }
    // });
}
//
// function renderFavList(){
//     console.log("aaaaaaaaaaa");
//     var url = "{% url 'deletefav'%}"
//     var eventfav = "document.forms['fav-form'].submit(); return false;"
//     // $.each(userFav,function(index, value){
//     userFav.forEach( function(value, index) {
//         console.log(value+'  '+index);
//         var row = '<li>'
//         row += '<div class="col-md-4" align="center">'
//         row += '<div class="product">'
//         row += '<img id="pic3" src="'+value.pictureUrl+'">'
//         row += '<div class="row">'
//         row += '<div class="col-sm-9">'
//         row += '<p>'+value.name+'<br>'+value.cost +'$</p>'
//         row += '</div><form id="fav-form" fav-url='+url+'user_id="'+user.id+'" product_id="'+value.id+'" method="post"> {% csrf_token %}'
//         row += '<div class="col-sm-3">'
//         row += '<a class="nav-link" id="unfav-btn" href="#" onclick='+eventfav+'>'
//         row += '<i id="heart1" class="fa fa-heart" aria-hidden="true"></i></a></div></form></div></div></div></li>'
//         $('#item-in-fav').append(row);
//     })
// }
