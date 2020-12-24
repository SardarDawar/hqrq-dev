

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







// Show the first tab and hide the rest
$("#left-button").hide()
$(document).ready(function () {
  let clickcount = 0 // variable
  $("#tabs-nav li:first-child").addClass("active")

  $("#tabs-nav li:first-child").find("rect").css("fill", "#EF8162")
  $(".tab-content").hide()
  $(".tab-content:first").show()

  $("#tabs-nav li").click(function () {
    $("#tabs-nav li").removeClass("active")

    $(".tab-content").hide()

    var activeTab = $(this).find("a").attr("href")
    var activeColor = $(this).find("rect").css("fill", "#EF8162")
    $(activeTab).fadeIn()

    console.log(activeColor, "here")

    return false
  })
  $(".subqestioncontainer #subquestionitemcontainer:first").addClass("active")
  $(".subqestioncontainer #subquestionitemcontainer").hide()
  $(".subqestioncontainer #subquestionitemcontainer:first").show()

  $("#right-button").click(function () {
    if (clickcount < 2) {
      $(".subqestioncontainer #subquestionitemcontainer").removeClass("active")
      $(".subqestioncontainer #subquestionitemcontainer").hide()

      clickcount += 1

      console.log(clickcount)
      $("#left-button").show()
    } else {
      $("#right-button").hide()
      $("#left-button").show()
    }
  })

  $("#left-button").click(function () {
    if (clickcount > 0) {
      console.log("hey")
      $(".subqestioncontainer #subquestionitemcontainer").removeClass("active")
      $(".subqestioncontainer #subquestionitemcontainer").hide()
      console.log(clickcount)

      clickcount -= 1
      $("#right-button").show()
    } else {
      $("#right-button").show()

      $("#left-button").hide()
    }
  })
})






