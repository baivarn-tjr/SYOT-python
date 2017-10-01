
	$(document).ready(function () {
    	$('#logo').addClass('animated fadeInDown');
    	$("input:text:visible:first").focus();
	});
	$('#username').focus(function() {
		$('label[for="username"]').addClass('selected');
	});
	$('#username').blur(function() {
		$('label[for="username"]').removeClass('selected');
	});
	$('#password').focus(function() {
		$('label[for="password"]').addClass('selected');
	});
	$('#password').blur(function() {
		$('label[for="password"]').removeClass('selected');
	});
  $('#email').focus(function() {
		$('label[for="email"]').addClass('selected');
	});
	$('#email').blur(function() {
		$('label[for="email"]').removeClass('selected');
	});
  $('#name').focus(function() {
		$('label[for="name"]').addClass('selected');
	});
	$('#name').blur(function() {
		$('label[for="name"]').removeClass('selected');
	});
  $('#address').focus(function() {
		$('label[for="address"]').addClass('selected');
	});
	$('#address').blur(function() {
		$('label[for="address"]').removeClass('selected');
	});

	
	function goBack() {
    	window.history.back();
	}
