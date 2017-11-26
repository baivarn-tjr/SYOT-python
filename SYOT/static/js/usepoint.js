checkpoint();

function checkpoint(){
    pointhad = Number($('#total-point').attr('point-value'));
    if(pointhad < 1500){
        $('#use-point').attr("disabled", "disabled");
    } else{
        console.log("much");
    }
}

$('#use-point').on('click',function(event){
    pointhad = Number($('#total-point').attr('point-value'));
    money = Number($('#total-money').attr('money-value'));
    if(pointhad >= 1500 && pointhad < 7000){
        pointhad -= 1500;
        money -= 1;
    } else if(pointhad >= 7000 && pointhad < 25000){
        pointhad -= 7000;
        money -= 10;
    } else{
        pointhad -= 250000;
        money -= 50;
    }
    if(money <= 0){
        money = 0
    }
    console.log("money "+money);
    console.log("pointhad "+pointhad);
    $.ajax({
        url : $('#use-point-div').attr("url-point"), // the endpoint
        type : "POST", // http method
        dataType: 'json',
        data : { pointuse : pointhad }, // data sent with the post request
        // handle a successful response
        success : function(json) {
            console.log("success"); // another sanity check
            $('#use-point').attr("disabled", "disabled");
            $('#total-point').text(pointhad)
            $('#total-money').text(money)
            checkmoney();

        },
        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log("errrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr");
            // console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
});

function checkmoney(){
    console.log("checkk");
    console.log($('#total-money').text());
    if($('#total-money').text() == '0'){
        console.log("checkkkkkkkk");
        window.location = $('#payment-point').attr("payment-url");
        // $.ajax({
        //     url : $('#payment-form').attr("payment-url"), // the endpoint
        //     type : "POST", // http method
        //     dataType: 'json',
        //     data : { },
        //     success : function(json) {
        //         console.log("test");
        //     },
        //     error : function(xhr,errmsg,err) {
        //     }
        // });
    }
}
