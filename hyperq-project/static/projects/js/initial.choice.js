// ####################################
//
// page 0
//
// ####################################



// initially
var curr_page_sel = '.page-wrap.pg2-wrap'


fixMainWinHeightImmediate(curr_page_sel);

window.onresize = () => {
    fixMainWinHeightImmediate(curr_page_sel);
}

const btnCreateProject = document.getElementById("create_new_project");
const btnNext_UpdateProject = document.getElementById("btn_next_updproj");

btnCreateProject.onclick = () => {
    disable_btnOpt(btnCreateProject)
    pageCleanup();
    window.location.href = url_projCreate
}

// page 2 visual choices
const pg2vischContainer = document.querySelectorAll(".pg2-visch.visch-container")
const pg2vischs = document.querySelectorAll(".pg2-visch > *")

// disable choice pointer events until transition
$(pg2vischContainer).css("pointer-events", "none");
setTimeout(()=>{
    $(pg2vischContainer).css("pointer-events", "all");
}, 500);
// initial choice
var pg2_selection_check = false;
pg2vischs.forEach(el => {    
    if (el.classList.contains("sel")) {
        pg2_selection_check = true;
        const el_id = el.getAttribute("id");
        if (el_id in pg2_visch_help_dict) {
            if (pg2_visch_help_dict[el_id][1] === null) {
                setRightSidebarSecondaryContent(curr_page_sel, pg2_sdbrR_header, pg2_visch_help_dict[el_id][2], pg2_visch_help_dict[el_id][0], true)
                setRightSidebarContent(pg2_sdbrR_header, pg2_visch_help_dict[el_id][2], pg2_visch_help_dict[el_id][0], true)
            } else {
                setRightSidebarSecondaryContent(curr_page_sel, pg2_visch_help_dict[el_id][1], pg2_visch_help_dict[el_id][2], pg2_visch_help_dict[el_id][0], true)
                setRightSidebarContent(pg2_visch_help_dict[el_id][1], pg2_visch_help_dict[el_id][2], pg2_visch_help_dict[el_id][0], true)
            }
        }            
    }
})
// set this only if no option on pg2 has been selected
if (!pg2_selection_check) 
{
    // initially
    setRightSidebarSecondaryContent(curr_page_sel, pg2_sdbrR_header, pg2_sdbrR_content, null, true, true)
    setRightSidebarContent(pg2_sdbrR_header, pg2_sdbrR_content, null, true, true)
}

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

var field_projupd = proj_choice_curr_value || null;

pg2vischs.forEach(el => {    
    el.onclick = () => {
        if (el.classList.contains("sel")) {
            clearAllVischsSel(pg2vischs);
            field_projupd = null;
            setRightSidebarSecondaryContent(curr_page_sel, pg2_sdbrR_header, pg2_sdbrR_content, null, !sdbrR_header_fixed)
            setRightSidebarContent(pg2_sdbrR_header, pg2_sdbrR_content, null, !sdbrR_header_fixed)
        } else {
            clearAllVischsSel(pg2vischs, el);
            el.classList.add("sel")
            field_projupd = el.getAttribute("optval");
            const el_id = el.getAttribute("id");
            if (el_id in pg2_visch_help_dict) {
                setRightSidebarSecondaryContent(curr_page_sel, pg2_visch_help_dict[el_id][1], pg2_visch_help_dict[el_id][2], pg2_visch_help_dict[el_id][0], !sdbrR_header_fixed)
                setRightSidebarContent(pg2_visch_help_dict[el_id][1], pg2_visch_help_dict[el_id][2], pg2_visch_help_dict[el_id][0], !sdbrR_header_fixed)
            }
        }
        if (field_projupd) btnNext_UpdateProject.disabled = false;
        else btnNext_UpdateProject.disabled = true;
    }
    el.addEventListener('mouseenter', () => {
        const el_id = el.getAttribute("id");
        if (el_id in pg2_visch_help_dict) {
            setRightSidebarSecondaryContent(curr_page_sel, pg2_visch_help_dict[el_id][1], pg2_visch_help_dict[el_id][2], pg2_visch_help_dict[el_id][0], !sdbrR_header_fixed)
            setRightSidebarContent(pg2_visch_help_dict[el_id][1], pg2_visch_help_dict[el_id][2], pg2_visch_help_dict[el_id][0], !sdbrR_header_fixed)
        }
    })
    el.addEventListener('mouseleave', () => {
        var selected = false;
        pg2vischs.forEach(ele => {
            if (ele.classList.contains("sel")) {
                const el_id = ele.getAttribute("id");
                if (el_id in pg2_visch_help_dict) {
                    setRightSidebarSecondaryContent(curr_page_sel, pg2_visch_help_dict[el_id][1], pg2_visch_help_dict[el_id][2], pg2_visch_help_dict[el_id][0], !sdbrR_header_fixed)
                    setRightSidebarContent(pg2_visch_help_dict[el_id][1], pg2_visch_help_dict[el_id][2], pg2_visch_help_dict[el_id][0], !sdbrR_header_fixed)
                }
                selected = true;
            }
        })  
        if (!selected) {
            setRightSidebarSecondaryContent(curr_page_sel, pg2_sdbrR_header, pg2_sdbrR_content, null, !sdbrR_header_fixed)
            setRightSidebarContent(pg2_sdbrR_header, pg2_sdbrR_content, null, !sdbrR_header_fixed)
        }
    })
})


// form logic

if (!proj_choice_curr_value) btnNext_UpdateProject.disabled = true;

const form_projectUpdate = document.getElementById("project_update_form");
const formInp_upd = document.getElementById("projFormInp-upd");

btnNext_UpdateProject.onclick = () => {
    const projUpd = field_projupd;
    if (!projUpd || projUpd.length === 0) {
        btnNext_UpdateProject.disabled = true;
        return;
    }

    formInp_upd.value = projUpd;
    pageCleanup();
    form_projectUpdate.submit();
}