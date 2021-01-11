

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
var itm = pg2_tabs_dict[0];
var itm_leading = pg2_tabs_leading_dict[0];

pg2tabs.forEach(el => {    
  // console.debug(el);
  el.onclick = () => {

    

    $("#contentEditButton").show();
    $("#contentDoneButton").hide();
    if (el.dataset.qid && !el.classList.contains("active")) {
      const qid = el.dataset.qid;
      if (qid === curr_qid) return;
      var itm = pg2_tabs_dict[qid]

      // if
      // console.debug($(".accessibility"));
      if(qid == 0){
        $(".auto-answer").show();
      }
      else{
        $(".auto-answer").hide();
      }
      var itm_leading = pg2_tabs_leading_dict[qid];
      curr_qid = qid;
      $("button.acc-help").attr("data-helptext", TIP_DICT[parseInt(curr_qid)]);
      
      $("button.acc-help").on("click", function(){
        $("#infoModalContent-text").html( TIP_DICT[parseInt(curr_qid)]);
      });
      
      if(Object.keys(pg2_tabs_dict).length == parseInt(curr_qid)+1){
        $("#btn_next_updproj").html("Submit");
      }
      else{
        $("#btn_next_updproj").html("Next");
      }

      pg2tabs.forEach(el2 => { 
        if (el2 !== el && el2.classList.contains("active")) el2.classList.remove("active")
      })
      if (!el.classList.contains("active")) el.classList.add("active")
      // console.debug(Object.keys(itm).length);
      if (Object.keys(itm).length>1) {
        curr_sqid = Object.keys(itm)[0];

        currnet_index = 0
        // console.debug(curr_sqid);
        // console.debug(ANSWER_DICT[curr_qid][currnet_index]);
        $("#pg1_field_updproj").val(ANSWER_DICT[curr_qid][currnet_index]);
        $pg2change_q.stop().fadeOut(100, ()=> {
          $pg2change_q.html(curr_sqid);
          $pg2change_q.fadeIn(50)
          if (!tabMVleft.classList.contains("show")) tabMVleft.classList.add("show")
          if (!tabMVright.classList.contains("show")) tabMVright.classList.add("show")
        });
        $pg2change_ql.stop().fadeOut(100, ()=> {
          $pg2change_ql.html(itm_leading[currnet_index].charAt(0).toUpperCase() + 
          itm_leading[currnet_index].slice(1));
          $pg2change_ql.fadeIn(50)
        });
        tabMVleft.onclick = null
        tabMVright.onclick = null
        tabMVleft.onclick = () => {
          $("#contentEditButton").show();
    $("#contentDoneButton").hide();
          if (currnet_index != 0) {
            currnet_index -= 1;
            // const new_sq_id = pg2_tabs_dict[qid]['subq'][curr_sqid]["prv_sq_id"]
            $("#pg1_field_updproj").val(ANSWER_DICT[curr_qid][currnet_index]);
            curr_sqid = Object.keys(itm)[currnet_index]
            // const new_sq = pg2_tabs_dict[qid]['subq'][new_sq_id]
            $pg2change_q.stop().fadeOut(100, ()=> {
              $pg2change_q.html(curr_sqid)
              $pg2change_q.fadeIn(50)
            })
            $pg2change_ql.stop().fadeOut(100, ()=> {
              $pg2change_ql.html(itm_leading[currnet_index].charAt(0).toUpperCase() + 
              itm_leading[currnet_index].slice(1));
              $pg2change_ql.fadeIn(50)
            })
          }

          // if (!("prv_sq_id" in pg2_tabs_dict[qid]['subq'][curr_sqid])) tabMVleft.classList.add("disabled")
          // else tabMVleft.classList.remove("disabled")
          // if (!("nxt_sq_id" in pg2_tabs_dict[qid]['subq'][curr_sqid])) tabMVright.classList.add("disabled")
          // else tabMVright.classList.remove("disabled")
        }
        tabMVright.onclick = () => {
          $("#contentEditButton").show();
    $("#contentDoneButton").hide();
          // var index = itm.map(function(o) { return o.attr1; }).indexOf(curr_sqid);
          // var index = itm.findIndex(p => p.attr1 == curr_sqid)
          // console.debug(index);
          if (currnet_index != Object.keys(itm).length-1) {
            currnet_index += 1;
            curr_sqid = Object.keys(itm)[currnet_index]
            $("#pg1_field_updproj").val(ANSWER_DICT[curr_qid][currnet_index]);
            // const new_sq_id = pg2_tabs_dict[qid]['subq'][curr_sqid]["nxt_sq_id"]
            // curr_sqid = new_sq_id
            // const new_sq = pg2_tabs_dict[qid]['subq'][new_sq_id]
            $pg2change_q.stop().fadeOut(100, ()=> {
              $pg2change_q.html(curr_sqid)
              $pg2change_q.fadeIn(50)
            })
            $pg2change_ql.stop().fadeOut(100, ()=> {
              $pg2change_ql.html(itm_leading[currnet_index].charAt(0).toUpperCase() + 
              itm_leading[currnet_index].slice(1));
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

      } 
      else {

        tabMVleft.onclick = null;
        tabMVright.onclick = null;
        // console.debug(ANSWER_DICT[curr_qid]);

        // !  Set Answer for current Tab
        $("#pg1_field_updproj").val(ANSWER_DICT[curr_qid]);
        
        curr_sqid = -1;
        
        $pg2change_q.stop().fadeOut(100, ()=> {
          $pg2change_q.html(Object.keys(itm)[0]);
          $pg2change_q.fadeIn(50)
          if (tabMVleft.classList.contains("show")) tabMVleft.classList.remove("show")
          if (tabMVright.classList.contains("show")) tabMVright.classList.remove("show")
        })
        $pg2change_ql.stop().fadeOut(100, ()=> {
          // console.debug(JSON.stringify(Object.keys(itm_leading)));
          // console.debug(itm_leading);
          $pg2change_ql.html((itm_leading[0]).charAt(0).toUpperCase() + 
          itm_leading[0].slice(1));
          $pg2change_ql.fadeIn(50)
        })
      }
    }
  }
})

pg2tabs[0].click()


// TODO : Next Button Form Submission Handler
btnNext_UpdateProject.onclick = () => {
  const projUpd = field_updproj.value.trim();
  if (!projUpd || projUpd.length === 0) {
      btnNext_UpdateProject.disabled = true;
      return;
  }


  // TODO : calculate the Number of tabs
  // TODO : get the current active tab id
  // TODO : compare if number of tabs is equal to (current active tab+1), Submit Form
  if(Object.keys(pg2_tabs_dict).length == parseInt(curr_qid)+1){
    // formInp_upd.value = projUpd;
    $("#projFormInp-upd").val(JSON.stringify(ANSWER_DICT));
    // console.debug((ANSWER_DICT));
    pageCleanup();
    // console.debug($("#projFormInp-upd").val());
    form_projectUpdate.submit();
  }
  else{
    // TODO : Remove All Active Tabs 
    $.each($(pg2tabs), function(){
      $(this).removeClass("active");
    });

    // TODO : Active Next Tab
    $(pg2tabs[parseInt(curr_qid)+1]).addClass("active");
    
    // TODO : Get Next Tab Question Object
    itm = pg2_tabs_dict[parseInt(curr_qid)+1];

    // TODO : Get Next Tab Question Leading Object
    itm_leading = pg2_tabs_leading_dict[parseInt(curr_qid)+1]

    // TODO : Check Number of Questions for Next Tab
    numberOfQuestions = Object.keys(itm).length;

    // TODO : Check Number of Question is equal to 1 or greater than 1
    if(numberOfQuestions > 1){

      // TODO : Show Main Question
      $pg2change_q.html(Object.keys(itm)[0]);
      $pg2change_q.fadeIn(50);

      // TODO : Show Main Question Leading Text
      // console.debug(itm_leading);
      $pg2change_ql.html((itm_leading[0]).charAt(0).toUpperCase() + 
      itm_leading[0].slice(1));
      $pg2change_ql.fadeIn(50);

      // TODO : Show Left Angle Sub-Question Button
      tabMVleft.classList.add("show");

      // TODO : Show Right Angle Sub-Question Button
      tabMVright.classList.add("show"); 
      curr_sqid = Object.keys(itm)[0];
      currnet_index = 0
      tabMVleft.onclick = null;
      tabMVright.onclick = null;
      // ANSWER_DICT[parseInt(curr_qid)+1][currnet_index] = $("#pg1_field_updproj").val();
      // console.debug(ANSWER_DICT);
      $("#pg1_field_updproj").val(ANSWER_DICT[parseInt(curr_qid)+1][currnet_index]);
      
      // TODO : Left Angle Sub-Question Button Handler
      tabMVleft.onclick = () => {
        $("#contentEditButton").show();
        $("#contentDoneButton").hide();
        if (currnet_index != 0) {
          currnet_index -= 1;
          $("#pg1_field_updproj").val(ANSWER_DICT[parseInt(curr_qid)+1][currnet_index]);
          curr_sqid = Object.keys(itm)[currnet_index];
          $pg2change_q.stop().fadeOut(100, ()=> {
            $pg2change_q.html(curr_sqid);
            $pg2change_q.fadeIn(50);
          });
          $pg2change_ql.stop().fadeOut(100, ()=> {
            $pg2change_ql.html(itm_leading[currnet_index].charAt(0).toUpperCase() + 
            itm_leading[currnet_index].slice(1));
            $pg2change_ql.fadeIn(50);
          });
        }
      }

      // TODO : Right Angle Sub-Question Button Handler
      tabMVright.onclick = () => {
        $("#contentEditButton").show();
        $("#contentDoneButton").hide();
        if (currnet_index != Object.keys(itm).length-1) {
          currnet_index += 1;
          $("#pg1_field_updproj").val(ANSWER_DICT[parseInt(curr_qid)+1][currnet_index]);
          curr_sqid = Object.keys(itm)[currnet_index]
          $pg2change_q.stop().fadeOut(100, ()=> {
            $pg2change_q.html(curr_sqid)
            $pg2change_q.fadeIn(50);
          });
          $pg2change_ql.stop().fadeOut(100, ()=> {
            $pg2change_ql.html(itm_leading[currnet_index].charAt(0).toUpperCase() + 
            itm_leading[currnet_index].slice(1));
            $pg2change_ql.fadeIn(50);
          });
        }
      }
    }
    else{
      tabMVleft.onclick = null;
      tabMVright.onclick = null;
      curr_sqid = -1;
      $("#pg1_field_updproj").val(ANSWER_DICT[parseInt(curr_qid)+1]);
      tabMVleft.classList.remove("show");
      tabMVright.classList.remove("show");
      $pg2change_q.html(Object.keys(itm)[0]);
      $pg2change_q.fadeIn(50);
      $pg2change_ql.html((itm_leading[0]).charAt(0).toUpperCase() + 
      itm_leading[0].slice(1));
      $pg2change_ql.fadeIn(50);
    }
    
    curr_qid = $(pg2tabs[parseInt(curr_qid)+1]).attr("data-qid");
    if(Object.keys(pg2_tabs_dict).length == parseInt(curr_qid)+1){
      $("#btn_next_updproj").html("Submit");
    }
    else{
      $("#btn_next_updproj").html("Next");
    }

  }
}


