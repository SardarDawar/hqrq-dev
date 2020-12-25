

// ####################################
//
// page 0
//
// ####################################


const btnCreateProject = document.getElementById("create_new_project");
const btnNext_UpdateProject = document.getElementById("btn_next_updproj");
const btn_AddTopic = document.getElementById("btn_add_subtopic");

btnCreateProject.onclick = () => {
    disable_btnOpt(btnCreateProject)
    pageCleanup();
    window.location.href = url_projCreate
}

const field_addtopic = document.getElementById('field_add_subtopic');

moveCursorToEndOfInput(field_addtopic)
field_addtopic.focus()

// form logic

if (!proj_choice_curr_value) btnNext_UpdateProject.disabled = true;
if (!field_addtopic.value.trim()) btn_AddTopic.disabled = true;

const form_projectUpdate = document.getElementById("project_update_form");
const formInp_upd = document.getElementById("projFormInp-upd");

checkUpdateButtonNext = (speech) => {
    const val = field_addtopic.value.trim();
    if (val.length === 0) btn_AddTopic.disabled = true;
    else btn_AddTopic.disabled = false;
}

setVoiceToTextFieldCallback(checkUpdateButtonNext)

field_addtopic.addEventListener('input' , checkUpdateButtonNext)
field_addtopic.addEventListener('keyup' , (e) => {
    const val = field_addtopic.value.trim();
    if (event.key === "Enter" && val.length !== 0) {
        btn_AddTopic.click()
    }
})

// form logic end

// initially
var curr_page_sel = '.page-wrap.pg2-wrap'

setRightSidebarSecondaryContent(curr_page_sel, pg1_sdbrR_header, pg1_sdbrR_content, null, true, true)
setRightSidebarContent(pg1_sdbrR_header, pg1_sdbrR_content, null, true, true)


fixMainWinHeightImmediate(curr_page_sel);

window.onresize = () => {
    fixMainWinHeightImmediate(curr_page_sel);
}


// page vischsl

const pg2vischContainer = document.querySelector(".pg2-vischsl.vischsl-container")

// disable choice pointer events until transition
$(pg2vischContainer).css("pointer-events", "none");
setTimeout(()=>{
    $(pg2vischContainer).css("pointer-events", "all");
}, 500);

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

var lastsel_vischsl_id = null

setupVischslListeners = () => {
    const pg2vischs = document.querySelectorAll(".pg2-vischsl > *")
    pg2vischs.forEach(el => {   
        el.onclick = null 
        el.onclick = () => {
            if (el.classList.contains("sel")) el.classList.remove("sel")
            else el.classList.add("sel")

            var opt_selected = 0; 
            for (var i=0; i<pg2vischs.length; i++) {
                const el2 = pg2vischs[i];
                if (el2.classList.contains("sel")) {
                    opt_selected++;
                    if (opt_selected > vischsl_minsel_count+1) break;
                }
            }

            if (opt_selected == vischsl_minsel_count+1 && lastsel_vischsl_id)  {
                const lastsel_vischsl = document.getElementById(lastsel_vischsl_id)
                lastsel_vischsl.classList.remove("sel")
                lastsel_vischsl_id = null
                opt_selected--
            } else if (opt_selected > vischsl_minsel_count+1) {
                var optsel2 = 0
                for (var i=0; i<pg2vischs.length; i++) {
                    const el2 = pg2vischs[i];
                    if (el2.classList.contains("sel")) {
                        if (optsel2 == vischsl_minsel_count) el2.classList.remove("sel");
                        else optsel2++;
                    }
                }
            }

            if (opt_selected == vischsl_minsel_count) btnNext_UpdateProject.disabled = false;
            else btnNext_UpdateProject.disabled = true;

            if (el.classList.contains("sel")) lastsel_vischsl_id = el.id
        }
    })
}

setupVischslListeners()


btn_AddTopic.onclick = () => {
    const newTopic = field_addtopic.value.trim();
    if (!newTopic || newTopic.length === 0) {
        btn_AddTopic.disabled = true;
        return;
    }

    pageCleanup();

    const pg2vischs = document.querySelectorAll(".pg2-vischsl > *")

    pg2vischContainer.innerHTML += `
        <li class="vischsl-item pg2-vischsl-opt-voice" id="pg2vischsl${pg2vischs.length+1}" optval="${newTopic}" style="justify-content: center; padding: 0">
            <div class="vischsl-item-text pg2-vischsl-voice-text" style="margin-top: 0; font-size: 16px; line-height: 23px;">
                ${newTopic}
            </div>
        </li>
    `

    field_addtopic.value = ""
    btn_AddTopic.disabled = true;

    setupVischslListeners()
    const new_vischsl = document.getElementById(`pg2vischsl${pg2vischs.length+1}`)
    // new_vischsl.click()
}