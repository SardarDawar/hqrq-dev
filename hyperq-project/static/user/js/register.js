var btnRegister = document.querySelector(".login-btn") 

var btnRegisterText = document.querySelector(".login-btn-text") 
var btnRegisterLoader = document.querySelector(".login-btn-loader") 
var btnRegisterTick = document.querySelector(".login-tick") 
var btnRegisterCross = document.querySelector(".login-cross") 

var inpEmail = document.querySelector('.input-email')
var inpEmailBox = document.querySelector('.inp-wrap.email-box')
var labelEmail = document.querySelector(".label-email")
inpEmail.value = ""

inpEmail.addEventListener('input' , listener_input_inpEmail)

ValidateEmail = function (email, bShowMsg=true) 
{
    if (/\s/.test(email) || !(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email))) 
    {
        // string contains some kind of whitespace or email structure invalid
        if (bShowMsg) showMessage('Invalid EMAIL address', 'error')
        
        return false;
    }

    return true;
}

function listener_input_inpEmail ()
{
    var errorPreviously = inpEmailBox.classList.contains('inp-error')
    if (inpEmail.value.length === 0)
    {
        if(errorPreviously) inpEmailBox.classList.remove('inp-error')
    }
    else if (ValidateEmail(inpEmail.value.trim(), false))
    {   
        if (errorPreviously)
        inpEmailBox.classList.remove('inp-error')
    }
    else if (!errorPreviously)
    {
        inpEmailBox.classList.add('inp-error')
    }
}

var inpFirstName = document.querySelector(".input-first_name") 
var inpLastName = document.querySelector(".input-last_name") 
var inpUser = document.querySelector(".input-username") 
var inpPass1 = document.querySelector('.input-password-1')
var inpPass2 = document.querySelector('.input-password-2')

var inpFirstNameBox = document.querySelector(".inp-wrap.first_name-box") 
var inpLastNameBox = document.querySelector(".inp-wrap.last_name-box") 
var inpUserBox = document.querySelector('.inp-wrap.username-box')
var inpPass1Box = document.querySelector('.inp-wrap.password-1-box')
var inpPass2Box = document.querySelector('.inp-wrap.password-2-box')

var url_register = '/register/';

inpPass2.addEventListener('input' , listener_input_inpPass12)
inpPass1.addEventListener('input' , listener_input_inpPass12)

function listener_input_inpPass12 ()
{
    var errorPreviously = inpPass2Box.classList.contains('inp-error')
    if (inpPass2.value.length === 0 || inpPass1.value.length ===0)
    {
        if(errorPreviously) inpPass2Box.classList.remove('inp-error')
    }
    else if (matchPasswords())
    {   
        if (errorPreviously)
        inpPass2Box.classList.remove('inp-error')
    }
    else if (!errorPreviously)
    {
        inpPass2Box.classList.add('inp-error')
    }
}

function matchPasswords() {
    return inpPass1.value === inpPass2.value
}

var labelFirstName = document.querySelector(".label-first_name") 
var labelLastName = document.querySelector(".label-last_name") 
var labelUser = document.querySelector(".label-username") 
var labelPass1 = document.querySelector(".label-password-1")
var labelPass2 = document.querySelector(".label-password-2") 

const MINIMUM_NAME_LENGTH = 1;
const MAXIMUM_NAME_LENGTH = 25;
const MINIMUM_PASSWORD_LENGTH = 8;
const MAXIMUM_PASSWORD_LENGTH = 45;
const MINIMUM_USERNAME_LENGTH = 3;
const MAXIMUM_USERNAME_LENGTH = 20;

btnRegister.addEventListener('click', listener_click_btnRegister);
inpFirstName.value = ""
inpLastName.value = ""
inpUser.value = ""
inpPass1.value = ""
inpPass2.value = ""

inpFirstName.addEventListener('input' , listener_input_inpFirstName)
inpLastName.addEventListener('input' , listener_input_inpLastName)
inpUser.addEventListener('input' , listener_input_inpUser)
inpPass1.addEventListener('input' , listener_input_inpPass1)

function listener_input_inpFirstName ()
{
    var errorPreviously = inpFirstNameBox.classList.contains('inp-error')
    if (inpFirstName.value.length === 0)
    {
        if(errorPreviously) inpFirstNameBox.classList.remove('inp-error')
    }
    else if (ValidateName(inpFirstName.value.trim(), false))
    {   
        if (errorPreviously)
        inpFirstNameBox.classList.remove('inp-error')
    }
    else if (!errorPreviously)
    {
        inpFirstNameBox.classList.add('inp-error')
    }
}

function listener_input_inpLastName ()
{
    var errorPreviously = inpLastNameBox.classList.contains('inp-error')
    if (inpLastName.value.length === 0)
    {
        if(errorPreviously) inpLastNameBox.classList.remove('inp-error')
    }
    else if (ValidateName(inpLastName.value.trim(), false))
    {   
        if (errorPreviously)
        inpLastNameBox.classList.remove('inp-error')
    }
    else if (!errorPreviously)
    {
        inpLastNameBox.classList.add('inp-error')
    }
}


