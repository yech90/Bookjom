
/* --------------------
    Color thema change
 -------------------- */
$(document).ready(function() {
    //set theme on cookie
     let theme = localStorage.getItem('theme')
    if(theme==null){
        setTheme('yellow')
    }
    else {
        setTheme(theme)
    }


 })



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

    localStorage.setItem('theme', mode)
}

/*
$("#sendMessageButton").on('submit', function(event) {
    console.log("sendMailToYech !!")
    alert("Thank you for your contact, i will come back to you soon !");
});
*/
let returnFromSendMail = document.getElementById('sendMessageButton')
returnFromSendMail.addEventListener('click', function() {
    console.log("sendMailToYech !!")
    alert("Thank you for your contact, i will come back to you soon !");
})


/* --------------------
    Language change
 -------------------- */
/*
let languageSelect = document.getElementsByClassName('language-set')

for (var i=0; languageSelect.length > i; i++) {
    languageSelect[i].addEventListener('click', function() {
        let lang = this.dataset.lang
        console.log('Language clicked:',lang)
        setLanguage(lang)
    })
}

function setLanguage(lang) {
    if(lang == 'francais') {
        console.log('Francais clicked')
        //document.getElementById('masthead-bg').style.backgroundImage = "url(/static/assets/img/bg/Francais_main.jpg)";
    }
     if(lang == 'english') {
        console.log('English clicked')
        //document.getElementById('masthead-bg').style.backgroundImage = "url(/static/assets/img/bg/england_main.jpg)";
    }
    if(lang == 'korean'){
        console.log('Korean clicked')
        //document.getElementById('masthead-bg').style.backgroundImage = "url(/static/assets/img/bg/seoul_main.jpg)";
    }

    localStorage.setItem('language', lang)
}
*/



