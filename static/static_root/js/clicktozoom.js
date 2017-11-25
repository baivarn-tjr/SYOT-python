// Get the modal
var modal1 = $('#myModalimg');
// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = $('#front-model');
var subImg1 = $('#sub-model-1');
var subImg2 = $('#sub-model-2');
var subImg3 = $('#sub-model-3');
var subImg4 = $('#sub-model-4');
var modalImg = $("#img01");
var captionText = $("#caption");
var closebtn = $('#closebtn');
$(document).click(function (e) {
if ($(e.target).is('#img01')) {
    modal1.style.display = "none";
}
if($(e.target).is('#myModal')){
    modal1.style.display = "none";
}
});
closebtn.on("click", function() {
    console.log("test");
    modal1.addClass("hide");
});
img.on("click", function() {
    console.log("test2");
    modal1.removeClass("hide");
    // modal.style.display = "block";
    modalImg.attr('src',$(this).attr('src'))
    // modalImg.src = this.src;
    captionText.innerHTML = this.alt;
});
subImg1.on("click", function() {
    modal1.removeClass("hide");
    // modal.style.display = "block";
    modalImg.attr('src',$(this).attr('src'))
    // modalImg.src = this.src;
    captionText.innerHTML = this.alt;
});
subImg2.on("click", function() {
    modal1.removeClass("hide");
    // modal.style.display = "block";
    modalImg.attr('src',$(this).attr('src'))
    // modalImg.src = this.src;
    captionText.innerHTML = this.alt;
});
subImg3.on("click", function() {
    modal1.removeClass("hide");
    // modal.style.display = "block";
    modalImg.attr('src',$(this).attr('src'))
    // modalImg.src = this.src;
    captionText.innerHTML = this.alt;
});
subImg4.on("click", function() {
    modal1.removeClass("hide");
    // modal.style.display = "block";
    modalImg.attr('src',$(this).attr('src'))
    // modalImg.src = this.src;
    captionText.innerHTML = this.alt;
});
// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  $('#Header').addClass("fixed-top");
  modal.style.display = "none";
}
// Get the <span> element that closes the modal
// var span = document.getElementsByClassName("close")[0];
// // When the user clicks on <span> (x), close the modal
// span.onclick = function() {
//     modal.addClass("hide");
//   // modal.style.display = "none";
// }