function listener_input_inpUser ()
{
    var errorPreviously = inpUserBox.classList.contains('inp-error')
    if (inpUser.value.length === 0)
    {
        if(errorPreviously) inpUserBox.classList.remove('inp-error')
    }
    else if (ValidateUsername(inpUser.value.trim(), false))
    {   
        if (errorPreviously)
        inpUserBox.classList.remove('inp-error')
    }
    else if (!errorPreviously)
    {
        inpUserBox.classList.add('inp-error')
    }
}

function listener_input_inpPass1()
{
    var errorPreviously = inpPass1Box.classList.contains('inp-error')
    if (inpPass1.value.length === 0)
    {
        if(errorPreviously) inpPass1Box.classList.remove('inp-error')
    }
    else if (ValidatePassword(inpPass1.value, false))
    {   
        if (errorPreviously)
        inpPass1Box.classList.remove('inp-error')
    }
    else if (!errorPreviously)
    {
        inpPass1Box.classList.add('inp-error')
    }
}

ValidateName = function (username, bShowMsg=true) {
    if (username.length < MINIMUM_NAME_LENGTH || username.length > MAXIMUM_NAME_LENGTH)
    {
        if (bShowMsg) showMessage(`Name must be between ${MINIMUM_USERNAME_LENGTH} and ${MAXIMUM_USERNAME_LENGTH} characters`, 'error')
        return false;
    }
    else if (/\s/.test(username)) {
        // string contains some kind of whitespace
        if(bShowMsg) showMessage('Invalid Name String', 'error')
        return false;
    }
    // check for invalid chars

    return true;
}

ValidateUsername = function (username, bShowMsg=true) {
    if (username.length < MINIMUM_USERNAME_LENGTH || username.length > MAXIMUM_USERNAME_LENGTH)
    {
        if (bShowMsg) showMessage(`Username must be between ${MINIMUM_USERNAME_LENGTH} and ${MAXIMUM_USERNAME_LENGTH} characters`, 'error')
        return false;
    }
    else if (/\s/.test(username)) {
        // string contains some kind of whitespace
        if(bShowMsg) showMessage('Invalid Username String', 'error')
        return false;
    }
    // check for invalid chars

    return true;
}

ValidatePassword = function (password, bShowMsg=true) {
    if (password.length < MINIMUM_PASSWORD_LENGTH || password.length > MAXIMUM_PASSWORD_LENGTH)
    {
        if (bShowMsg) showMessage(`Password must be between ${MINIMUM_PASSWORD_LENGTH} and ${MAXIMUM_PASSWORD_LENGTH} characters`, 'error')
        return false;
    }

    return true;
}

function listener_click_btnRegister(e)
{
    inpFirstName.value = inpFirstName.value.trim()
    inpLastName.value = inpLastName.value.trim()
    inpUser.value = inpUser.value.trim()
    if (inpFirstName.value.length === 0 || inpLastName.value.length === 0 || inpEmail.value.length === 0 || inpUser.value.length === 0 || inpPass1.value.length === 0 || inpPass2.value.length === 0)
    {
        showMessage('Please Fill Out All Fields')
    }
    else if (!ValidateName(inpFirstName.value)) 
    {
        e.preventDefault()
        inpFirstName.focus()
        if (!inpFirstNameBox.classList.contains('inp-error')) inpFirstNameBox.classList.add('inp-error')
    }
    else if (!ValidateName(inpLastName.value)) 
    {
        e.preventDefault()
        inpLastName.focus()
        if (!inpLastNameBox.classList.contains('inp-error')) inpLastNameBox.classList.add('inp-error')
    }
    else if (!ValidateEmail(inpEmail.value)) 
    {
        e.preventDefault()
        inpEmail.focus()
        if (!inpEmailBox.classList.contains('inp-error')) inpEmailBox.classList.add('inp-error')
    }
    else if (!ValidateUsername(inpUser.value)) 
    {
        e.preventDefault()
        inpUser.focus()
        if (!inpUserBox.classList.contains('inp-error')) inpUserBox.classList.add('inp-error')
    }
    else if (!ValidatePassword(inpPass1.value)) 
    {
        e.preventDefault()
        inpPass1.focus()
        if (!inpPass1.classList.contains('inp-error')) inpPass1.classList.add('inp-error')
    }
    else if (!matchPasswords())
    {
        e.preventDefault()
        inpPass2.focus()
        if (!inpPass2.classList.contains('inp-error')) inpPass2.classList.add('inp-error')
        showMessage('Passwords do not match', 'error')
    }
    else 
    {
        e.preventDefault()
        inpFirstName.disabled = true
        inpLastName.disabled = true
        inpEmail.disabled = true
        inpUser.disabled = true
        inpPass1.disabled = true
        inpPass2.disabled = true

        btnRegister.disabled = true;
        btnRegister.classList.remove('enabled')

        labelFirstName.classList.add('label-disabled')
        labelLastName.classList.add('label-disabled')
        labelEmail.classList.add('label-disabled')
        labelUser.classList.add('label-disabled')
        labelPass1.classList.add('label-disabled')
        labelPass2.classList.add('label-disabled')

        btnRegisterLoader.hidden = false;
        btnRegisterText.hidden = true; 
        btnRegister.style.cursor = "default"

        showMessage('Please Wait')
        $.ajax({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }, 

            type: 'POST',
            url: url_register,
            data: {
                'first_name': inpFirstName.value,
                'last_name': inpLastName.value,
                'email': inpEmail.value,
                'username': inpUser.value,
                'password1': inpPass1.value,
                'password2':inpPass2.value,
            },
            success: function(data){
                handler_Register(data);
            },
            error: function(error){
                console.log(error);
                showMessage("An unknown error has occurred");
                
                inpFirstName.disabled = false;
                inpLastName.disabled = false;
                inpEmail.disabled = false;
                inpUser.disabled = false
                inpPass1.disabled = false; 
                inpPass2.disabled = false; 
                
                btnRegister.disabled = false;
                btnRegister.classList.add('enabled')
                
                labelFirstName.classList.remove('label-disabled')
                labelLastName.classList.remove('label-disabled')
                labelEmail.classList.remove('label-disabled')
                labelUser.classList.remove('label-disabled')
                labelPass1.classList.remove('label-disabled')
                labelPass2.classList.remove('label-disabled')
                
                btnRegisterLoader.hidden = true;
                btnRegisterText.hidden = false; 
                btnRegister.style.cursor = "pointer"
                
                enableRegisterButton()
            }
        });
    }
};

