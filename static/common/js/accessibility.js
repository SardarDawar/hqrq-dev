const accSpeakers = document.querySelectorAll(".accessibility .acc-speak")
var voiceToTextFieldCallback = null;

setVoiceToTextFieldCallback = (func) => {
    voiceToTextFieldCallback = func;
}

// $(document).ready(function(){
// $.each($("div#pg1-acc-speak-field"), function(){
//         console.debug($(this));
//     });
// });

accSpeakers.forEach(el => {
    const field = document.getElementById(el.dataset.fieldid);
    var textRead = ""

    el.onclick = () => {
        // if (field.hasAttribute("value")) TextToVoice(textRead, true);
        // else TextToVoice(field.innerHTML, true);        
        // $.each($("div#pg1-acc-speak-field, span#pg2-change-question"), function(){
        //     textRead = ""
        //     if($(this).attr("value")){
        //         textRead = $(this).attr("value");
        //     }
        //     // new SpeechSynthesisUtterance object
                

        let utter = new SpeechSynthesisUtterance();
        utter.lang = 'en-US';
        utter.text = $("div#pg1-acc-speak-field").attr("value");
        utter.volume = 1;
        window.speechSynthesis.speak(utter);

        // Second
        utter = new SpeechSynthesisUtterance();
        utter.lang = 'en-US';
        utter.text = $("span#pg2-change-question").html().trim();
        utter.volume = 1;
        window.speechSynthesis.speak(utter);

        // Third
        utter = new SpeechSynthesisUtterance();
        utter.lang = 'en-US';
        utter.text = $("div#pg2-change-questionlead").html().trim();
        utter.volume = 1;
        
        window.speechSynthesis.speak(utter);

        }





        
});





// const accMics = document.querySelectorAll(".accessibility .acc-mic")
const accMics = new Set([
    ...document.querySelectorAll(".accessibility .acc-mic"),
    ...document.querySelectorAll(".acsblty.acc-mic")
])

accMics.forEach(el => {

    if (el.hasAttribute("voiceselect")) {
        const options = document.querySelectorAll(`.${el.dataset.fieldsclass}`);
        const forcesel = el.hasAttribute("forcesel");
        el.onclick = () => {
            VoiceToText(null, (speech) => {
                for (var o=0; o<options.length; o++)
                {
                    const opt = options[o];
                    const text = opt.querySelector(`.${el.dataset.textsclass}`).innerHTML.toLowerCase()
                    const speech_split = speech.toLowerCase().split(" ");
                    var contains_all_words = true
                    for (var i=0; i<speech_split.length; i++) {
                        if (!text.includes(speech_split[i])) {
                            contains_all_words = false
                            break;
                        }
                    }
                    if (contains_all_words) {
                        if (forcesel)
                        {
                            options.forEach(lo => {
                                if (opt !== lo && lo.classList.contains("sel")) lo.classList.remove("sel")
                            })                        
                            if (!opt.classList.contains("sel")) opt.classList.add('sel')
                            else opt.classList.remove("sel")
                        }
                        opt.click();
                        opt.focus()
                        break;
                    }
                }
            });        
        }
    } else {
        const field = document.getElementById(el.dataset.fieldid);
        var textcase = null;
        if (field && field.hasAttribute("textcase")) textcase = field.getAttribute("textcase")
        if (field) {
            el.onclick = () => {
                VoiceToText(field, voiceToTextFieldCallback, textcase);        
            }
        }
    }
});


accessibility_initMicsActiveVoiceToFieldText = () => {
    accMics.forEach(el => {
        el.onclick = null;
        el.onclick = () => {
            const field = document.getElementById(el.dataset.fieldid);
            var textcase = null;
            if (field && field.hasAttribute("textcase")) textcase = field.getAttribute("textcase")
            if (field) {
                field.focus()
                moveCursorToEndOfInput(field) 
                VoiceToText(field, voiceToTextFieldCallback, textcase);
            }        
        }
    });
}

unsetMicActiveVoiceToTextField = (mic_el) => {
    if (mic_el.hasAttribute("data-fieldid")) mic_el.removeAttribute("data-fieldid")
}

setMicActiveVoiceToTextField = (mic_el, field, textcase) => {
    mic_el.setAttribute("data-fieldid", `${field.id}`)
    if (textcase) mic_el.setAttribute("textcase", `${textcase}`)
}

const accHelps = document.querySelectorAll(".accessibility .acc-help")

accHelps.forEach(el => {
    if (el.hasAttribute("data-helptext")) {
        const help_text = el.dataset.helptext;
        var help_text_title = `Tip\
                <svg aria-hidden="true" width="33px" focusable="false" data-prefix="fad" data-icon="question-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="svg-inline--fa fa-question-circle fa-w-16 fa-9x"><g class="fa-group"><path fill="currentColor" d="M256 8C119 8 8 119.08 8 256s111 248 248 248 248-111 248-248S393 8 256 8zm0 422a46 46 0 1 1 46-46 46.05 46.05 0 0 1-46 46zm40-131.33V300a12 12 0 0 1-12 12h-56a12 12 0 0 1-12-12v-4c0-41.06 31.13-57.47 54.65-70.66 20.17-11.31 32.54-19 32.54-34 0-19.82-25.27-33-45.7-33-27.19 0-39.44 13.14-57.3 35.79a12 12 0 0 1-16.67 2.13L148.82 170a12 12 0 0 1-2.71-16.26C173.4 113 208.16 90 262.66 90c56.34 0 116.53 44 116.53 102 0 77-83.19 78.21-83.19 106.67z" class="fa-secondary"></path><path fill="currentColor" d="M256 338a46 46 0 1 0 46 46 46 46 0 0 0-46-46zm6.66-248c-54.5 0-89.26 23-116.55 63.76a12 12 0 0 0 2.71 16.24l34.7 26.31a12 12 0 0 0 16.67-2.13c17.86-22.65 30.11-35.79 57.3-35.79 20.43 0 45.7 13.14 45.7 33 0 15-12.37 22.66-32.54 34C247.13 238.53 216 254.94 216 296v4a12 12 0 0 0 12 12h56a12 12 0 0 0 12-12v-1.33c0-28.46 83.19-29.67 83.19-106.67 0-58-60.19-102-116.53-102z" class="fa-primary"></path></g></svg>
        `;        
        var help_text_subtitle = "";
        if (el.hasAttribute("data-helptexttitle")) help_text_title =  el.dataset.helptexttitle;
        if (el.hasAttribute("data-helptextsubtitle")) help_text_subtitle =  el.dataset.helptextsubtitle;
        el.onclick = () => {
            showInfoModal_info(help_text_title, help_text_subtitle, help_text, 'none') 
        }
    }
});