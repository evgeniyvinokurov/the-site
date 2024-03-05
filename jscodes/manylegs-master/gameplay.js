gameplay = function()
{
	this.points = 0;
	this.level = 3;
	this.count = Math.floor(Math.random() * 4 * this.level) + 2;
	this.mnogonozhky = [];
	this.mnogonozhky_went = [];
	this.current = 0;
	this.cur_color = "red";
	this.legs_count = 0;

	this.temperature = 20;

	this.temperature_timeout = false;
	this.queue_timeout = false;

	this.speed = 1;
	
	this.updown_q = 1;
	this.temperature_q = 1;
	this.queue_q = 1;
	this.time_anti_bonuses = 0;

	var self = this;

	this.init_temperature = function(cb){
		var self = this;

		self.temperature = -30 + Math.random() * 60;			
		self.draw_temperature();
	}

	this.set_temperature = function(cb)
	{	
		var self = this;

		self.temperature = -30 + Math.random() * 60;						
		self.temperature_q = ((self.temperature + 30) / 60) * 65;
		self.draw_temperature();
	}

	this.get_random_color = function() {
	    var letters = '0123456789ABCDEF'.split('');
	    var color = '#';
	    for (var i = 0; i < 6; i++ ) {
	        color += letters[Math.floor(Math.random() * 16)];
	    }
	    return color;
	}

	this.change_color = function(color)
	{
		var rand = Math.floor(Math.random() * 3);
		//console.log(rand);
		//var new_color = this.get_random_color();

		var needable_path = $("#mnogo");

		var style = needable_path.attr("style");
		style = style.replace(this.cur_color, color);
		needable_path.attr("style", style);
		this.cur_color = color;

		//style="fill:#e95f1a;fill-opacity:1;fill-rule:evenodd;stroke:none"
	    //       id="path2985-9"
	}

	this.change_legs = function(legs)
	{
		var needable_path = $("#mnogo"), html ="";
		
		for(var i= 0; i<legs;i++)
			html+="●";

		needable_path.html(html);
	}


	this.wait = function(ms)
	{
	    var start = new Date().getTime();
	    var end = start;
	    while(end < start + ms) 
	    {
	    	end = new Date().getTime();
	    }
	}

	this.wear_current = function()
	{
		this.mnogonozhky[this.current].wear();
	}

	this.go_current = function(cb)
	{
		this.mnogonozhky[this.current].go();
	}

	this.init = function()
	{
		for(var i = 0; i < this.count; i++)
		{
			var x = 1;

			while(isOdd(x))
			{
				x = Math.floor(Math.random() * 10);
			}

			var mnogonozhka_i = new mnogonozhka(x);
			this.mnogonozhky.push(mnogonozhka_i);
			this.legs_count += x;
		}
	}

	this.draw_mnogonozhka = function(key)
	{
		this.current = key;

		this.change_color(this.mnogonozhky[this.current].color);
		this.change_legs(this.mnogonozhky[this.current].legs);
		this.mnogonozhky[this.current].show();
	}

	this.draw_temperature = function()
	{	
		var max_temp = 30;
		var percent = (Math.abs(this.temperature) / max_temp ) * 50;

		if(this.temperature > 0)
		{					
			$(".temperature .hg-red").css({"height": percent+"%"});
			$(".temperature .hg-blue").css({"height": "0%"});		
			$(".temperature .emptyness-down").css({"height": 50 +"%"});							
			$(".temperature .emptyness-up").css({"height": 50-percent+"%"});					
		}
		else
		{					
			$(".temperature .hg-blue").css({"height": percent+"%"});
			$(".temperature .hg-red").css({"height": "0%"});				
			$(".temperature .emptyness-up").css({"height": 50 +"%"});							
			$(".temperature .emptyness-down").css({"height": 50-percent + "%"});									
		}
	}

	this.next_mnogonozhka = function()
	{
		var self = this;
		var counter = 0, allwent = true;
		
		for(var mnogonozhka of this.mnogonozhky) {
			allwent = allwent && mnogonozhka.went;
		}
 		
 		if (!allwent){
	 		do {
				if(self.mnogonozhky.length > self.current + 1)
					self.current += 1
				else{
					self.current = 0;
				}
			} while (this.mnogonozhky[self.current].went)	
			
			self.draw_mnogonozhka(self.current);			
			return true;
		} else{
			$("#mnogo").html("")
			$("#end").html("end")
			return false;
		} 
	}

	this.check = function() {
		var happyness = 0;
		var sadness = 0;

		for(var mnogonozhka of this.mnogonozhky) {
			happyness += mnogonozhka.happyness;
			sadness += mnogonozhka.tiredness;
		}

		$("#happyness").html(happyness);
		$("#sadness").html(sadness);
	}
}
