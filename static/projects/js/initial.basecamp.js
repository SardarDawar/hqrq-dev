// ####################################
//
// page 0
//
// ####################################


const btnCreateProject = document.getElementById("create_new_project");
const btnNext_UpdateProject = document.getElementById("btn_next_updproj");

btnCreateProject.onclick = () => {
    disable_btnOpt(btnCreateProject)
    pageCleanup();
    window.location.href = url_projCreate
}

// form logic

const form_projectUpdate = document.getElementById("project_update_form");


btnNext_UpdateProject.onclick = () => {
    pageCleanup();
    form_projectUpdate.submit();
}

// form logic end


// initially
var curr_page_sel = '.page-wrap.pg1-wrap'

setRightSidebarSecondaryContent(curr_page_sel, pg1_sdbrR_header, pg1_sdbrR_content, null, true, true)
setRightSidebarContent(pg1_sdbrR_header, pg1_sdbrR_content, null, true, true)


fixMainWinHeightImmediate(curr_page_sel);

window.onresize = () => {
    fixMainWinHeightImmediate(curr_page_sel);
}

const basecampMic = document.getElementById("basecamp-mic");

// basecamp editable fields
var befs = document.querySelectorAll(".basecamp-text .editable")

const btn_contentEdit = document.getElementById("contentEditButton")
const contentEditOptions = document.getElementById("contentEditOptions")
const btn_contentEdit_done = contentEditOptions.querySelector("#contentEditOption-done")
const btn_contentEdit_cancel = contentEditOptions.querySelector("#contentEditOption-cancel")

const basecampTextDiv = document.querySelector(".basecamp-text")
const $basecampTextDiv = $(basecampTextDiv)

function ValidateResponseInputs(break_on_error) {
    var error = false;
    for(var i=0; i<befs.length; i++) {
        const el = befs[i]  
        const pname = el.getAttribute("pname")
        const inpID = `inp-bef-${pname}`
        const inp = document.getElementById(inpID)  
        if (inp) {
            const value = inp.innerHTML.trim()
            if (!value || value.length === 0) { 
                if (!inp.classList.contains("is-invalid")) inp.classList.add("is-invalid")
                error = true;
                if (break_on_error) return error;
            } else {
                if (inp.classList.contains("is-invalid")) inp.classList.remove("is-invalid")
            }
        }
    }
    if (error) {
        if (!btn_contentEdit_done.classList.contains("disabled")) btn_contentEdit_done.classList.add("disabled")
    } else {
        if (btn_contentEdit_done.classList.contains("disabled")) btn_contentEdit_done.classList.remove("disabled")
    }
    return error;
}

function initResponseFields() {
    var first = true;
    befs = document.querySelectorAll(".basecamp-text .editable")
    unsetMicActiveVoiceToTextField(basecampMic)
    befs.forEach(el => {    
        if (!el.querySelector(".input-bef")) {
            const pname = el.getAttribute("pname")
            const pvalue = el.getAttribute("pvalue")
            const evalue = el.getAttribute("evalue")
            const tvalue = el.getAttribute("tvalue")
            const inpID = `inp-bef-${pname}`    
            el.innerHTML = `
                <span class="input-bef form-control" id="${inpID}" role="textbox" name="${pname}" contenteditable>${evalue}</span>
            `
            const inp = document.getElementById(inpID)
            el.classList.add('editing')
            inp.addEventListener('keydown' , (e) => {
                if (e.key === "Enter") {
                    e.preventDefault();
                }
            })
            inp.addEventListener('keyup' , (e) => {
                if (e.key === "Enter") {
                    e.preventDefault();
                }
            })
            inp.addEventListener("input", (e)=>{
                ValidateResponseInputs();
            })
            inp.addEventListener("focus", (e)=>{
                setMicActiveVoiceToTextField(basecampMic, inp)
            })
            if (first) {
                inp.focus()
                moveCursorToEndOfContenteditable(inp)
                first = false
            }
        }
    })  
    if (!btn_contentEdit_done.classList.contains("disabled")) btn_contentEdit_done.classList.add("disabled")
    if (btn_contentEdit_cancel.classList.contains("disabled")) btn_contentEdit_cancel.classList.remove("disabled")
    if (!basecampTextDiv.classList.contains("bscmp-editing")) basecampTextDiv.classList.add("bscmp-editing")
    $(btn_contentEdit).hide()
    $(contentEditOptions).show()
}

