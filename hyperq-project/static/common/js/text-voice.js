
var speech_voices = null;
var speech_state = false;
var speech_voice_inx = null;
const speech_voice_lang = "en-US";
const VOICE_TEXT_CASE_TITLE = "TITLE_CASE"
const VOICE_TEXT_CASE_UPPER = "UPPER_CASE"
const VOICE_TEXT_CASE_LOWER = "LOWER_CASE"
const VOICE_TEXT_CASE_STANDARD = "STAND_CASE"

setTimeout(() => {
    speech_voices = window.speechSynthesis.getVoices();
}, 50);

var speechTimeout;
function speechTimer() {
    window.speechSynthesis.pause();
    window.speechSynthesis.resume();
    speechTimeout = setTimeout(speechTimer, 10000);
}

if(window.speechSynthesis.onvoiceschanged !== undefined)
{
    window.speechSynthesis.onvoiceschanged = () => {
        speech_voices = window.speechSynthesis.getVoices();
        if (speech_voices)
        {
            for(var i=0; i<speech_voices.length; i++)
            {
                if(speech_voices[i].lang === speech_voice_lang) speech_voice_inx = i;
            }
        }
    }
}

function toTitleCase(str) {
    return str.replace(/\w\S*/g, function(txt) {
        return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    });
};

function TextToVoice(text) {
    if (!text) return;

    var utterThis = new SpeechSynthesisUtterance(text);
    if (speech_voices && speech_voice_inx)
    {
        utterThis.voice = speech_voices[speech_voice_inx];
    }
    utterThis.lang = "en-US";
    utterThis.rate = 0.85;
    // utterThis.pitch = 0.5;
    if (!speech_state)
    {
        speechTimeout = setTimeout(speechTimer, 10000);
        speech_state = true;
        utterThis.onend = () => {
            speech_state = false;
            if (speechTimeout) clearTimeout(speechTimeout);
        }
        console.log(utterThis)
        window.speechSynthesis.speak(utterThis);
    }
    else {
        window.speechSynthesis.cancel();
        if (speechTimeout) clearTimeout(speechTimeout);
    }
};

function textVoiceCleanup() {
    window.speechSynthesis.cancel();
    if (speechTimeout) clearTimeout(speechTimeout); 
}

const start_beep = document.getElementById("beep");

var voiceToText_FieldType = 'input'

setVoiceToText_FieldType = (type) => {
    if (type === 'input' || type === 'contenteditable') {
        voiceToText_FieldType = type
    }
}

function VoiceToText(field, callback, text_case) {

    if (!text_case) text_case = VOICE_TEXT_CASE_STANDARD;

    if (!field && !callback) return;

    if (field) {
        field.focus()
        if (voiceToText_FieldType === 'contenteditable') {
            moveCursorToEndOfContenteditable(field)
        } else {
            moveCursorToEndOfInput(field);
        }
    }

    if (window.hasOwnProperty("webkitSpeechRecognition")) {
        var recognition = new window.webkitSpeechRecognition();
    }
    if (window.hasOwnProperty("SpeechRecognition")) {
        var recognition = new window.SpeechRecognition();
    }
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = "en-US";
    recognition.onstart = function() {
        start_beep.play();
    }
    recognition.onresult = function(event) {
        const speech = ""+event.results[0][0].transcript;
        var speech_cased = speech;
        
        if (text_case===VOICE_TEXT_CASE_TITLE) speech_cased = toTitleCase(speech)
        else if (text_case===VOICE_TEXT_CASE_UPPER) speech_cased = speech.toUpperCase();
        else if (text_case===VOICE_TEXT_CASE_LOWER) speech_cased = speech.toLowerCase();
        
        recognition.stop();
        if (field) {
            if (voiceToText_FieldType === 'contenteditable') {
                if (!field.innerHTML) field.innerHTML = speech_cased.trim()
                else field.innerHTML = `${field.innerHTML} ${speech_cased.trim()}`
                moveCursorToEndOfContenteditable(field)
            } else {
                $(field).val(()=> {
                    if (!field.value) return speech_cased.trim()
                    else return `${field.value.trim()} ${speech_cased.trim()}`;
                });
                moveCursorToEndOfInput(field);
            }
        }
        if (callback) callback(speech);
    }
    recognition.onerror = function(event) {
        const err_msg = ""+event.error;
        console.log(err_msg)
        recognition.stop();
    }
    recognition.onend = function() {
        start_beep.play();
    }
    recognition.start();
};



var speechUtteranceChunker = function (utt, settings, callback) {
    settings = settings || {};
    var newUtt;
    var txt = (settings && settings.offset !== undefined ? utt.text.substring(settings.offset) : utt.text);
    if (utt.voice && utt.voice.voiceURI === 'native') { // Not part of the spec
        newUtt = utt;
        newUtt.text = txt;
        newUtt.addEventListener('end', function () {
            if (speechUtteranceChunker.cancel) {
                speechUtteranceChunker.cancel = false;
            }
            if (callback !== undefined) {
                callback();
            }
        });
    }
    else {
        var chunkLength = (settings && settings.chunkLength) || 160;
        var pattRegex = new RegExp('^[\\s\\S]{' + Math.floor(chunkLength / 2) + ',' + chunkLength + '}[.!?,]{1}|^[\\s\\S]{1,' + chunkLength + '}$|^[\\s\\S]{1,' + chunkLength + '} ');
        var chunkArr = txt.match(pattRegex);

        if (chunkArr[0] === undefined || chunkArr[0].length <= 2) {
            //call once all text has been spoken...
            if (callback !== undefined) {
                callback();
            }
            return;
        }
        var chunk = chunkArr[0];
        newUtt = new SpeechSynthesisUtterance(chunk);
        var x;
        for (x in utt) {
            if (utt.hasOwnProperty(x) && x !== 'text') {
                newUtt[x] = utt[x];
            }
        }
        newUtt.addEventListener('end', function () {
            if (speechUtteranceChunker.cancel) {
                speechUtteranceChunker.cancel = false;
                return;
            }
            settings.offset = settings.offset || 0;
            settings.offset += chunk.length - 1;
            speechUtteranceChunker(utt, settings, callback);
        });
    }

    if (settings.modifier) {
        settings.modifier(newUtt);
    }
    console.log(newUtt); //IMPORTANT!! Do not remove: Logging the object out fixes some onend firing issues.
    //placing the speak invocation inside a callback fixes ordering and onend issues.
    setTimeout(function () {
        speechSynthesis.speak(newUtt);
    }, 0);
};