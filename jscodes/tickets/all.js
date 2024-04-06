window.d = {
	ticket_data:{
		ticket_subject: "Transcorp .inc",
		ticket_main_city_info: "",
		ticket_main_company_inn_name: "no:",
		ticket_main_company_inn_value: "48238257764",
		ticket_type: "BUS",
		ticket_title: "control ticket",
		ticket_price: "21 rub",
		ticket_series_name: "series",
		ticket_series_value: "ty513",
		ticket_ads: "buy our elephants )",
		ticket_company_info: "bus company",
		ticket_company_inn_name: "no:",
		ticket_company_inn_value: "6723823989"
	}
};

window.rulesOfHappyness = new (function(){
	this.rules = [];

	this.init = function() {
		var rule1 = function(number) {
			var sum1 = number[0]*1 + number[1]*1 + number[2]*1;
			var sum2 = number[3]*1 + number[4]*1 + number[5]*1;
			return sum1 == sum2;
		}

		this.rules.push(rule1);			
	}

	this.init();
	return this.rules;
})();
window.x = new (function(){

	// Generating ticket by template, we can try to pass different data
	this.newTicket = function() {
		var ticket = window.ticketGenerator.new({rules: window.rulesOfHappyness});

		var ticketTemplate = document.getElementById("ticket-template");
		var ticketsOutput = document.getElementById("ticket-output");

		var html = window.t.htmlize(ticketTemplate.innerHTML, ticket);
		ticketsOutput.innerHTML = html + ticketsOutput.innerHTML;
		ticketsOutput.className += " animation";

		setTimeout(function() {
			ticketsOutput.className = ticketsOutput.className.replace("animation", "");
		}, 1000);
	}


	// Let's find needable sizes for current window
	this.initSizes = function() {
		var width, height, px;
		var zoom = 8;

		if (window.innerWidth > window.innerHeight) {
			height = Math.round(window.innerHeight / zoom) * 3;
			width = Math.round(window.innerHeight / zoom) * 2;
			px = window.innerHeight / (zoom * 60);
		} else {
			height = Math.round(window.innerWidth / zoom) * 3;
			width = Math.round(window.innerWidth / zoom) * 2;
			px = window.innerWidth / (zoom * 60);
		}

		if (!height || height < 105) {
			height = 105;
		}

		if (!width || width < 70) {
			width = 70;
		}

		if (!px || px < 0.59) {
			px = 0.59;
		}
		

		var ticket_header = document.getElementsByClassName("ticket__header");
		for (var i = 0; i < ticket_header.length; i++) {
			(ticket_header[i]).style.height = height * 10 / 100 + "px";
			(ticket_header[i]).style.width = width + 30 + "px";
		}

		var ticket_footer = document.getElementsByClassName("ticket__footer");
		for (var i = 0; i < ticket_footer.length; i++) {
			(ticket_footer[i]).style.height = height * 30 / 100 + "px";
			(ticket_footer[i]).style.width = width + 30 + "px";
		}

		var ticket_content_main = document.getElementsByClassName("ticket__content-main");
		for (var i = 0; i < ticket_content_main.length; i++) {
			(ticket_content_main[i]).style.height = height * 55 / 100 + "px";
		}

		var ticket_content_header = document.getElementsByClassName("ticket__content-header");
		for (var i = 0; i < ticket_content_header.length; i++) {
			(ticket_content_header[i]).style.height = height * 30 / 100 + "px";
		}

		var ticket_content_footer = document.getElementsByClassName("ticket__content-footer");
		for (var i = 0; i < ticket_content_footer.length; i++) {
			(ticket_content_footer[i]).style.height = height * 15 / 100 + "px";
		}

		var ticket_content = document.getElementsByClassName("ticket__content");
		for (var i = 0; i < ticket_content.length; i++) {
			(ticket_content[i]).style.height = height + 30 + "px";
		}

		var ticket = document.getElementsByClassName("ticket");
		for (var i = 0; i < ticket.length; i++) {
			(ticket[i]).style.width = width + 10 + "px";
			(ticket[i]).style.height = height *1.5 + "px";
		}

		var ticket_button = document.getElementById("get-ticket");
		ticket_button.style.width = width + 30 + "px";		


		var text10 = document.getElementsByClassName("px10");
		for (var i = 0; i < text10.length; i++) {
			text10[i].style.fontSize = 10 * px + "px";
		}

		var text7 = document.getElementsByClassName("px7");
		for (var i = 0; i < text7.length; i++) {
			text7[i].style.fontSize = 7 * px + "px";	
		}

		var text20 = document.getElementsByClassName("px20");
		for (var i = 0; i < text20.length; i++) {
			text20[i].style.fontSize = 20 * px + "px";		
		}
	}

	this.ticketButton = function() {
		var button = document.getElementById("get-ticket");
		var self = this;

		button.onclick = function() {
			self.newTicket();
			self.initSizes();
		}
	}

	this.initEvents = function() {
		var self = this;

		window.onresize = function() {
			self.initSizes();
		}

		window.onload = function() {
			self.ticketButton();
			self.initSizes();
		}
	}

	this.init = function() {
		this.initEvents();
	}

	this.init();
})();
window.t = new (function(){
	this.htmlize = function(html, data) {
		for (var i in data) {
			html = html.replace("#" + i + "#", data[i]);
		}
		return html;
	}
})();