btn_contentEdit.onclick = initResponseFields

editCancel = () => {
    befs.forEach(el => {  
        const pname = el.getAttribute("pname")
        const pvalue = el.getAttribute("pvalue")
        const evalue = el.getAttribute("evalue")
        const tvalue = el.getAttribute("tvalue")
        el.innerHTML = tvalue
        el.classList.remove('editing')
    })
    $(contentEditOptions).hide()
    $(btn_contentEdit).show()
    if (basecampTextDiv.classList.contains("disabled")) basecampTextDiv.classList.remove("disabled")
    if (basecampTextDiv.classList.contains("bscmp-editing")) basecampTextDiv.classList.remove("bscmp-editing")
}

editSubmit = () => {
    if (ValidateResponseInputs(true)) {
        if (!btn_contentEdit_done.classList.contains("disabled")) btn_contentEdit_done.classList.add("disabled")
        return;
    }

    if (!btn_contentEdit_done.classList.contains("disabled")) btn_contentEdit_done.classList.add("disabled")
    if (!btn_contentEdit_cancel.classList.contains("disabled")) btn_contentEdit_cancel.classList.add("disabled")
    if (!basecampTextDiv.classList.contains("disabled")) basecampTextDiv.classList.add("disabled")

    // collect all responses
    var responses = {}
    befs.forEach(el => { 
        const pname = el.getAttribute("pname")
        const pvalue = el.getAttribute("pvalue")
        const evalue = el.getAttribute("evalue")
        const tvalue = el.getAttribute("tvalue")
        const inpID = `inp-bef-${pname}`
        const inp = document.getElementById(inpID)  
        if (inp) {
            const value = inp.innerHTML.trim()
            responses[`${pname}`] = value;
        }
    })  
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }, 

        type: 'POST',
        url: url_update_responses_exp,
        data: {
            'project_id': project_id,
            'responses': JSON.stringify(responses),
        },
        success: function(data){
            if (data['updated']) {
                const responses_text = data["responses_text"]
                $basecampTextDiv.stop().fadeOut(300, ()=> {
                    $basecampTextDiv.html(responses_text)
                    $basecampTextDiv.fadeIn(300)
                    if (basecampTextDiv.classList.contains("disabled")) basecampTextDiv.classList.remove("disabled")
                    if (basecampTextDiv.classList.contains("bscmp-editing")) basecampTextDiv.classList.remove("bscmp-editing")
                    $(contentEditOptions).hide()
                    $(btn_contentEdit).show()
                })

            } else {
                // show error message
                showMessage(data["message"], 'error')
                editCancel();
            }
        },
        error: function(error){
            console.log(error);
            // show error message
            showMessage("An unknown error has occurred", 'error')
            editCancel();
        }
    });
}

btn_contentEdit_cancel.onclick = editCancel
btn_contentEdit_done.onclick = editSubmit


const message_text_title = `Error\
        <svg aria-hidden="true" width="33px" focusable="false" data-prefix="fad" data-icon="exclamation-circle" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="svg-inline--fa fa-exclamation-circle fa-w-16 fa-9x"><g class="fa-group"><path fill="currentColor" d="M256 8C119 8 8 119.08 8 256s111 248 248 248 248-111 248-248S393 8 256 8zm0 376a32 32 0 1 1 32-32 32 32 0 0 1-32 32zm38.24-238.41l-12.8 128A16 16 0 0 1 265.52 288h-19a16 16 0 0 1-15.92-14.41l-12.8-128A16 16 0 0 1 233.68 128h44.64a16 16 0 0 1 15.92 17.59z" class="fa-secondary"></path><path fill="currentColor" d="M278.32 128h-44.64a16 16 0 0 0-15.92 17.59l12.8 128A16 16 0 0 0 246.48 288h19a16 16 0 0 0 15.92-14.41l12.8-128A16 16 0 0 0 278.32 128zM256 320a32 32 0 1 0 32 32 32 32 0 0 0-32-32z" class="fa-primary"></path></g></svg>
    `;        
const message_text_subtitle = "";
function showMessage(message, type)
{
    showInfoModal_info(message_text_title, message_text_subtitle, message, 'none')
}


// voice to text init
accessibility_initMicsActiveVoiceToFieldText();
setVoiceToText_FieldType('contenteditable');
setVoiceToTextFieldCallback(ValidateResponseInputs)