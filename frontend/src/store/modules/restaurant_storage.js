'use strict'

var update_restaurants = async function (r_list, updateRestaurant) {
	local_rs = localStorage.restaurants
	r_list.foreach (function(r){
		console.log("Checking " + r.title + " (" + r.provider + ")")
		if (!local_rs[r.provider]) {
			console.log('... Empty provider ' + r.provider)
			local_rs[r.provider] = {}
		}
		if (!local_rs[r.provider][r.title]) {
			console.log("... Empty title: " + r.title + " (" + r.provider + ")")
			const result = await updateRestaurant(r.provider, r.title)
			console.log("Result after " + r.title + " update: " + result)
		}
		else if (local_rs[r.provider][r.title].hash != )
	});
}

export { update_restaurants }