window.player = (function(){
	const defaultText = "Greetings!!! / Поздравления!!!";

	let playing = false;

	let dataEn = [
		[
			"Comrades, ",
			"On the other hand",
			"Equally",
			"One should not, however, forget that",
			"In this way",
			"Everyday practice shows that"
		],
		[
			"the implementation of the planned targets",
			"frame and place of study",
			"constant quantitative growth and the scope of our activity",
			"the existing structure of the organization",
			"new model of organizational activity",
			"further development of various forms of activity"
		],
		[
			"plays an important role in shaping",
			"they require analysis from us",
			"require definition and clarification",
			"contributes to the preparation and implementation",
			"provides a wide range of (specialists) participation in the formation",
			"allows you to complete important development tasks"
		],
		[
			"of material financial and administrative conditions",
			"of further development directions",
			"of participatory systems",
			"of positions held by participants in relation to the tasks",
			"of new offers",
			"of directions of progressive development",
		]
	];

	let dataRu = [
		[
			"Товарищи, ",
			"С другой стороны",
			"Равным образом",
			"Не следует, однако, забывать, что",
			"Таким образом",
			"Повседневная практика показывает, что" 
		],
		[
			"реализация плановых заданий",
			"место и рамки обучения кадров",
			"постоянный количественный рост и сфера нашей активности",
			"сложившаяся структура организации",
			"новая модель организационной деятельности",
			"дальнейшее развитие различных форм деятельности"
		],
		[
			"играет важную роль в формировании",
			"требует от нас анализа",
			"требует определения и уточнения",
			"способствует подготовке и реализации",
			"обеспечивает широкому кругу (специалистов) участие в формировании",
			"позволяет выполнить важные задания по разработке"
		],
		[
			"существенных финансовых и административных условий",
			"дальнейших направлений развития",
			"системы массового участия",
			"позиций, занимаемых участниками в отношении поставленных задач",
			"новых предложений",
			"направлений прогрессивного развития"
		]
	];

	let msgText = defaultText;

	let marquee = function(msgText){		
		var obj = document.getElementsByClassName("textMarquee");
		obj[0].innerHTML = msgText;
	}

	let getRandomInt = function(min, max) {
	    return Math.floor(Math.random() * (max - min + 1)) + min;
	}

	let getText = function(lang) {
		var data = dataEn;

		switch(lang){
			case "ru":
				data = dataRu;
			break;
			case "en":
				data = dataEn;
			break;
		}

		let result = '';
		for (let i = 0, len = data.length; i < len; i++) {
			result += ' ' + data[i][getRandomInt(0, 5)];
		}

		return result;
	};

	let browserSupport = function() {		
		if (typeof speechSynthesis == 'undefined' || typeof SpeechSynthesisUtterance == 'undefined') {
			alert('browser not supported');
			return false; 
		}
		return true;
	}

	let play = function() {
		playing = true;
		
		if (!browserSupport())
			return false;

		let lang = "en";
		let ruVoice = null;

		let voices = speechSynthesis.getVoices();

		if (voices.length == 0) {
			marquee("Problem with speech synthesis voices / Проблема с голосами синтезатора речи")				
		} else {
			for(voice of voices) {				
				if (voice.lang.indexOf("ru") != -1) {
					lang = "ru";
					ruVoice = voice;
				}
			}
		}
			
		if (playing) {
			let msg = new SpeechSynthesisUtterance()

			msgText = getText(lang);
			msg.text = msgText;

			if (lang == "ru") {
				msg.voice = ruVoice;
			}

			msg.addEventListener('end', function(event) {
				if (playing) {
					play();
				}
			});
			
			speechSynthesis.speak(msg);
			marquee(msgText);
		} else {
			stop();
		}
	};

	let stop = function() {
		playing = false;
		speechSynthesis.cancel();

		marquee(defaultText)
	}

	let toggle = function(e) {
		playing ? stop() : play();
	}

	return {
		toggle: toggle
	}
})();
