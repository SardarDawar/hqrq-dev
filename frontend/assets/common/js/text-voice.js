
var speach_voices = null;
var speach_state = false;
var speach_voice_inx = null;
const speach_voice_lang = "en-US";


setTimeout(() => {
    speach_voices = window.speechSynthesis.getVoices();
}, 50);

if(window.speechSynthesis.onvoiceschanged !== undefined)
{
    window.speechSynthesis.onvoiceschanged = () => {
        speach_voices = window.speechSynthesis.getVoices();
        if (speach_voices)
        {
            for(var i=0; i<speach_voices.length; i++)
            {
                if(speach_voices[i].lang === speach_voice_lang) speach_voice_inx = i;
            }
        }
    }
}

function TextToVoice(text) {
    var utterThis = new SpeechSynthesisUtterance(text);
    if (speach_voices && speach_voice_inx)
    {
        utterThis.voice = speach_voices[speach_voice_inx];
    }
    utterThis.lang = "en-US";
    utterThis.rate = 0.85;
    // utterThis.pitch = 0.5;
    if (!speach_state)
    {
        speach_state = true;
        utterThis.onend = () => {
            speach_state = false;
        }
        window.speechSynthesis.speak(utterThis);
    }
};


function VoiceToText(field) {
    var start_beep = document.getElementById("beep");
    if (window.hasOwnProperty("webkitSpeechRecognition")) {
        var recognition = new window.webkitSpeechRecognition();
    }
    if (window.hasOwnProperty("SpeechRecognition")) {
        var recognition = new window.SpeechRecognition();
    }
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = "en-US";
    recognition.start();
    recognition.onstart = function() {
        start_beep.play();
    }
    recognition.onresult = function(event) {
        var speech = ""+event.results[0][0].transcript;
        var user_name = toTitleCase(speech)
        $(field).val(user_name);
        recognition.stop();
    }
    recognition.onerror = function(event) {
        var err_msg = ""+event.error;
        $(field).val(err_msg);
        recognition.stop();
    }
    recognition.onend = function() {
        start_beep.play();
    }
};