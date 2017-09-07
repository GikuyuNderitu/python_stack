const remove_range = function (arr, start, end) {
	for(var i = end+1; i < arr.length; i++)
		arr[i-(end-start)-1] = arr[i]
	arr.length = i-(end-start)-1
}

let arr = [20,30,40,50,60,70,80,90,100]

console.log(arr);
remove_range(arr,1,4)
console.log(arr);
