function hidePanels(panelSection) {
	var ptarget = document.getElementById(panelSection);
	var bid = panelSection.concat('button');
	var btarget = document.getElementById(bid);
	var hide = 'Hide '.concat(panelSection)
	var show = 'Show '.concat(panelSection)
	if (ptarget.style.display === "none") {
		ptarget.style.display = "block";
		btarget.innerHTML=hide;
	} else {
		ptarget.style.display = "none";
		btarget.innerHTML=show;
	}
}

//function changeButton(buttonId) {
//	var target
//}	


// This sample uses the Autocomplete widget to help the user select a
// place, then it retrieves the address components associated with that
// place, and then it populates the form fields with those details.
// This sample requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">

function initAutocomplete() {
  // Create the autocomplete object, restricting the search predictions to
  // geographical location types.
  autocomplete = new google.maps.places.Autocomplete(
      document.getElementById('address'), {types: ['geocode']});
      
  // Avoid paying for data that you don't need by restricting the set of
  // place fields that are returned to just the address components.
  autocomplete.setFields(['address_component']);
  
}

// Bias the autocomplete object to the user's geographical location,
// as supplied by the browser's 'navigator.geolocation' object.
function geolocate() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var geolocation = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      var circle = new google.maps.Circle(
          {center: geolocation, radius: position.coords.accuracy});
      autocomplete.setBounds(circle.getBounds());
    });
  }
}
