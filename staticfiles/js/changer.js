console.log("changer entered")

let theme = localStorage.getItem('theme')
if(theme==null){
    setTheme('light')
}
else {
    setTheme(theme)
}

let language = localStorage.getItem('language')
if(language==null){
    setLanguage('english')
}
else {
    setLanguage(language)
}

let themeDots = document.getElementsByClassName('theme-dot')

for (var i=0; themeDots.length > i; i++){
	themeDots[i].addEventListener('click', function(){
		let mode = this.dataset.mode
		console.log('Option clicked:', mode)
		setTheme(mode)
	})
}

function setTheme(mode){
	if(mode == 'yellow'){
		document.getElementById('theme-style').href ="/static/css/yellow.css"
	}

	if(mode == 'blue'){
		document.getElementById('theme-style').href ="/static/css/blue.css"
	}

	if(mode == 'green'){
		document.getElementById('theme-style').href ="/static/css/green.css"
	}

	if(mode == 'purple'){
		document.getElementById('theme-style').href = "/static/css/purple.css"
	}

	//localStorage.setItem('theme', mode)
}

let languageSelect = document.getElementsByClassName('dropdown-item')

for (var i=0; languageSelect.length > i; i++) {
    languageSelect[i].addEventListener('click', function() {
        let mode = this.dataset.mode
        console.log('Language clicked:',mode)
        setLanguage(mode)
    })
}

function setLanguage(mode) {
    if(mode == 'francais') {
        console.log('Francais clicked')
        document.getElementById('masthead-bg').style.backgroundImage = "url(/static/assets/img/bg/Francais_main.jpg)";
    }
    else if(mode == 'english') {
        console.log('English clicked')
        document.getElementById('masthead-bg').style.backgroundImage = "url(/static/assets/img/bg/england_main.jpg)";
    }
    else {
        console.log('Korean clicked')
        document.getElementById('masthead-bg').style.backgroundImage = "url(/static/assets/img/bg/seoul_main.jpg)";
    }

    localStorage.setItem('language', mode)
}