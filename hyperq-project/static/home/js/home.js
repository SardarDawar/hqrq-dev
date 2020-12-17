// ####################################
//
// page 0
//
// ####################################

const btnCreateProject = document.getElementById("create_new_project");
const btnBack_CreateProjectPage_1_Name = document.getElementById("btn_back_crprojName");
const btnNext_CreateProjectPage_1_Name = document.getElementById("btn_next_crprojName");
const btnBack_CreateProjectPage_2_DocType = document.getElementById("btn_back_crprojDocType");
const btnNext_CreateProjectPage_2_DocType = document.getElementById("btn_next_crprojDocType");

// form logic
var field_docType = null;

const field_projName = document.getElementById('pg1_field_project_name');

btnNext_CreateProjectPage_1_Name.disabled = true;
btnNext_CreateProjectPage_2_DocType.disabled = true;

const form_projectCreation = document.getElementById("project_creation_form");
const formInp_title = document.getElementById("projFormInp-title");
const formInp_doc_type = document.getElementById("projFormInp-doc_type");

checkUpdateProjNameNextButton = (speech) => {
    const val = field_projName.value.trim();
    if (val.length === 0) btnNext_CreateProjectPage_1_Name.disabled = true;
    else btnNext_CreateProjectPage_1_Name.disabled = false;
}

setVoiceToTextFieldCallback(checkUpdateProjNameNextButton)

field_projName.addEventListener('input' , checkUpdateProjNameNextButton)
field_projName.addEventListener('keyup' , (e) => {
    const val = field_projName.value.trim();
    if (event.key === "Enter" && val.length !== 0) {
        btnNext_CreateProjectPage_1_Name.click()
    }
})

btnNext_CreateProjectPage_2_DocType.onclick = () => {
    const projName = field_projName.value.trim();
    const projDocType = field_docType;
    if (!projName || !projDocType || projName.length === 0 || projDocType.length === 0) {
        btnNext_CreateProjectPage_2_DocType.disabled = true;
        return;
    }

    formInp_title.value = projName;
    formInp_doc_type.value = projDocType;
    form_projectCreation.submit();
}

// end form logic 


// initially
var curr_page_sel = '.page-wrap.pg0-wrap'

setRightSidebarSecondaryContent(curr_page_sel, pg0_sdbrR_header, pg0_sdbrR_content, null, true, true)
setRightSidebarContent(pg0_sdbrR_header, pg0_sdbrR_content, null, true, true)


fixMainWinHeightImmediate(curr_page_sel);

window.onresize = () => {
    fixMainWinHeightImmediate(curr_page_sel);
}

// page 2 visual choices
const pg2vischContainer = document.querySelectorAll(".pg2-visch.visch-container")
const pg2vischs = document.querySelectorAll(".pg2-visch > *")

// pages flow
btnCreateProject.onclick = () => {
    disable_btnOpt(btnCreateProject)
    collapseLeftSidebar()
    hidePage('.page-wrap.pg0-wrap')
    showPage('.page-wrap.pg1-wrap', null, ()=> {
        field_projName.focus();
    })
    setRightSidebarSecondaryContent('.page-wrap.pg1-wrap', pg1_sdbrR_header, pg1_sdbrR_content, null, true)
    setRightSidebarContent(pg1_sdbrR_header, pg1_sdbrR_content, null, true)
}

if (initilShowProjectCreationPage) btnCreateProject.click();

btnBack_CreateProjectPage_1_Name.onclick = () => {
    enable_btnOpt(btnCreateProject)
    expandLeftSidebar()
    hidePage('.page-wrap.pg1-wrap', 'right')
    showPage('.page-wrap.pg0-wrap')
    setRightSidebarSecondaryContent('.page-wrap.pg0-wrap', pg0_sdbrR_header, pg0_sdbrR_content, null, true)
    setRightSidebarContent(pg0_sdbrR_header, pg0_sdbrR_content, null, true)
}

