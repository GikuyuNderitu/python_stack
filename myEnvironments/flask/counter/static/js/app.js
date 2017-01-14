"use strict";

const setSize = function () {
	console.log('run');
	$('span').css('font-size', function (idx) {
		if( $('#container').data('num') < 17)
			return  $('#container').data('num')*11
		else
			return 15*15
	})
}

const resetVal = function () {
	$('input').attr('value', 'reset')
}

$(document).ready(function () {
	$('input').attr('value',$('#container').data('num'))

	setSize()
	$('form').submit(function () {
	})
})
