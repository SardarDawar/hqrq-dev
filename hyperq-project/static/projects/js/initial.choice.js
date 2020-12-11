// ####################################
//
// page 0
//
// ####################################


const sdbrL = document.querySelector(".sidebar.left")
const sdbrL_ddws = document.querySelectorAll(".opt-dropdown-wrap")
const sdbrR = document.querySelector(".sidebar.right")

sdbrL_ddws.forEach(el => {
    const opt = el.querySelector(".opt")
    opt.onclick = () => {
        if (el.classList.contains("sel")) el.classList.remove("sel")
        else el.classList.add("sel")
    }
});

const accSpeakers = document.querySelectorAll(".accessibility .acc-speak")

accSpeakers.forEach(el => {
    const field = document.getElementById(el.dataset.fieldid);
    el.onclick = () => {
        if (field.hasAttribute("value")) TextToVoice(field.getAttribute("value"), true);
        else TextToVoice(field.innerHTML, true);        
    }
});

const accMics = document.querySelectorAll(".accessibility .acc-mic")

accMics.forEach(el => {
    if (el.hasAttribute("voiceselect")) {
        const options = document.querySelectorAll(`.${el.dataset.fieldsclass}`);
        const forcesel = el.hasAttribute("forcesel");
        el.onclick = () => {
            VoiceToText(null, (speech) => {
                for (var o=0; o<options.length; o++)
                {
                    const opt = options[o];
                    const text = opt.querySelector(`.${el.dataset.textsclass}`).innerHTML.toLowerCase()
                    const speech_split = speech.toLowerCase().split(" ");
                    var contains_all_words = true
                    for (var i=0; i<speech_split.length; i++) {
                        if (!text.includes(speech_split[i])) {
                            contains_all_words = false
                            break;
                        }
                    }
                    if (contains_all_words) {
                        if (forcesel)
                        {
                            options.forEach(lo => {
                                if (opt !== lo && lo.classList.contains("sel")) lo.classList.remove("sel")
                            })                        
                            if (!opt.classList.contains("sel")) opt.classList.add('sel')
                            else opt.classList.remove("sel")
                        }
                        opt.click();
                        opt.focus()
                        break;
                    }
                }
            });        
        }
    } else {
        const field = document.getElementById(el.dataset.fieldid);
        el.onclick = () => {
            VoiceToText(field);        
        }
    }
});

const mainContent = document.querySelector(".main-content");
const mainWin = document.querySelector(".main-win");

const btnLeftSidebarShowHide = document.getElementById("ls_show_hide");

hideRightSidebar = () => {
    if (!sdbrR.classList.contains("closed")) sdbrR.classList.add("closed");
}

showRightSidebar = () => {
    if (sdbrR.classList.contains("closed")) sdbrR.classList.remove("closed");
}

toggleLeftSidebar = () => {
    if (!sdbrL.classList.contains("collapsed")) sdbrL.classList.add("collapsed");   // this class must be present for this functionality
    if (sdbrL.classList.contains("show")) { 
        sdbrL.classList.remove("show");
        showRightSidebar();
    } else {
        sdbrL.classList.add("show");
        hideRightSidebar();
    }
}

btnLeftSidebarShowHide.onclick = toggleLeftSidebar

collapseLeftSidebar = () => {
    if (!sdbrL.classList.contains("collapsed")) sdbrL.classList.add("collapsed");    
    if (mainContent.classList.contains("small")) mainContent.classList.remove("small");    

    if (sdbrL.classList.contains("show")) { 
        sdbrL.classList.remove("show");
    }
    showRightSidebar();
}

expandLeftSidebar = () => {
    if (sdbrL.classList.contains("collapsed")) sdbrL.classList.remove("collapsed");    
    if (!mainContent.classList.contains("small")) mainContent.classList.add("small");

    if (sdbrL.classList.contains("show")) { 
        sdbrL.classList.remove("show");
    }
    showRightSidebar();
}

fixMainWinHeight = (sel) => {
    if (window.innerWidth <= 750)
    {
        setTimeout(()=> {
            // console.log($(sel).height())
            $('.main-win').css('min-height', `${$(sel).height()}px`)
            $('.main-win').css('max-height', `${$(sel).height()}px`)
            
        }, 500)
    }
    else {
        $('.main-win').css('min-height', `unset`)
        $('.main-win').css('max-height', `unset`)
    }
}

fixMainWinHeightImmediate = (sel) => {
    if (window.innerWidth <= 750)
    {
        setTimeout(()=> {
            // console.log($(sel).height())
            $('.main-win').css('min-height', `${$(sel).height()}px`)
            $('.main-win').css('max-height', `${$(sel).height()}px`)
    
        }, 200)
    }
    else {
        $('.main-win').css('min-height', `unset`)
        $('.main-win').css('max-height', `unset`)
    }
}


const sdbrR_header = sdbrR.querySelector(".side-header");
const $sdbrR_header = $('.sidebar.right .side-header')

