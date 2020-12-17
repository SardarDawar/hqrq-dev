// ####################################
//
// page 0
//
// ####################################

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


