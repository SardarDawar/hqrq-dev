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
var $backButton = $("#btn_back_updproj");

// ***************************************************************************
// TODO : TOP UPPER TAB HANDLER
// ***************************************************************************
pg2tabs.forEach(el => {    
  el.onclick = () => {

    // TODO : Show Edit Button
    $("#contentEditButton").show();

    // TODO : Hide Done Button
    $("#contentDoneButton").hide();

    // TODO : Get Current Question ID (qid)...
    if (el.dataset.qid && !el.classList.contains("active")) {
      // console.debug(ANSWER_DICT);
      const qid = el.dataset.qid;
      if (qid === curr_qid) {
        return;
      }

      // TODO : Get Question Dictionary...
      var itm = pg2_tabs_dict[qid]

      // TODO : Show Answer Me Option Only On The First Tab, Otherwise Hide It...
      if(qid == 0){
        $(".auto-answer").show();
      }
      else{
        $(".auto-answer").hide();
      }

      // TODO : Get Questions Leading Text
      var itm_leading = pg2_tabs_leading_dict[qid];

      // ?  Currente Value of Question-ID
      curr_qid = qid;

      // TODO : Set Current Question Help TextValue
      $("button.acc-help").attr("data-helptext", TIP_DICT[parseInt(curr_qid)]);
      
      // TODO : Click Event Handler for Button Help Text
      $("button.acc-help").on("click", function(){
        $("#infoModalContent-text").html( TIP_DICT[parseInt(curr_qid)]);
      });
      
      //  ! Change text of NEXT button to SUBMIT, if this the last tab...
      if(Object.keys(pg2_tabs_dict).length == parseInt(curr_qid)+1){
        $("#btn_next_updproj").html("Submit");
      }
      else{
        $("#btn_next_updproj").html("Next");
      }

      // !  Change the value of onclick event handler, if it is the first tab...
      if(parseInt(curr_qid) == 0){
        $backButton.attr("onclick", "event.preventDefault(); pageCleanup(); window.location.href='/p/u/10-tesing-project-multiple-words/doc_len'");
      }
      else{
        $backButton.attr("onclick", "null");
      }

      // TODO : remove "active" class from all other Tabs except for the current one.
      pg2tabs.forEach(el2 => { 
        if (el2 !== el && el2.classList.contains("active")){
          el2.classList.remove("active");
        }
      });

      // TODO : Set the value of current tab to "active", if "active" class is not present in it class attribute. 
      if (!el.classList.contains("active")){
        el.classList.add("active");
      }

      // !  If current tab has sub-questions....
      if (Object.keys(itm).length>1) {

        // TODO : save the current sab-question tab value.
        currnet_index = activeSabTab[parseInt(curr_qid)];

        // TODO : Show the current sab-question.
        curr_sqid = Object.keys(itm)[currnet_index];
        
        // !  Change the value for the answer according to the current sab-question...
        // !  Always show Answer of first sab-question on all sub-versions of  the questoin
        // !  For this purpose
        // !  Set currnet_index = 0
        $("#pg1_field_updproj").val(String(ANSWER_DICT[curr_qid][0]).trim());

        // TODO : Disabled Edit Button on current value of answer input field
        if($("#pg1_field_updproj").val().trim() != ""){
          $("#contentEditButton").attr("disabled", true);
        }
        else{
          $("#contentEditButton").attr("disabled", false);
        }

        // TODO : Disabled "NEXT" Button if current value of answer input field is EMPTY
        if($("#pg1_field_updproj").val().trim() == ""){
          $("#btn_next_updproj").prop("disabled", true);
        }
        else{
          $("#btn_next_updproj").prop("disabled", false);
        }

        // !  Show Current Tab Sab-Question
        $pg2change_q.stop().fadeOut(100, ()=> {
          $pg2change_q.html(curr_sqid).fadeIn(50);
          if (!tabMVleft.classList.contains("show")){
            tabMVleft.classList.add("show");
          }
          if (!tabMVright.classList.contains("show")){
            tabMVright.classList.add("show");
          }
        });

        // !  Change Current Tab Sab-Question Leading Text...
        $pg2change_ql.stop().fadeOut(100, ()=> {
          $pg2change_ql.html(itm_leading[currnet_index].charAt(0).toUpperCase() + 
          itm_leading[currnet_index].slice(1)).fadeIn(50);
        });
        tabMVleft.onclick = null
        tabMVright.onclick = null

        // !  Left Button Click Event Handler
        tabMVleft.onclick = () => {
          
          // TODO : Show Edit Button
          $("#contentEditButton").show();

          // TODO : Hide Done Button
          $("#contentDoneButton").hide();

          // !  Condition if this is not the first sab-question tab....
          // !  If it is so
          // !  Decrease "currnet_index" value by 1
          // !  Set Active Sub Tab value...
          // !  Update the answer input current value
          if (currnet_index != 0) {
            currnet_index -= 1;
            activeSabTab[parseInt(curr_qid)] = currnet_index;
            $("#pg1_field_updproj").val(String(ANSWER_DICT[curr_qid][0]).trim());

            // TODO : Disabled Edit Button on current value of answer input field
            if($("#pg1_field_updproj").val().trim() != ""){
              $("#contentEditButton").attr("disabled", true);
            }
            else{
              $("#contentEditButton").attr("disabled", false);
            }

            // TODO : Disabled "NEXT" Button if current value of answer input field is EMPTY
            if($("#pg1_field_updproj").val().trim() == ""){
              $("#btn_next_updproj").prop("disabled", true);
            }
            else{
              $("#btn_next_updproj").prop("disabled", false);
            }

            // !  Get Current Sub-Question...
            curr_sqid = Object.keys(itm)[currnet_index]

            $pg2change_q.stop().fadeOut(100, ()=> {
              $pg2change_q.html(curr_sqid).fadeIn(50);
            });
            $pg2change_ql.stop().fadeOut(100, ()=> {
              $pg2change_ql.html(itm_leading[currnet_index].charAt(0).toUpperCase() + 
              itm_leading[currnet_index].slice(1)).fadeIn(50);
            })
          }
        }
        // !  Right Angled Button
        tabMVright.onclick = () => {
          // console.debug("JS FILE : 255 : ", ANSWER_DICT);
          $("#contentEditButton").show();
          $("#contentDoneButton").hide();
          if (currnet_index != Object.keys(itm).length-1) {
            currnet_index += 1;
            activeSabTab[parseInt(curr_qid)] = currnet_index;
            curr_sqid = Object.keys(itm)[currnet_index]
            $("#pg1_field_updproj").val(String(ANSWER_DICT[curr_qid][0]).trim());

            // TODO : Disabled Edit Button on current value of input field
            if($("#pg1_field_updproj").val().trim() != ""){
              $("#contentEditButton").attr("disabled", true);
            }
            else{
              $("#contentEditButton").attr("disabled", false);
            }

            // TODO : Disabled "NEXT" Button if current value of answer input field is EMPTY
            if($("#pg1_field_updproj").val().trim() == ""){
              $("#btn_next_updproj").prop("disabled", true);
            }
            else{
              $("#btn_next_updproj").prop("disabled", false);
            }


            $pg2change_q.stop().fadeOut(100, ()=> {
              $pg2change_q.html(curr_sqid).fadeIn(50);
            });
            $pg2change_ql.stop().fadeOut(100, ()=> {
              $pg2change_ql.html(itm_leading[currnet_index].charAt(0).toUpperCase() + 
              itm_leading[currnet_index].slice(1)).fadeIn(50);
            });
          }
        }

      } 
      else {
        // !  Change the value for activeTab
          activeSabTab[parseInt(curr_qid)] = 0;
          // console.debug(activeSabTab);
        tabMVleft.onclick = null;
        tabMVright.onclick = null;
        // !  Set Answer for current Tab
        $("#pg1_field_updproj").val( String(ANSWER_DICT[(curr_qid)]).trim());


        // TODO : Disabled Edit Button on current value of input field
        if($("#pg1_field_updproj").val().trim() != ""){
          $("#contentEditButton").attr("disabled", true);
        }
        else{
          $("#contentEditButton").attr("disabled", false);
        }

        // TODO : Disabled "NEXT" Button if current value of answer input field is EMPTY
        if($("#pg1_field_updproj").val().trim() == ""){
          $("#btn_next_updproj").prop("disabled", true);
        }
        else{
          $("#btn_next_updproj").prop("disabled", false);
        }

        
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

    const project_id = JSON.parse(document.getElementById('PROJECT_ID').textContent);
    $.ajax({
      
      method: "GET",
      url: $("#btn_next_updproj").attr("data-url"),
      data: { 
          project_id : project_id,
          // name: "AJAx", 
          answer : JSON.stringify(ANSWER_DICT),
      }
  }).done(function(response){
      // console.debug(response);
      // ANSWER_DICT = response["instance"];
      for(var index=0; index < Object.keys(response["instance"]).length; index++){
        // console.debug(response["instance"][index]);
        ANSWER_DICT[index] = response["instance"][index];
      }
  });


  }
})

pg2tabs[0].click()


// ***************************************************************************************
//  TODO  : Next Button Handler
// ***************************************************************************************
// TODO : Next Button Form Submission Handler
btnNext_UpdateProject.onclick = () => {

  // console.debug(pg2_tabs_dict);


  // TODO : Get the value of current tab answer...
  var projUpd = $("#pg1_field_updproj").val().trim();
  
  // !  AJAX GET METHOD TO SAVE ANSWER TO THE DATABASE
  const project_id = JSON.parse(document.getElementById('PROJECT_ID').textContent);
  $.ajax({
    method: "GET",
    url: $("#btn_next_updproj").attr("data-url"),
    data: { 
        project_id : project_id,
        answer : JSON.stringify(ANSWER_DICT),
    }
  }).done(function(response){
    for(var index=0; index < Object.keys(response["instance"]).length; index++){
      ANSWER_DICT[index] = response["instance"][index];
    }
  });


  if (!projUpd || projUpd.length === 0 ) {
      btnNext_UpdateProject.disabled = true;
      return;
  }

  // console.debug("JS FILE : 393",ANSWER_DICT);


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


    // console.debug("Nexxt Button Event", curr_qid);
    // !  Behavour of the Back  Button....
    // !  Change the value of onclick event handler, if it is the first tab...
    


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
      currnet_index = activeSabTab[parseInt(curr_qid)+1];
      tabMVleft.onclick = null;
      tabMVright.onclick = null;

      // !  Set currnet_index = 0 for current answer of the sab-question
      $("#pg1_field_updproj").val(String(ANSWER_DICT[parseInt(curr_qid)+1][0]).trim());
      if(String(ANSWER_DICT[parseInt(curr_qid)+1][0]).trim() == ""){
        
        // TODO : Disabled "NEXT" Button if current value of answer input field is EMPTY
        if($("#pg1_field_updproj").val().trim() == ""){
          $("#btn_next_updproj").prop("disabled", true);
        }
        else{
          $("#btn_next_updproj").prop("disabled", false);
        }
      }
      
      // TODO : Left Angle Sub-Question Button Handler
      tabMVleft.onclick = () => {
        // console.debug("LEFT  ANGLE : ", ANSWER_DICT);
        $("#contentEditButton").show();
        $("#contentDoneButton").hide();
        if (currnet_index != 0) {
          currnet_index -= 1;
          activeSabTab[parseInt(curr_qid)] = currnet_index;
          $("#pg1_field_updproj").val(String(ANSWER_DICT[(curr_qid)][0]).trim());

          // TODO : Disabled Edit Button on current value of answer input field
          if($("#pg1_field_updproj").val().trim() != ""){
            $("#contentEditButton").attr("disabled", true);
          }
          else{
            $("#contentEditButton").attr("disabled", false);
          }

          // TODO : Disabled "NEXT" Button if current value of answer input field is EMPTY
          if($("#pg1_field_updproj").val().trim() == ""){
            $("#btn_next_updproj").prop("disabled", true);
          }
          else{
            $("#btn_next_updproj").prop("disabled", false);
          }



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
        // console.debug("RIGHT  ANGLE : ", pg2_tabs_dict);
        $("#contentEditButton").show();
        $("#contentDoneButton").hide();
        if (currnet_index != Object.keys(itm).length-1) {
          currnet_index += 1;
          activeSabTab[parseInt(curr_qid)] = currnet_index;
          $("#pg1_field_updproj").val(String(ANSWER_DICT[(curr_qid)][0]).trim());


          // TODO : Disabled Edit Button on current value of answer input field
          if($("#pg1_field_updproj").val().trim() != ""){
            $("#contentEditButton").attr("disabled", true);
          }
          else{
            $("#contentEditButton").attr("disabled", false);
          }

          // TODO : Disabled "NEXT" Button if current value of answer input field is EMPTY
          if($("#pg1_field_updproj").val().trim() == ""){
            $("#btn_next_updproj").prop("disabled", true);
          }
          else{
            $("#btn_next_updproj").prop("disabled", false);
          }


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
      activeSabTab[parseInt(curr_qid)] = 0;
      $("#pg1_field_updproj").val(String(ANSWER_DICT[parseInt(curr_qid)+1]).trim());


      // TODO : Disabled Edit Button on current value of answer input field
      if($("#pg1_field_updproj").val().trim() != ""){
        $("#contentEditButton").attr("disabled", true);
      }
      else{
        $("#contentEditButton").attr("disabled", false);
      }

      // TODO : Disabled "NEXT" Button if current value of answer input field is EMPTY
      if($("#pg1_field_updproj").val().trim() == ""){
        $("#btn_next_updproj").prop("disabled", true);
      }
      else{
        $("#btn_next_updproj").prop("disabled", false);
      }


      tabMVleft.classList.remove("show");
      tabMVright.classList.remove("show");
      $pg2change_q.html(Object.keys(itm)[0]);
      $pg2change_q.fadeIn(50);
      $pg2change_ql.html((itm_leading[0]).charAt(0).toUpperCase() + 
      itm_leading[0].slice(1));
      $pg2change_ql.fadeIn(50);
    }
    
    curr_qid = $(pg2tabs[parseInt(curr_qid)+1]).attr("data-qid");
    if(parseInt(curr_qid) == 0){
      $backButton.attr("onclick", "event.preventDefault(); pageCleanup(); window.location.href='/p/u/10-tesing-project-multiple-words/doc_len'");
    }
    else{
      $backButton.attr("onclick", "null");
    }
    if(Object.keys(pg2_tabs_dict).length == parseInt(curr_qid)+1){
      $("#btn_next_updproj").html("Submit");
    }
    else{
      $("#btn_next_updproj").html("Next");
    }
  }
}


// ***********************************************************************
// TODO : END OF "NEXT BUTTON" HANDLER....
// ***********************************************************************



// ***********************************************************************
// TODO :  "BACK BUTTON" HANDLER....
// ***********************************************************************


// ! Case Test for Edit Button
// TODO : edit button should be there but blocked (possibly with small error message) - remove answers on this topic first.
if($("#pg1_field_updproj").val().trim() != ""){
  $("#contentEditButton").attr("disabled", true);
}
else{
  $("#contentEditButton").attr("disabled", false);
}



// !  Back Button Click Handler
$backButton.on("click", function(event){
  event.preventDefault();
  event.stopPropagation();

  // console.debug(pg2_tabs_dict, ANSWER_DICT,  parseInt(curr_qid)-1, activeSabTab);
  
  
  currnet_index = activeSabTab[parseInt(curr_qid)-1];

  // console.debug(currnet_index);
  // console.debug(currnet_index, pg2_tabs_dict);

  // !  Check if current tab is ZERO 
  if((parseInt(curr_qid)) == 0){
    $backButton.attr("onclick", "event.preventDefault(); pageCleanup(); window.location.href='/p/u/10-tesing-project-multiple-words/doc_len'");
    // console.debug("BACK BUTTON ZERO TAB CONDITION");
  }
  else{
    $backButton.attr("onclick", "null");
    // TODO : Remove All Active Tabs 
    $.each($(pg2tabs), function(){
      $(this).removeClass("active");
    });



// !  Check if this is not the last tab 
//  ! Change text of NEXT button to SUBMIT, if this the last tab...
if(Object.keys(pg2_tabs_dict).length == parseInt(curr_qid)){
  $("#btn_next_updproj").html("Submit");
}
else{
  $("#btn_next_updproj").html("Next");
}






    // TODO : Active Next Tab
    $(pg2tabs[parseInt(curr_qid)-1]).addClass("active");
    
    // TODO : Get Next Tab Question Object
    itm = pg2_tabs_dict[parseInt(curr_qid)-1];

    // TODO : Get Next Tab Question Leading Object
    itm_leading = pg2_tabs_leading_dict[parseInt(curr_qid)-1]

    // TODO : Check Number of Questions for Next Tab
    numberOfQuestions = Object.keys(itm).length;

    // TODO : Check Number of Question is equal to 1 or greater than 1
    if(numberOfQuestions > 1){

      // currnet_index = activeSabTab[parseInt(curr_qid)-1] ;

      // console.debug(Object.keys(itm)[pg2_tabs_dict]);

      // TODO : Show Main Question
      $pg2change_q.html(Object.keys(itm)[currnet_index]);
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
      curr_sqid = Object.keys(itm)[currnet_index];
      tabMVleft.onclick = null;
      tabMVright.onclick = null;
      // ANSWER_DICT[parseInt(curr_qid)+1][currnet_index] = $("#pg1_field_updproj").val();
      // console.debug(ANSWER_DICT);
      $("#pg1_field_updproj").val(String(ANSWER_DICT[parseInt(curr_qid)-1][0]).trim());
      
      // TODO : Left Angle Sub-Question Button Handler
      tabMVleft.onclick = () => {
        $("#contentEditButton").show();
        $("#contentDoneButton").hide();
        if (currnet_index != 0) {
          currnet_index -= 1;
          activeSabTab[parseInt(curr_qid)] = currnet_index;
          $("#pg1_field_updproj").val(String(ANSWER_DICT[parseInt(curr_qid)-1][0]).trim());
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
        // console.debug(Object.keys(itm), currnet_index);
        $("#contentEditButton").show();
        $("#contentDoneButton").hide();
        if (currnet_index != Object.keys(itm).length-1) {
          currnet_index += 1;
          activeSabTab[parseInt(curr_qid)] = currnet_index;
          $("#pg1_field_updproj").val(String(ANSWER_DICT[parseInt(curr_qid)-1][0]).trim());
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
      activeSabTab[parseInt(curr_qid)] = 0;
      $("#pg1_field_updproj").val(String(ANSWER_DICT[parseInt(curr_qid)-1]).trim());


// TODO : Disabled Edit Button on current value of input field
        if($("#pg1_field_updproj").val().trim() != ""){
          $("#contentEditButton").attr("disabled", true);
        }
        else{
          $("#contentEditButton").attr("disabled", false);
        }

        // TODO : Disabled "NEXT" Button if current value of answer input field is EMPTY
        if($("#pg1_field_updproj").val().trim() == ""){
          $("#btn_next_updproj").prop("disabled", true);
        }
        else{
          $("#btn_next_updproj").prop("disabled", false);
        }



      tabMVleft.classList.remove("show");
      tabMVright.classList.remove("show");
      $pg2change_q.html(Object.keys(itm)[0]);
      $pg2change_q.fadeIn(50);
      $pg2change_ql.html((itm_leading[0]).charAt(0).toUpperCase() + 
      itm_leading[0].slice(1));
      $pg2change_ql.fadeIn(50);
    }
    
    curr_qid = $(pg2tabs[parseInt(curr_qid)-1]).attr("data-qid");
    if((parseInt(curr_qid)) == 0){
      $backButton.attr("onclick", "event.preventDefault(); pageCleanup(); window.location.href='/p/u/10-tesing-project-multiple-words/doc_len'");
    }
    else{
      $backButton.attr("onclick","null");
    }
    
  }


})
