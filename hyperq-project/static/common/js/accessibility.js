const accSpeakers = document.querySelectorAll(".accessibility .acc-speak")
var voiceToTextFieldCallback = null;

setVoiceToTextFieldCallback = (func) => {
    voiceToTextFieldCallback = func;
}

accSpeakers.forEach(el => {
    const field = document.getElementById(el.dataset.fieldid);
    el.onclick = () => {
        if (field.hasAttribute("value")) TextToVoice(field.getAttribute("value"), true);
        else TextToVoice(field.innerHTML, true);        
    }
});

const accMics = document.querySelectorAll(".accessibility .acc-mic")

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
        el.onclick = () => {
            VoiceToText(field, voiceToTextFieldCallback, textcase);        
        }
    }
});