btnNext_CreateProjectPage_1_Name.onclick = () => {
    hidePage('.page-wrap.pg1-wrap', 'left')
    showPage('.page-wrap.pg2-wrap')
    // disable choice pointer events until transition
    $(pg2vischContainer).css("pointer-events", "none");
    setTimeout(()=>{
        $(pg2vischContainer).css("pointer-events", "all");
    }, 500);
    var pg2_selection_check = false;
    pg2vischs.forEach(el => {    
        if (el.classList.contains("sel")) {
            pg2_selection_check = true;
            const el_id = el.getAttribute("id");
            if (el_id in pg2_visch_help_dict) {
                setRightSidebarSecondaryContent('.page-wrap.pg2-wrap', pg2_visch_help_dict[el_id][1], pg2_visch_help_dict[el_id][2], pg2_visch_help_dict[el_id][0], true)
                setRightSidebarContent(pg2_visch_help_dict[el_id][1], pg2_visch_help_dict[el_id][2], pg2_visch_help_dict[el_id][0], true)
            }            
        }
    })
    // set this only if no option on pg2 has been selected
    if (!pg2_selection_check) 
    {
        setRightSidebarSecondaryContent('.page-wrap.pg2-wrap', pg2_sdbrR_header, pg2_sdbrR_content, null, true)
        setRightSidebarContent(pg2_sdbrR_header, pg2_sdbrR_content, null, true)
    }
}

btnBack_CreateProjectPage_2_DocType.onclick = () => {
    hidePage('.page-wrap.pg2-wrap', 'right')
    showPage('.page-wrap.pg1-wrap')
    setRightSidebarSecondaryContent('.page-wrap.pg1-wrap', pg1_sdbrR_header, pg1_sdbrR_content, null, true)
    setRightSidebarContent(pg1_sdbrR_header, pg1_sdbrR_content, null, true)
}

// page 2 visual choices logic

clearAllVischsSel = (list, except) => {
    if (except) {
        list.forEach(el => {
            if (el !== except) {
                if (el.classList.contains("sel")) el.classList.remove("sel")
            }
        })
    } else {
        list.forEach(el => {
            if (el.classList.contains("sel")) el.classList.remove("sel")
        })
    }
}

pg2vischs.forEach(el => {    
    el.onclick = () => {
        if (el.classList.contains("sel")) {
            clearAllVischsSel(pg2vischs);
            field_docType = null;
            setRightSidebarSecondaryContent('.page-wrap.pg2-wrap', pg2_sdbrR_header, pg2_sdbrR_content, null, true)
            setRightSidebarContent(pg2_sdbrR_header, pg2_sdbrR_content, null, true)
        } else {
            clearAllVischsSel(pg2vischs, el);
            el.classList.add("sel")
            field_docType = el.getAttribute("optval");
            const el_id = el.getAttribute("id");
            if (el_id in pg2_visch_help_dict) {
                setRightSidebarSecondaryContent('.page-wrap.pg2-wrap', pg2_visch_help_dict[el_id][1], pg2_visch_help_dict[el_id][2], pg2_visch_help_dict[el_id][0], true)
                setRightSidebarContent(pg2_visch_help_dict[el_id][1], pg2_visch_help_dict[el_id][2], pg2_visch_help_dict[el_id][0], true)
            }
        }
        if (field_docType) btnNext_CreateProjectPage_2_DocType.disabled = false;
        else btnNext_CreateProjectPage_2_DocType.disabled = true;
    }
    el.addEventListener('mouseenter', () => {
        const el_id = el.getAttribute("id");
        if (el_id in pg2_visch_help_dict) {
            setRightSidebarSecondaryContent('.page-wrap.pg2-wrap', pg2_visch_help_dict[el_id][1], pg2_visch_help_dict[el_id][2], pg2_visch_help_dict[el_id][0], true)
            setRightSidebarContent(pg2_visch_help_dict[el_id][1], pg2_visch_help_dict[el_id][2], pg2_visch_help_dict[el_id][0], true)
        }
    })
    el.addEventListener('mouseleave', () => {
        var selected = false;
        pg2vischs.forEach(ele => {
            if (ele.classList.contains("sel")) {
                const el_id = ele.getAttribute("id");
                if (el_id in pg2_visch_help_dict) {
                    setRightSidebarSecondaryContent('.page-wrap.pg2-wrap', pg2_visch_help_dict[el_id][1], pg2_visch_help_dict[el_id][2], pg2_visch_help_dict[el_id][0], true)
                    setRightSidebarContent(pg2_visch_help_dict[el_id][1], pg2_visch_help_dict[el_id][2], pg2_visch_help_dict[el_id][0], true)
                }
                selected = true;
            }
        })  
        if (!selected) {
            setRightSidebarSecondaryContent('.page-wrap.pg2-wrap', pg2_sdbrR_header, pg2_sdbrR_content, null, true)
            setRightSidebarContent(pg2_sdbrR_header, pg2_sdbrR_content, null, true)
        }
    })
})
