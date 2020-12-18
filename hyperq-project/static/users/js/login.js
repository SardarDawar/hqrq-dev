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
        showMessage('Invalid EMAIL address', 'error', true)
        
        return false;
    }

    return true;
}

ValidatePassword = function (password) {
    if (password.length < MINIMUM_PASSWORD_LENGTH || password.length > MAXIMUM_PASSWORD_LENGTH)
    {
        showMessage(`Password must be between ${MINIMUM_PASSWORD_LENGTH} and ${MAXIMUM_PASSWORD_LENGTH} characters`, 'error', true)
        return false;
    }

    return true;
}

function listener_click_btnLogin(e)
{
    inpEmail.value = inpEmail.value.trim()
    if (inpEmail.value.length === 0 || inpPass.value.length === 0)
    {
        showMessage('Please Fill Out Both Fields', 'error', true)
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

        showMessage('Please Wait', 'info')
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
                showMessage("An unknown error has occurred", 'error', true);
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

function handler_Login(data) 
{   
    console.log(data['message'])

    if (data['message'] === 'success')
    {
        btnLoginLoader.hidden = true;
        
        btnLoginTick.style.visibility = "visible"
        $('.login-tick').hide().fadeIn(200);

        showMessage('You will be redirected soon', 'success')
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

        showMessage('Incorrect Username or Password', 'error', true)
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

var messageBoxTransitioning = false;
const message_text_title = `Error\
        <svg aria-hidden="true" width="33px" focusable="false" data-prefix="fad" data-icon="exclamation-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="error svg-inline--fa fa-exclamation-circle fa-w-16 fa-9x"><g class="fa-group"><path fill="currentColor" d="M256 8C119 8 8 119.08 8 256s111 248 248 248 248-111 248-248S393 8 256 8zm0 376a32 32 0 1 1 32-32 32 32 0 0 1-32 32zm38.24-238.41l-12.8 128A16 16 0 0 1 265.52 288h-19a16 16 0 0 1-15.92-14.41l-12.8-128A16 16 0 0 1 233.68 128h44.64a16 16 0 0 1 15.92 17.59z" class="fa-secondary"></path><path fill="currentColor" d="M278.32 128h-44.64a16 16 0 0 0-15.92 17.59l12.8 128A16 16 0 0 0 246.48 288h19a16 16 0 0 0 15.92-14.41l12.8-128A16 16 0 0 0 278.32 128zM256 320a32 32 0 1 0 32 32 32 32 0 0 0-32-32z" class="fa-primary"></path></g></svg>
    `;        
const message_text_subtitle = "";
function showMessage(message, type, show_modal)
{
    if (show_modal) {
        showInfoModal_info(message_text_title, message_text_subtitle, message, type) 
    }

    if (message.trim() === messageBox.innerHTML.trim()) return;
    if (messageBoxTransitioning) setTimeout(() => {
        showMessage(message, type);
    }, 200)
    else {
        setMessageBoxTextType(type)
        messageBox.innerHTML = message
        messageBoxTransitioning = true;
        $(messageBox).hide().fadeIn(200, ()=>{
            messageBoxTransitioning = false;
        });
    }
}

setMessageBoxTextType = (type) => {
    if (type === 'info') {
        $(messageBox).attr("class", "message-box text-muted")
    } else if (type === 'error') {
        $(messageBox).attr("class", "message-box text-danger")
    } else if (type === 'success') {
        $(messageBox).attr("class", "message-box text-success")
    } else {
        $(messageBox).attr("class", "message-box text-muted")
    }
}