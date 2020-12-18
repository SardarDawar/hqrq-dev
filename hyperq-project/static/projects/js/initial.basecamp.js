// ####################################
//
// page 0
//
// ####################################

function moveCursorToEndOfContenteditable(contentEditableElement)
{
    var range,selection;
    if(document.createRange)//Firefox, Chrome, Opera, Safari, IE 9+
    {
        range = document.createRange();//Create a range (a range is a like the selection but invisible)
        range.selectNodeContents(contentEditableElement);//Select the entire contents of the element with the range
        range.collapse(false);//collapse the range to the end point. false means collapse to end rather than the start
        selection = window.getSelection();//get the selection object (allows you to change selection)
        selection.removeAllRanges();//remove any selections already made
        selection.addRange(range);//make the range you have just created the visible selection
    }
    else if(document.selection)//IE 8 and lower
    { 
        range = document.body.createTextRange();//Create a range (a range is a like the selection but invisible)
        range.moveToElementText(contentEditableElement);//Select the entire contents of the element with the range
        range.collapse(false);//collapse the range to the end point. false means collapse to end rather than the start
        range.select();//Select the range (make it the visible selection
    }
}

const btnCreateProject = document.getElementById("create_new_project");
const btnNext_UpdateProject = document.getElementById("btn_next_updproj");

btnCreateProject.onclick = () => {
    disable_btnOpt(btnCreateProject)
    window.location.href = url_projCreate
}

// form logic

const form_projectUpdate = document.getElementById("project_update_form");


btnNext_UpdateProject.onclick = () => {
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


// basecamp editable fields
var befs = document.querySelectorAll(".bascamp-text .editable")

const btn_contentEdit = document.getElementById("contentEditButton")
const contentEditOptions = document.getElementById("contentEditOptions")
const btn_contentEdit_done = contentEditOptions.querySelector("#contentEditOption-done")
const btn_contentEdit_cancel = contentEditOptions.querySelector("#contentEditOption-cancel")

const bascampTextDiv = document.querySelector(".bascamp-text")

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
    befs = document.querySelectorAll(".bascamp-text .editable")
    befs.forEach(el => {    
        if (!el.querySelector(".input-bef")) {
            const pname = el.getAttribute("pname")
            const pvalue = el.getAttribute("pvalue")
            const tvalue = el.getAttribute("tvalue")
            const inpID = `inp-bef-${pname}`    
            el.innerHTML = `
                <span class="input-bef form-control" id="${inpID}" role="textbox" name="${pname}" contenteditable>${pvalue}</span>
            `
            const inp = document.getElementById(inpID)
            el.classList.add('editing')
            if (first) {
                inp.focus()
                moveCursorToEndOfContenteditable(inp)
                first = false
            }
            inp.addEventListener("input", ()=>{
                ValidateResponseInputs();
            })
        }
    })  
    if (!btn_contentEdit_done.classList.contains("disabled")) btn_contentEdit_done.classList.add("disabled")
    if (btn_contentEdit_cancel.classList.contains("disabled")) btn_contentEdit_cancel.classList.remove("disabled")
    $(btn_contentEdit).hide()
    $(contentEditOptions).show()
}

btn_contentEdit.onclick = initResponseFields

editCancel = () => {
    befs.forEach(el => {  
        const pname = el.getAttribute("pname")
        const pvalue = el.getAttribute("pvalue")
        const tvalue = el.getAttribute("tvalue")
        el.innerHTML = tvalue
        el.classList.remove('editing')
    })
    $(contentEditOptions).hide()
    $(btn_contentEdit).show()
}

editSubmit = () => {
    if (ValidateResponseInputs(true)) {
        if (!btn_contentEdit_done.classList.contains("disabled")) btn_contentEdit_done.classList.add("disabled")
        return;
    }

    if (!btn_contentEdit_done.classList.contains("disabled")) btn_contentEdit_done.classList.add("disabled")
    if (!btn_contentEdit_cancel.classList.contains("disabled")) btn_contentEdit_cancel.classList.add("disabled")

    // collect all responses
    var responses = {}
    befs.forEach(el => { 
        const pname = el.getAttribute("pname")
        const pvalue = el.getAttribute("pvalue")
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
        url: url_update_responses,
        data: {
            'project_id': project_id,
            'responses': JSON.stringify(responses),
        },
        success: function(data){
            if (data['updated']) {
                bascampTextDiv.innerHTML = data["responses_text"]
                $(contentEditOptions).hide()
                $(btn_contentEdit).show()
            } else {
                // show error message
                editCancel();
            }
        },
        error: function(error){
            console.log(error);
            // show error message
            editCancel();
        }
    });
}

btn_contentEdit_cancel.onclick = editCancel
btn_contentEdit_done.onclick = editSubmit



