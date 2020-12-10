
var speech_voices = null;
var speech_state = false;
var speech_voice_inx = null;
const speech_voice_lang = "en-US";


setTimeout(() => {
    speech_voices = window.speechSynthesis.getVoices();
}, 50);

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
        speech_state = true;
        utterThis.onend = () => {
            speech_state = false;
        }
        window.speechSynthesis.speak(utterThis);
    }
};

const start_beep = document.getElementById("beep");

function VoiceToText(field, callback) {
    if (!field && !callback) return;

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
        const speech_cased = toTitleCase(speech)
        recognition.stop();
        if (field) $(field).val(speech_cased);
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