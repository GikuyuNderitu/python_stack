"use strict";

const appendRow = function (arr) {
	let fName = arr[0].value
	let lName = arr[1].value
	let email = arr[2].value
	let phone = arr[3].value

	$('tbody').append(()=>{
		let content = "<tr>"+
			"<td>"+fName+"</td>"+
			"<td>"+lName+"</td>"+
			"<td>"+email+"</td>"+
			"<td>"+phone+"</td>"+
		"</tr>"

		return content;
	})

}

$(document).ready(function(){
	$('.close').click(function () {
		$(this).parent().remove()
	})
	$('label').has('textarea').css({
		'flex-direction': 'column'
	})
	$("#survey").submit(function(){
		appendRow($(this).serializeArray());
	})
})
