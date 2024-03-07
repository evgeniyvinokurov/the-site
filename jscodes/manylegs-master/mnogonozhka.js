mnogonozhka = function(legs)
{
	this.legs = legs || 4;
	this.color = gplay.get_random_color();			
	this.showed = 0;
	this.weared = 0;
	this.went = false;
	this.happy = null;
	this.happyness = 50;
	this.tiredness = 0;

	this.wear = function()
	{
		this.weared += 2;
	}

	this.show = function()
	{
		this.showed += 2;

		this.happyness = ( this.weared / this.legs ) * 100;
		this.tiredness = this.showed + (100 - ( this.weared / this.legs ) * 100);
	}

	this.go = function()
	{
		this.went = true;

		if(this.legs !== this.weared)
		{
			this.happy = false;
		}
		else
		{
			this.happy = true;
		}
	}
}