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
	const locations = ['Silicon Valley','Seattle','Los Angeles', 'Dallas', 'Washington DC', 'Chicago', 'Berkeley', 'Orange County'].sort()
	const langs = ['Python', 'Ruby', 'Swift', 'Objective-C', 'JavaScript', 'Java', 'C/C++', 'Assembly! (NERD)'].sort()

	locations.forEach(val => {$('#locations').append(`<option value="${val}">${val}</option>`)})
	langs.forEach(val => {$('#langs').append(`<option value="${val}">${val}</option>`)})
	console.log(langs);

	$('label').has('textarea').css({
		'flex-direction': 'column'
	})
	$("#survey").submit(function(){
		appendRow($(this).serializeArray());
	})
})
