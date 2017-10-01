// This is "probably" IE9 compatible but will need some fallbacks for IE8
// - (event listeners, forEach loop)

// wait for the entire page to finish loading
window.addEventListener('load', function() {

	// setTimeout to simulate the delay from a real page load
	setTimeout(lazyLoad, 1000);

});

function lazyLoad() {
	var card_images = document.querySelectorAll('.card-image');

	// loop over each card image
	card_images.forEach(function(card_image) {
		var image_url = card_image.getAttribute('data-image-full');
		var content_image = card_image.querySelector('img');

		// change the src of the content image to load the new high res photo
		content_image.src = image_url;

		// listen for load event when the new photo is finished loading
		content_image.addEventListener('load', function() {
			// swap out the visible background image with the new fully downloaded photo
			card_image.style.backgroundImage = 'url(' + image_url + ')';
			// add a class to remove the blur filter to smoothly transition the image change
			card_image.className = card_image.className + ' is-loaded';
		});

	});

}

// Slider configuration
var config = {
  speed: 3000,
  auto: true, // true or false
  arrows: true, // true or false
  nav: true, // true or false
  navStyle: 'default' // square,rectangle, default
};

// Slider core
var slides = $('.slide');
var totalSlides = slides.length;
var currentIndex = 0;

function setSlides() {
  var currentSlide = slides.eq(currentIndex);
  slides.hide();
  currentSlide.fadeIn(1500);
};
setSlides();

// autoplay
if (config.auto) {
  var autoSlide = setInterval(function() {
    currentIndex += 1;
    if (currentIndex > totalSlides - 1) {
      currentIndex = 0;
    }
    setSlides();
    navigation();
  }, config.speed);
};

// navigation arrows
if (config.arrows) {
  $('.arrow').addClass('active');
  $('.prev').click(function() {
    clearInterval(autoSlide);
    currentIndex -= 1;
    if (currentIndex < 0) {
      currentIndex = totalSlides - 1;
    }
    navigation();
    setSlides();
  });
  $('.next').click(function() {
    clearInterval(autoSlide);
    currentIndex += 1;
    if (currentIndex > totalSlides - 1) {
      currentIndex = 0;
    }
    navigation();
    setSlides();
  });
};

// navigation
if (config.nav) {
	for (i = 0; i < slides.length; i+=1) {
  	$('<li/>').attr( {'class': 'nav-item','id': i}).appendTo('.slide-nav');
	};
  $('.nav-item').first().addClass('item-active');
  switch(config.navStyle) { // navigation style
    case 'square':
        $('.nav-item').addClass('square');
        break;
    case 'rectangle':
        $('.nav-item').addClass('rectangle');
        break;
    default:
        $('.nav-item').addClass('dot');
  };
  function navigation() {
    $('.nav-item').removeClass('item-active');
    $('.nav-item').eq(currentIndex).addClass('item-active');
  };
	$('.nav-item').click(function() {
  	clearInterval(autoSlide);
  	var navNumb =  $(this).attr('id');
  	currentIndex = navNumb;
  	navigation();
  	setSlides();
  });
};
