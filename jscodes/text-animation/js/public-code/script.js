getRandomInt = (max) => {
  return Math.floor(Math.random() * max);
}

glob = {
	phrase: "If you really want to hear about it, the first thing you'll probably want to know is where I was born, an what my lousy childhood was like, and how my parents were occupied and all before they had me, and all that David Copperfield kind of crap, but I don't feel like going into it, if you want to know the truth. In the first place, that stuff bores me, and in the second place, my parents would have about two hemorrhages a piece if I told anything pretty personal about them."
}


let setTimes = (keys, keys2, selector, phrase) => {
	random = getRandomInt(keys.length);
	child = keys[random] + 1;

	setTimeout(function() {
			let x = ".line" + phrase.i + " " + selector + " .letter:nth-child(" + child + ")";

			$(x).removeClass("hide");
      $(x).addClass("showin");

			keys.splice(random, 1);

			cond = ((keys.length == 0) && (keys2.length == 0));
			if (!cond){
				f(phrase);
			}
		}, 10);
}

let f = function(phrase) {
		let count = 0, cond = false, random, isFirst = false;
		let keysUp = Array.from([...Array(phrase.text.length)].keys());
		let keysDown = Array.from([...Array(phrase.text.length)].keys());

		cond = ((keysUp.length == 0) && (keysDown.length == 0));
		isFirst = ((Math.random() < 0.5) || (keysDown.length == 0)) && (keysUp.length != 0);

		switch (isFirst) {
			case true:
					setTimes(keysUp, keysDown, ".first", phrase)
					break;
			default:
					setTimes(keysDown, keysUp, ".second", phrase)
					break;
		}
}

jQuery(document).ready(function($) {
		let stringLetter = "", sar = [], s = "", lineLength = 50, cnt = 2, j = 0;

		for(let sym of glob.phrase){
      let char = (sym == " ") ? "&nbsp;": sym;
			stringLetter += "<div class='letter hide'>" + char + "</div>";
			s += char;

			if ((cnt % lineLength == 0) || cnt == glob.phrase.length) {
				$(".site__content").append("<div class='line line" + j + "'><div class='first'>" + stringLetter + "</div><div class='second'>" + stringLetter + "</div>");
				sar.push({text:s, i:j})
				s = "";
				j++;
				stringLetter = "";
			}
			cnt++;
		}

		for (phrase of sar) {
			f(phrase);
		}
});