window.ticketGenerator = new (function(){
	this.tickets = [];
	this.border_color = null;
	this.happy = null;

	this.getRandomInt = function(max) {
	  	return Math.floor(Math.random() * max);
	}

	this.getCity = function(){
		return "state of freedom";
	}

	this.getPrice = function() {
		return this.getRandomInt(100) + " rub";
	}

	this.city = this.getCity();
	this.price = this.getPrice();


 	this.getNumber = function() {
 		return (this.happy) ? (this.happy++, this.getNumberAsString()) : (this.getHappyTicket(), this.getNumberAsString());
 	};

	this.getHappyTicket = function() {
		var number = null;
		var happy = false;

		while (!happy) {
			this.getRandomNumber();
			number = this.getNumberAsString();

			for (var i = 0; i < this.rules.length; i++ ) {
				if (typeof(this.rules[i]) == "function") {
					happy = this.rules[i](number);
				} else {
					happy = false;
				}
			}			
		}

		return this.happy = number;
	}

	this.getNumberAsString = function() {
		return ((this.happy + "").length < 6) ? (Math.pow(10, 6 - (this.happy + "").length) + "").replace("1", "") + this.happy : this.happy;
	}

	this.getRandomNumber = function() {
		this.happy = Math.round(Math.random() * 1000000);
		return this.happy;
	}

	this.getBorderColor = function() {
		if (this.border_color) 
			return this.border_color;

	    var letters = '0123456789';
	    var number = 'rgba(';

	    for (var i = 0; i < 3; i++ ) {
	        number += Math.floor(Math.random() * 255) + ",";
	    }

	    number += "0.4)"
	    this.border_color = number;

	    return number;
	};

	this.new = function(options) {
		this.rules = options.rules || [];

		var data = window.d.ticket_data;
		var ticket = {
			ticket_subject: data.ticket_subject,
			ticket_main_city_info: this.city,
			ticket_main_company_inn_name: data.ticket_main_company_inn_name,
			ticket_main_company_inn_value: data.ticket_main_company_inn_value,
			ticket_type: data.ticket_type,
			ticket_title: data.ticket_title,
			ticket_price: this.price,
			ticket_series_name: data.ticket_series_name,
			ticket_series_value: data.ticket_series_value,
			ticket_ads: data.ticket_ads,
			ticket_company_info: data.ticket_company_info,
			ticket_company_inn_name: data.ticket_company_inn_name,
			ticket_company_inn_value: data.ticket_company_inn_value,
			ticket_number: this.getNumber(),
			last_ticket: this.tickets.length > 0 ? "": "last-ticket",
			border_color: 'style="border-color:'+this.getBorderColor()+';"'
		}

		this.tickets.push(ticket);
		return ticket;
	}	
})();