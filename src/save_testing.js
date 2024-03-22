//This script doesn't actually do anything for our input page at the moment.//
//It's here as a placeholder for the script I will need to write later in order to make the page save input.//
var main = function() {

	$('form').submit(function(event) {
		var $input = $(event.target).find('input');
		var comment = $input.val();

		if (comment != "") {
			var state_names = ;
		}

		return false;
	});

}

$(document).ready(main);