// const urlParams = new URLSearchParams(window.location.search);
// var url_next = '/'
// if (urlParams.has('next')) url_next = urlParams.get('next')


function handler_Register(data) 
{   
    console.log(data['message'])

    if (data['message'] === 'created')
    {
        var account = data['account']

        btnRegisterLoader.hidden = true;
        
        btnRegisterTick.style.visibility = "visible"
        $('.login-tick').hide().fadeIn(200);

        showMessage(`Account for \'${account['username']}\' successfully created. You are now being redirected to the login page.`)
        setTimeout(redirectToLogin, 1000);
    }
    else if (data['message'] === 'failure')
    {
        inpFirstName.disabled = false;
        inpLastName.disabled = false;
        inpEmail.disabled = false
        inpUser.disabled = false
        inpPass1.disabled = false
        inpPass2.disabled = false

        inpFirstName.addEventListener("input", enableRegisterButton);
        inpLastName.addEventListener("input", enableRegisterButton);
        inpEmail.addEventListener("input", enableRegisterButton);
        inpUser.addEventListener("input", enableRegisterButton);
        inpPass1.addEventListener("input", enableRegisterButton);
        inpPass2.addEventListener("input", enableRegisterButton);

        labelFirstName.classList.remove('label-disabled')
        labelLastName.classList.remove('label-disabled')
        labelEmail.classList.remove('label-disabled')
        labelUser.classList.remove('label-disabled')
        labelPass1.classList.remove('label-disabled')
        labelPass2.classList.remove('label-disabled')

        btnRegisterLoader.hidden = true;

        // show cross sign on login button until change/input
        btnRegisterCross.style.visibility = "visible"
        $('.login-cross').hide().fadeIn(200);

        showMessage(data['error_message'])
        if (data['error_field'] === 'email') inpEmailBox.classList.add('inp-error');
        else if (data['error_field'] === 'username') inpUserBox.classList.add('inp-error');
        else if (data['error_field'] === 'password1') inpPass1Box.classList.add('inp-error');
        else if (data['error_field'] === 'password2') inpPass2Box.classList.add('inp-error');
        else if (data['error_field'] === 'first_name') inpFirstNameBox.classList.add('inp-error');
        else if (data['error_field'] === 'last_name') inpLastNameBox.classList.add('inp-error');
    }
}

function enableRegisterButton(rmvEvntLstnr = true) {
    btnRegister.disabled = false;
    btnRegister.classList.add('enabled')
    btnRegister.style.cursor = "pointer"

    if (rmvEvntLstnr)
    {
        inpFirstName.removeEventListener("input", enableRegisterButton);
        inpLastName.removeEventListener("input", enableRegisterButton);
        inpEmail.removeEventListener("input", enableRegisterButton);
        inpUser.removeEventListener("input", enableRegisterButton);
        inpPass1.removeEventListener("input", enableRegisterButton);
        inpPass2.removeEventListener("input", enableRegisterButton);
    }

    btnRegisterCross.style.visibility = "hidden"
    btnRegisterText.hidden = false
}

var messageBox = document.querySelector('.message-box') 

function redirectToUrl(url="/") {
    window.location.replace(url);
}

var url_login = "/login/"

function redirectToLogin() {
    if (url_next) {
        window.location.replace(`${url_login}?next=${url_next}`);
    } else {
        window.location.replace(url_login);
    }
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