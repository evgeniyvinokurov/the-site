
document.addEventListener("DOMContentLoaded", (event) => {

    ///// Maps 
	
	// LONGITUDE -180 to + 180
	function generateRandomLong() {
	    var num = (Math.random()*180).toFixed(3);
	    var neg = Math.ceil(Math.random());
	    if (neg == 0) {
	        num = num * -1;
	    }
	    return num;
	}

	// LATITUDE -90 to 90
	function generateRandomLat() {
	    var num = (Math.random()*90).toFixed(3);
	    var neg = Math.ceil(Math.random());
	    if (neg == 0) {
	        num = num * -1;
	    }
	    return num;
	}

    // Ymaps    	

    if (!!ymaps) {
    	var lat = generateRandomLat();
    	var long = generateRandomLong();

	 	ymaps.ready(function () {
		    var myMap = new ymaps.Map('map', {
		            center: [lat-1, long-1],
		            zoom: 5,
		            controls: []
		        }, {
		            searchControlProvider: 'yandex#search'
		        })

		        // Creating a content layout.
		        MyIconContentLayout = ymaps.templateLayoutFactory.createClass(
		            '<div style="color: #FFFFFF; font-weight: bold;">$[properties.iconContent]</div>'
		        ),

		        myPlacemarkWithContent = new ymaps.Placemark([lat, long
					], {
		            hintContent: 'Hello, hello, hello!! We glad to see you here))))',
		            balloonContent: 'Food Festival party',
		            iconContent: ' '
		        }, {
		            /**
		             * Options.
		             * You must specify this type of layout.
		             */
		            iconLayout: 'default#imageWithContent',
		            // Custom image for the placemark icon.
		            iconImageHref: 'imgs/placemark.png',
		            // The size of the placemark.
		            iconImageSize: [37, 57],
		            /**
		             * The offset of the upper left corner of the icon relative
		             * to its "tail" (the anchor point).
		             */
		            iconImageOffset: [-24, -24],
		            // Offset of the layer with content relative to the layer with the image.
		            iconContentOffset: [15, 15],
		            // Content layout.
		            iconContentLayout: MyIconContentLayout
		        });

		    myMap.geoObjects
		        .add(myPlacemarkWithContent);
            
            myMap.panTo([
                    [lat, long]
                ]);


		});
	}

});