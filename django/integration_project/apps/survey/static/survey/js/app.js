$(function () {
	const langs = ['JavaScript', 'Ruby', 'iOS/Swift', 'C#/.NET', 'C/C++', 'Python', 'Go', 'Java', 'Fortran', 'Basic'].sort((a,b)=>{ return a[0].toLowerCase() > b[0].toLowerCase()})
	const locs = ['Washington D.C.', 'San Francisco', 'Seattle', 'Dallas', 'Chicago', 'Dojo-topia'].sort()
	const prefix = '<option value="'
	const middle = '">'
	const suffix = '</option>'
	$('#languages').append(()=>{
		let str = ''
		for (let i = 0; i < langs.length; i++) {
			str += prefix + langs[i]+ middle + langs[i] + suffix
		}
		return str
	})

	$('#locations').append(()=>{
		let str = ''
		for (let i = 0; i < locs.length; i++) {
			str += prefix + locs[i]+ middle + locs[i] + suffix
		}
		return str
	})
})
