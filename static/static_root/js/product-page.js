// Get the modal
var modal = document.getElementById('myModal');
// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById('front-model');
var subImg1 = document.getElementById('sub-model-1');
var subImg2 = document.getElementById('sub-model-2');
var subImg3 = document.getElementById('sub-model-3');
var subImg4 = document.getElementById('sub-model-4');
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");

<<<<<<< HEAD
img.onclick = function(){
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
}

subImg1.onclick = function(){
=======
// close modal if click on background//
$(document).click(function (e) {
    if ($(e.target).is('#img01')) {
        modal.style.display = "none";
    }
    if($(e.target).is('#myModal')){
        modal.style.display = "none";
    }
});


img.onclick = function(){
    $('#Header').removeClass("fixed-top");
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
    if($('#img01').data('clicked')) {
        alert('yes');
    }
}

subImg1.onclick = function(){
    $('#Header').removeClass("fixed-top");
>>>>>>> 257f3058b6350ff90c2074b53d6e3abfee0c8527
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
}

subImg2.onclick = function(){
<<<<<<< HEAD
=======
    $('#Header').removeClass("fixed-top");
>>>>>>> 257f3058b6350ff90c2074b53d6e3abfee0c8527
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
}

subImg3.onclick = function(){
<<<<<<< HEAD
=======
    $('#Header').removeClass("fixed-top");
>>>>>>> 257f3058b6350ff90c2074b53d6e3abfee0c8527
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
}

subImg4.onclick = function(){
<<<<<<< HEAD
=======
    $('#Header').removeClass("fixed-top");
>>>>>>> 257f3058b6350ff90c2074b53d6e3abfee0c8527
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
<<<<<<< HEAD
span.onclick = function() {
=======
span.onclick = function() { 
  $('#Header').addClass("fixed-top");
>>>>>>> 257f3058b6350ff90c2074b53d6e3abfee0c8527
  modal.style.display = "none";
}
