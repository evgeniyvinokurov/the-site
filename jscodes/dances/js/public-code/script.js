jQuery(document).ready(function ($) {
			
	// Sliders
	var swiper = new Swiper('.slider-container', {
		slidesPerView: 1,
		spaceBetween: 0,
		grabCursor: true
	});
	var swiper2 = new Swiper('.slider2-container', {
		slidesPerView: 3,
		spaceBetween: 0,
		grabCursor: true
	});

    $('.js-main-slider-left').click(function () {
        swiper2.slidePrev();
    });

    $('.js-main-slider-right').click(function () {
        swiper2.slideNext();
    });

    // Bongos (Don't know how bongos differ from tam tams)
    $('.tam').click(function () {
        $("#"+$(this).data("audio")).clone()[0].play();
    });


    // Map Buttons
    var data = {
    	"bycicle": {
			text: "This is a comedy/drama with a strong theme of mistrust. The story is about a prostitute who is constantly opposed by a weapons officer. It starts in a village. The story begins with a holiday preparation. A sudden increase in dangerous monsters is a major plot element.",
			level: 2
    	},
		"train": {
			text: "This is an epic about discovery. The story is about a prince, a diabolical movie producer, a politician, and a scribe. It takes place on a generation ship. The future of warfare is a major part of this story.",
			level: 1
		},
		"car": {
			text: "This is an epic about religion versus creativity. The story is about a policeman who is married to a biologist. It takes place in an apartment complex in an outpost. The return of an ancient evil plays an important part in the story.",
			level: 1
		},
		"plane": {
			text: "The story is about an inhibited hermit who is constantly annoying an assassin. It takes place in a bank in a small city. The story climaxes with a natural disaster.",
			level: 1
		},
		"foot": {
			text: "This is a crime drama with an emphasis on the need for traditional values. The story is about two extraverted mentors. It starts aboard a space station used for on a deep-space probe. A major element of this story is when technology becomes indistinguishable from magic.",
			level: 2
		},
		"bus": { 
			text: "The story is about eight medical officers. It starts in a town in the Arctic. The story begins with research being done.",
			level: 1
		}
    };

    var timeout = null;

    $(document).on("mouseover", "#map .map-button", function(){
    	$('.js-descriptions:eq(0)').html(data[$(this).data("type")]["text"]);
    	$('.js-descriptions:eq(1)').css({top: data[$(this).data("type")]["level"] == 1 ? "236px": "280px"})
    	$('.js-descriptions').show();
    })

    $(document).on("mouseleave", "#map .map-button", function(){
    	$('.js-descriptions').hide();
    })

    // Ymaps    	
    if (!!ymaps) {
	 	ymaps.ready(function () {
		    var myMap = new ymaps.Map('map', {
		            center: [53.755, 127.237347],
		            zoom: 13,
		            controls: []
		        }, {
		            searchControlProvider: 'yandex#search'
		        }),

		        // Creating a content layout.
		        MyIconContentLayout = ymaps.templateLayoutFactory.createClass(
		            '<div style="color: #FFFFFF; font-weight: bold;">$[properties.iconContent]</div>'
		        ),

		        myPlacemarkWithContent = new ymaps.Placemark([53.765105, 127.237347
					], {
		            hintContent: 'Dance Festival Party Hint',
		            balloonContent: 'Dance Festival Party',
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



		    // Creating a polygon using the GeoObject class.
		    var myGeoObject = new ymaps.GeoObject({
		        // Describing the geometry of the geo object.
		        geometry: {
		            // The "Polygon" geometry type.
		            type: "Polygon",
		            // Specifying the coordinates of the vertices of the polygon.
		            coordinates: [
		                // The coordinates of the vertices of the external contour.
		                [
		                    [53.76, 127.23],
		                    [53.7608, 127.2282],
		                    [53.7638, 127.2314],
		                    [53.7652, 127.2458],
		                    [53.7616, 127.2480]
		                ],
		            ],
		            // Setting the fill rule for internal contours using the "nonZero" algorithm.
		            fillRule: "nonZero"
		        },
		        // Defining properties of the geo object.
		        properties:{
		            // The contents of the balloon.
		            balloonContent: "Polygon"
		        }
		    }, {
		        /**
		         * Describing the geo object options.
		         *  Fill color.
		         */
		        fillColor: '#ffffff00',
		        // Stroke color.
		        strokeColor: '#000000',
		        // The overall transparency (for both fill and stroke).
		        // The stroke width.
		        strokeWidth: 4,
		        // The stroke style.
		        strokeStyle: 'shortdash'
		    });

		    // Adding the polygon to the map.
		    myMap.geoObjects.add(myGeoObject);

		    
		    var template1 =
			  '<div><img width="40px" class="map-button" data-type="bus" src="imgs/button1.png"/></div>' 
			var template2 =
			  '<div><img width="40px" class="map-button" data-type="train" src="imgs/button2.png"/></div>' 
			var template3 =
			  '<div><img width="40px" class="map-button" data-type="car" src="imgs/button3.png"/></div>'
			var template4 =
			  '<div><img width="40px" class="map-button" data-type="plane" src="imgs/button4.png"/></div>' 
			var template5 =
			  '<div><img width="40px" class="map-button" data-type="foot" src="imgs/button5.png"/></div>' 
			var template6 =
			  '<div><img width="40px" class="map-button" data-type="bycicle" src="imgs/button6.png"/></div>'

			myMap.controls.add(
			  new ymaps.control.Button({
			    options: {
			      layout:
			        ymaps.templateLayoutFactory.createClass(
			            template1
			        ),
			      maxWidth: 50
			    }}),{
				  float: "none",
				  position: {
				  	bottom: 75,
				  	right: 145
				  }
				}
			);
			myMap.controls.add(
			  new ymaps.control.Button({
			    options: {
			      layout:
			        ymaps.templateLayoutFactory.createClass(
			            template2
			        ),
			      maxWidth: 50
			    }}),{
				  float: "none",
				  position: {
				  	bottom: 75,
				  	right: 55
				  }
				}
			);
			myMap.controls.add(
			  new ymaps.control.Button({
			    options: {
			      layout:
			        ymaps.templateLayoutFactory.createClass(
			            template3
			        ),
			      maxWidth: 50
			    }}),{
				  float: "none",
				  position: {
				  	bottom: 75,
				  	right: 10
				  }
				}
			);
			myMap.controls.add(
			  new ymaps.control.Button({
			    options: {
			      layout:
			        ymaps.templateLayoutFactory.createClass(
			            template4
			        ),
			      maxWidth: 50
			    }}),{
				  float: "none",
				  position: {
				  	bottom: 75,
				  	right: 100
				  }
				}
			);
			myMap.controls.add(
			  new ymaps.control.Button({
			    options: {
			      layout:
			        ymaps.templateLayoutFactory.createClass(
			            template5
			        ),
			      maxWidth: 50
			    }}),{
				  float: "none",
				  position: {
				  	bottom: 30,
				  	right: 55
				  }
				}
			);
			myMap.controls.add(
			  new ymaps.control.Button({
			    options: {
			      layout:
			        ymaps.templateLayoutFactory.createClass(
			            template6
			        ),
			      maxWidth: 50
			    }}),{
				  float: "none",
				  position: {
				  	bottom: 30,
				  	right: 10
				  }
				}
			);
		});
	}


	// Interactive earth

	var countries = [
		{
			id: "path4140",
			name: "ligula",
			text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
		},	
		{
			id: "path4142",
			name: "molestie",
			text: "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. "
		},	
		{
			id: "path4146",
			name: "vehicula",
			text: "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. "
		},	
		{
			id: "path4148",
			name: "rutrum",
			text: "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga."
		}
	];

	var paths = ["path4140", "path4142", "path4146", "path4148"];



    function mouseOverEarthCheck(x, y, center) {
    	var z = Math.pow(125, 2) > Math.pow(x - center.x, 2) + Math.pow(y - center.y, 2)

    	return z;
    }

    function getdecenter(center, x, y, r) {
    	var b = (x * center.y - y * center.x) / (x - center.x);
    	var a = (y - b) / x;

    	var b2 = 2*a*b - 2 * center.x - 2 * a * center.y;

    	var c = (b - center.y)*(b - center.y) + center.x * center.x - r*r; 
    	var a2 = (a*a + 1);
    	var ac = a2 * c; 
    	var d = b2*b2 - 4*ac;

    	var xx = (- b2 - (x > center.x ? -1:1) * Math.sqrt(d)) / (2 * a2);
    	var yy = a * xx + b;
    	var yy2 = Math.sqrt(r*r - (xx - center.x)*(xx - center.x)) + center.y;

    	return { x:xx , y:yy };
    }


    function init(center) {
        var mouseOver = false;        
        
        var objectForClicking = $(".js-earth-block");
        var earthObj = $("#earthsvg");
        var svgCanvas = $("#svgCanvas");
        var label = $(".js-earth-label");
        var info = $(".js-country-info");
        var fixed = false;

        objectForClicking.click(function(e) {
        	fixed = !fixed; 
        });

        objectForClicking.mousemove(function(e) {
        	
        	if (mouseOver && !fixed) {
	            var x = e.pageX - $(this).offset().left;
	            var y = e.pageY - $(this).offset().top;

	            do {
			    	var decenter = getdecenter(center, x, y, 182);
			    	var decenter2 = getdecenter(center, x, y, 80);

			    	var overY = window.outerHeight - (decenter.y + info.outerHeight());
			    	y = y - 1;
		   		}
		    	while (overY < 0) 

		    	var d = "M "+ Math.ceil(decenter2.x)+","+Math.ceil(decenter2.y)+" L "+Math.ceil(decenter.x)+","+Math.ceil(decenter.y) +";";

		    	var textWidth = label.outerWidth();
		    	var textHeight = label.outerHeight();

		    	var computedx = Math.ceil(x > center.x ? decenter.x + textWidth : decenter.x -textWidth);

		    	var textLeft = x > center.x ? computedx - textWidth : computedx;

		    	var d2 = "M "+ Math.ceil(decenter.x)+","+Math.ceil(decenter.y)+" L "+computedx+","+Math.ceil(decenter.y) +";";

		    	$("#line").find("animate").attr("values", d);

		    	$("#line2").attr("d", d2);


		    	label.css({top: decenter.y - textHeight, left: textLeft});

		    	var popupLeft = x > center.x ? textWidth + textLeft : textLeft - info.outerWidth();

		    	info.css({top: decenter.y - 4, left: popupLeft});
        	}

        	mouseOverEarth = mouseOverEarthCheck(x, y, center);
        	var hide = !mouseOver && !fixed;

        	if (hide) {       		
	        	svgCanvas.css({visibility: "hidden"});   		
	        	label.css({visibility: "hidden"}); 		
	        	info.css({visibility: "hidden"});
	        } else {
	            svgCanvas.css({visibility: "visible"});	
	            label.css({visibility: "visible"});		
	        	info.css({visibility: "visible"});
        	}
        });
	

		$.each(paths, function(i, path) {

			$(document).find("#" + path).on("mouseover", function () {
				mouseOver = true;
				var self = this;

				$.each(countries, function(i, country) {
					if ($(self).attr("id") == country.id) {

						label.html(country.name);

						info.find(".js-title").html(country.name);
						info.find(".js-text").html(country.text);
					}
				})
			})

			$(document).find("#" + path).on("mouseleave", function () {
				mouseOver = false;
			})					
		})
    }

    init({x:350, y:250});
});