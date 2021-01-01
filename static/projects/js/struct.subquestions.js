

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
// console.debug(pg2tabs);

const pg2change_q = document.getElementById("pg2-change-question")
const pg2change_ql = document.getElementById("pg2-change-questionlead")
const $pg2change_q = $(pg2change_q)
const $pg2change_ql = $(pg2change_ql)

const tabMVleft = document.querySelector(".tab-mover.tb-mv-left")
const tabMVright = document.querySelector(".tab-mover.tb-mv-right")

var curr_qid = 0;
var curr_sqid = -1;
var currnet_index = 0;

pg2tabs.forEach(el => {    
  el.onclick = () => {
    if (el.dataset.qid && !el.classList.contains("active")) {
      const qid = el.dataset.qid;
      if (qid === curr_qid) return;
      const itm = pg2_tabs_dict[qid]
      curr_qid = qid;
      // console.debug(curr_qid);
      // console.debug(qid);
      // console.debug(itm);
      pg2tabs.forEach(el2 => { 
        if (el2 !== el && el2.classList.contains("active")) el2.classList.remove("active")
      })
      if (!el.classList.contains("active")) el.classList.add("active")
      // console.debug(Object.keys(itm).length);
      if (Object.keys(itm).length>1) {
        // if (!tabMVleft.classList.contains("show")) tabMVleft.classList.add("show")
        // if (!tabMVright.classList.contains("show")) tabMVright.classList.add("show")
        // console.debug(itm);
        // for (var firstKey in itm['subq']) break;
        curr_sqid = Object.keys(itm)[0];
        currnet_index = 0
        // console.debug(curr_sqid);
        $pg2change_q.stop().fadeOut(100, ()=> {
          $pg2change_q.html(curr_sqid);
          $pg2change_q.fadeIn(50)
          if (!tabMVleft.classList.contains("show")) tabMVleft.classList.add("show")
          if (!tabMVright.classList.contains("show")) tabMVright.classList.add("show")
        });
        $pg2change_ql.stop().fadeOut(100, ()=> {
          $pg2change_ql.html(curr_sqid)
          $pg2change_ql.fadeIn(50)
        });
        tabMVleft.onclick = null
        tabMVright.onclick = null
        tabMVleft.onclick = () => {
          
          if (currnet_index != 0) {
            currnet_index -= 1;
            // const new_sq_id = pg2_tabs_dict[qid]['subq'][curr_sqid]["prv_sq_id"]
            curr_sqid = Object.keys(itm)[currnet_index]
            // const new_sq = pg2_tabs_dict[qid]['subq'][new_sq_id]
            $pg2change_q.stop().fadeOut(100, ()=> {
              $pg2change_q.html(curr_sqid)
              $pg2change_q.fadeIn(50)
            })
            $pg2change_ql.stop().fadeOut(100, ()=> {
              $pg2change_ql.html(curr_sqid)
              $pg2change_ql.fadeIn(50)
            })
          }

          // if (!("prv_sq_id" in pg2_tabs_dict[qid]['subq'][curr_sqid])) tabMVleft.classList.add("disabled")
          // else tabMVleft.classList.remove("disabled")
          // if (!("nxt_sq_id" in pg2_tabs_dict[qid]['subq'][curr_sqid])) tabMVright.classList.add("disabled")
          // else tabMVright.classList.remove("disabled")
        }
        tabMVright.onclick = () => {
          // var index = itm.map(function(o) { return o.attr1; }).indexOf(curr_sqid);
          // var index = itm.findIndex(p => p.attr1 == curr_sqid)
          // console.debug(index);
          if (currnet_index != Object.keys(itm).length-1) {
            currnet_index += 1;
            curr_sqid = Object.keys(itm)[currnet_index]
            // const new_sq_id = pg2_tabs_dict[qid]['subq'][curr_sqid]["nxt_sq_id"]
            // curr_sqid = new_sq_id
            // const new_sq = pg2_tabs_dict[qid]['subq'][new_sq_id]
            $pg2change_q.stop().fadeOut(100, ()=> {
              $pg2change_q.html(curr_sqid)
              $pg2change_q.fadeIn(50)
            })
            $pg2change_ql.stop().fadeOut(100, ()=> {
              $pg2change_ql.html(curr_sqid)
              $pg2change_ql.fadeIn(50)
            })
          }

          // if (!("prv_sq_id" in pg2_tabs_dict[qid]['subq'][curr_sqid])) tabMVleft.classList.add("disabled")
          // else tabMVleft.classList.remove("disabled")
          // if (!("nxt_sq_id" in pg2_tabs_dict[qid]['subq'][curr_sqid])) tabMVright.classList.add("disabled")
          // else tabMVright.classList.remove("disabled")
        }

        // if (!("prv_sq_id" in pg2_tabs_dict[qid]['subq'][curr_sqid])) tabMVleft.classList.add("disabled")
        // else tabMVleft.classList.remove("disabled")
        // if (!("nxt_sq_id" in pg2_tabs_dict[qid]['subq'][curr_sqid])) tabMVright.classList.add("disabled")
        // else tabMVright.classList.remove("disabled")

      } else {
        tabMVleft.onclick = null
        tabMVright.onclick = null
        // if (tabMVleft.classList.contains("show")) tabMVleft.classList.remove("show")
        // if (tabMVright.classList.contains("show")) tabMVright.classList.remove("show")
        curr_sqid = -1;
        // console.debug($pg2change_q);
        $pg2change_q.stop().fadeOut(100, ()=> {
          // console.debug(Object.keys(itm)[0]);
          $pg2change_q.html(Object.keys(itm)[0]);
          $pg2change_q.fadeIn(50)
          if (tabMVleft.classList.contains("show")) tabMVleft.classList.remove("show")
          if (tabMVright.classList.contains("show")) tabMVright.classList.remove("show")
        })
        $pg2change_ql.stop().fadeOut(100, ()=> {
          $pg2change_ql.html(Object.keys(itm)[0])
          // $pg2change_q.html(Object.keys(itm)[0]);
          // console.debug(itm['ql']);
          $pg2change_ql.fadeIn(50)
        })
      }
    }
  }
})

pg2tabs[0].click()