const sdbrR_content = sdbrR.querySelector(".side-content");
const $sdbrR_content = $('.sidebar.right .side-content')



setRightSidebarSecondaryContent = (page_sel, h_html, c_html, no_animation, initial) => {

    const sdbrRsecondary_header = document.querySelector(`${page_sel} .sidebar-right-secondary .side-header`);
    const $sdbrRsecondary_header = $(`${page_sel} .sidebar-right-secondary .side-header`)

    const sdbrRsecondary_content = document.querySelector(`${page_sel} .sidebar-right-secondary .side-content`);
    const $sdbrRsecondary_content = $(`${page_sel} .sidebar-right-secondary .side-content`)

    if (no_animation) {
        if (h_html && (!sdbrR_header_fixed || initial)) sdbrRsecondary_header.innerHTML = h_html
        sdbrRsecondary_content.innerHTML = c_html
    } else {
        if (h_html && (!sdbrR_header_fixed || initial) && sdbrRsecondary_header.innerHTML !== h_html) {
            $sdbrRsecondary_header.fadeOut(400, ()=> {
                sdbrRsecondary_header.innerHTML = h_html
                $sdbrRsecondary_header.fadeIn(300)
            })
        }
        if (sdbrRsecondary_content.innerHTML !== c_html) {
            $sdbrRsecondary_content.fadeOut(400, ()=> {
                sdbrRsecondary_content.innerHTML = c_html
                $sdbrRsecondary_content.fadeIn(300)
            })
        }
    }

    fixMainWinHeight(page_sel);
}

setRightSidebarContent = (h_html, c_html, no_animation, initial) => {
    if (no_animation) {
        if (h_html && (!sdbrR_header_fixed || initial)) sdbrR_header.innerHTML = h_html
        sdbrR_content.innerHTML = c_html
    } else {
        if (h_html && (!sdbrR_header_fixed || initial) && sdbrR_header.innerHTML !== h_html) {
            $sdbrR_header.fadeOut(400, ()=> {
                sdbrR_header.innerHTML = h_html
                $sdbrR_header.fadeIn(300)
            })
        }
        if (sdbrR_content.innerHTML !== c_html) {
            $sdbrR_content.fadeOut(400, ()=> {
                sdbrR_content.innerHTML = c_html
                $sdbrR_content.fadeIn(300)
            })
        }
    }
}

disable_btnOpt = (btn) => {
    if (!btn.classList.contains("sel")) btn.classList.add("sel");
}

enable_btnOpt = (btn) => {
    if (btn.classList.contains("sel")) btn.classList.remove("sel");    
}

// initially
setRightSidebarSecondaryContent('.page-wrap.pg2-wrap', pg2_sdbrR_header, pg2_sdbrR_content, true, true)
setRightSidebarContent(pg2_sdbrR_header, pg2_sdbrR_content, true, true)

var curr_page_sel = '.page-wrap.pg2-wrap'

fixMainWinHeightImmediate(curr_page_sel);

window.onresize = () => {
    fixMainWinHeightImmediate(curr_page_sel);
}

const btnCreateProject = document.getElementById("create_new_project");
const btnNext_UpdateProject = document.getElementById("btn_next_updproj");

btnCreateProject.onclick = () => {
    disable_btnOpt(btnCreateProject)
    window.location.href = url_projCreate
}

// page 2 visual choices
pg2vischs = document.querySelectorAll(".pg2-visch > *")

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

var field_projupd = null;

pg2vischs.forEach(el => {    
    el.onclick = () => {
        if (el.classList.contains("sel")) {
            clearAllVischsSel(pg2vischs);
            field_projupd = null;
            setRightSidebarSecondaryContent('.page-wrap.pg2-wrap', pg2_sdbrR_header, pg2_sdbrR_content)
            setRightSidebarContent(pg2_sdbrR_header, pg2_sdbrR_content)
        } else {
            clearAllVischsSel(pg2vischs, el);
            el.classList.add("sel")
            field_projupd = el.getAttribute("optval");
            const el_id = el.getAttribute("id");
            if (el_id in pg2_visch_help_dict) {
                setRightSidebarSecondaryContent('.page-wrap.pg2-wrap', pg2_visch_help_dict[el_id][0], pg2_visch_help_dict[el_id][1])
                setRightSidebarContent(pg2_visch_help_dict[el_id][0], pg2_visch_help_dict[el_id][1])
            }
        }
        if (field_projupd) btnNext_UpdateProject.disabled = false;
        else btnNext_UpdateProject.disabled = true;
    }
})


// form logic

btnNext_UpdateProject.disabled = true;

const form_projectUpdate = document.getElementById("project_update_form");
const formInp_upd = document.getElementById("projFormInp-upd");

btnNext_UpdateProject.onclick = () => {
    const projUpd = field_projupd;
    if (!projUpd || projUpd.length === 0) {
        btnNext_UpdateProject.disabled = true;
        return;
    }

    formInp_upd.value = projUpd;
    form_projectUpdate.submit();
}