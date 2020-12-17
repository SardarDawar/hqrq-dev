var btnLogin = document.querySelector(".login-btn") 

var btnLoginText = document.querySelector(".login-btn-text") 
var btnLoginLoader = document.querySelector(".login-btn-loader") 
var btnLoginTick = document.querySelector(".login-tick") 
var btnLoginCross = document.querySelector(".login-cross") 

var inpEmail = document.querySelector('.input-email')
var inpPass = document.querySelector(".input-password") 
var url_login = '/login/';

var labelEmail = document.querySelector(".label-email")
var labelPass = document.querySelector(".label-password") 

const MINIMUM_PASSWORD_LENGTH = 8;
const MAXIMUM_PASSWORD_LENGTH = 45;

btnLogin.addEventListener('click', listener_click_btnLogin);
inpEmail.value = ""
inpPass.value = ""

ValidateEmail = function (email) 
{
    if (/\s/.test(email) || !(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email))) 
    {
        // string contains some kind of whitespace or email structure invalid
        showMessage('Invalid EMAIL address')
        
        return false;
    }

    return true;
}

ValidatePassword = function (password) {
    if (password.length < MINIMUM_PASSWORD_LENGTH || password.length > MAXIMUM_PASSWORD_LENGTH)
    {
        showMessage(`Password must be between ${MINIMUM_PASSWORD_LENGTH} and ${MAXIMUM_PASSWORD_LENGTH} characters`)
        return false;
    }

    return true;
}

function listener_click_btnLogin(e)
{
    inpEmail.value = inpEmail.value.trim()
    if (inpEmail.value.length === 0 || inpPass.value.length === 0)
    {
        showMessage('Please Fill Out Both Fields')
    }
    else if (!ValidateEmail(inpEmail.value)) 
    {
        e.preventDefault()
        inpEmail.focus()
    }
    else if (!ValidatePassword(inpPass.value)) 
    {
        e.preventDefault()
        inpPass.focus()
    }
    else 
    {
        e.preventDefault()
        inpEmail.disabled = true
        inpPass.disabled = true

        btnLogin.disabled = true;
        btnLogin.classList.remove('enabled')

        labelEmail.classList.add('label-disabled')
        labelPass.classList.add('label-disabled')

        btnLoginLoader.hidden = false;
        btnLoginText.hidden = true; 
        btnLogin.style.cursor = "default"

        showMessage('Please Wait')
        $.ajax({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }, 

            type: 'POST',
            url: url_login,
            data: {
                'email': inpEmail.value,
                'password': inpPass.value
            },
            success: function(data){
                handler_Login(data);
            },
            error: function(error){
                console.log(error);
                showMessage("An unknown error has occurred");
                inpEmail.disabled = false
                inpPass.disabled = false
        
                btnLogin.disabled = false;
                btnLogin.classList.add('enabled')
        
                labelEmail.classList.remove('label-disabled')
                labelPass.classList.remove('label-disabled')
        
                btnLoginLoader.hidden = true;
                btnLoginText.hidden = false; 
                btnLogin.style.cursor = "pointer"
        
            }
        });
    }
};

// const urlParams = new URLSearchParams(window.location.search);
// var url_next = '/'
// if (urlParams.has('next')) url_next = urlParams.get('next')


function handler_Login(data) 
{   
    console.log(data['message'])

    if (data['message'] === 'success')
    {
        btnLoginLoader.hidden = true;
        
        btnLoginTick.style.visibility = "visible"
        $('.login-tick').hide().fadeIn(200);

        showMessage('You will be redirected soon')
        setTimeout(() => {
            redirectToUrl(url_next);
        }, 1000);
    }
    else if (data['message'] === 'failure')
    {
        inpEmail.disabled = false
        inpPass.disabled = false

        inpEmail.addEventListener("input", enableLoginButton);
        inpPass.addEventListener("input", enableLoginButton);


        labelEmail.classList.remove('label-disabled')
        labelPass.classList.remove('label-disabled')

        btnLoginLoader.hidden = true;

        // show cross sign on login button until change/input
        btnLoginCross.style.visibility = "visible"
        $('.login-cross').hide().fadeIn(200);

        showMessage('Incorrect Username or Password')
    }
}

function enableLoginButton() {
    btnLogin.disabled = false;
    btnLogin.classList.add('enabled')
    btnLogin.style.cursor = "pointer"

    inpEmail.removeEventListener("input", enableLoginButton);
    inpPass.removeEventListener("input", enableLoginButton);

    btnLoginCross.style.visibility = "hidden"
    btnLoginText.hidden = false
}

var messageBox = document.querySelector('.message-box') 

function redirectToUrl(url="/") {
    window.location.replace(url);
}

var messageBoxTransitionaing = false;
function showMessage(message)
{
    if (message.trim() === messageBox.innerHTML.trim()) return;
    if (messageBoxTransitionaing) setTimeout(() => {
        showMessage(message);
    }, 200)
    else {
        messageBox.innerHTML = message
        messageBoxTransitionaing = true;
        $(messageBox).hide().fadeIn(200, ()=>{
            messageBoxTransitionaing = false;
        });
    }
}