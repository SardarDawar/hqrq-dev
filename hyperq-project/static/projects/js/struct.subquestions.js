

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

const field_updproj = document.getElementById('pg1_field_updproj');

moveCursorToEndOfInput(field_updproj)
field_updproj.focus()

// form logic

if (!proj_choice_curr_value || !field_updproj.value.trim()) btnNext_UpdateProject.disabled = true;

const form_projectUpdate = document.getElementById("project_update_form");
const formInp_upd = document.getElementById("projFormInp-upd");

checkUpdateButtonNext = (speech) => {
    const val = field_updproj.value.trim();
    if (val.length === 0) btnNext_UpdateProject.disabled = true;
    else btnNext_UpdateProject.disabled = false;
}

setVoiceToTextFieldCallback(checkUpdateButtonNext)

field_updproj.addEventListener('input' , checkUpdateButtonNext)
field_updproj.addEventListener('keyup' , (e) => {
    const val = field_updproj.value.trim();
    if (event.key === "Enter" && val.length !== 0) {
        btnNext_UpdateProject.click()
    }
})

btnNext_UpdateProject.onclick = () => {
    const projUpd = field_updproj.value.trim();
    if (!projUpd || projUpd.length === 0) {
        btnNext_UpdateProject.disabled = true;
        return;
    }

    formInp_upd.value = projUpd;
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


// page tabs

// page tabs
const pg2tabs = document.querySelectorAll(".tabselect")

const pg2change_q = document.getElementById("pg2-change-question")
const pg2change_ql = document.getElementById("pg2-change-questionlead")
const $pg2change_q = $(pg2change_q)
const $pg2change_ql = $(pg2change_ql)

const tabMVleft = document.querySelector(".tab-mover.tb-mv-left")
const tabMVright = document.querySelector(".tab-mover.tb-mv-right")

var curr_qid = 0;

pg2tabs.forEach(el => {    
  el.onclick = () => {
    if (el.dataset.qid && !el.classList.contains("active")) {
      const qid = el.dataset.qid;
      if (qid === curr_qid) return;
      console.log(qid)
      console.log(pg2_tabs_dict[qid])
      const itm = pg2_tabs_dict[qid]
      curr_qid = qid;

      pg2tabs.forEach(el2 => { 
        if (el2 !== el && el2.classList.contains("active")) el2.classList.remove("active")
      })
      if (!el.classList.contains("active")) el.classList.add("active")

      if (itm['has_subq']) {
        if (!tabMVleft.classList.contains("show")) tabMVleft.classList.add("show")
        if (!tabMVright.classList.contains("show")) tabMVright.classList.add("show")
      } else {
        if (tabMVleft.classList.contains("show")) tabMVleft.classList.remove("show")
        if (tabMVright.classList.contains("show")) tabMVright.classList.remove("show")
        $pg2change_q.stop().fadeOut(100, ()=> {
          $pg2change_q.html(itm['q'])
          $pg2change_q.fadeIn(50)
        })
        $pg2change_ql.stop().fadeOut(100, ()=> {
          $pg2change_ql.html(itm['ql'])
          $pg2change_ql.fadeIn(50)
        })
      }
    }
  }
})
