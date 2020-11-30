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
    const field = document.getElementById(el.dataset.fieldid);
    el.onclick = () => {
        VoiceToText(field);        
    }
});

const mainContent = document.querySelector(".main-content");

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

hidePage = (sel, dir) => {
    if (dir === 'left') $(sel).css('transform', 'translateX(-100%').css('opacity', '0')
    else if (dir === 'right') $(sel).css('transform', 'translateX(100%').css('opacity', '0')
    else $(sel).css('transform', 'translateX(-100%').css('opacity', '0')

    setTimeout(function() {$(sel).addClass('hidden')}, 500)    
}

showPage = (sel, dir) => {
    $(sel).removeClass('hidden').css('transform', 'translateX(0%)').css('opacity', '1')
}

const sdbrR_header = sdbrR.querySelector(".side-header");
const $sdbrR_header = $('.sidebar.right .side-header')

const sdbrR_content = sdbrR.querySelector(".side-content");
const $sdbrR_content = $('.sidebar.right .side-content')

setRightSidebarContent = (h_html, c_html) => {
    if (sdbrR_header.innerHTML !== h_html) {
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

disable_btnOpt = (btn) => {
    if (!btn.classList.contains("sel")) btn.classList.add("sel");
}

enable_btnOpt = (btn) => {
    if (btn.classList.contains("sel")) btn.classList.remove("sel");    
}

const btnCreateProject = document.getElementById("create_new_project");
const btnBack_CreateProjectPage_1_Name = document.getElementById("btn_back_crprojName");
const btnNext_CreateProjectPage_1_Name = document.getElementById("btn_next_crprojName");
const btnBack_CreateProjectPage_2_DocType = document.getElementById("btn_back_crprojDocType");
const btnNext_CreateProjectPage_2_DocType = document.getElementById("btn_next_crprojDocType");

btnCreateProject.onclick = () => {
    disable_btnOpt(btnCreateProject)
    collapseLeftSidebar()
    hidePage('.page-wrap.pg0-wrap')
    showPage('.page-wrap.pg1-wrap')
    setRightSidebarContent(pg1_sdbrR_header, pg1_sdbrR_content)
}

btnBack_CreateProjectPage_1_Name.onclick = () => {
    enable_btnOpt(btnCreateProject)
    expandLeftSidebar()
    hidePage('.page-wrap.pg1-wrap', 'right')
    showPage('.page-wrap.pg0-wrap')
    setRightSidebarContent(pg0_sdbrR_header, pg0_sdbrR_content)
}

btnNext_CreateProjectPage_1_Name.onclick = () => {
    hidePage('.page-wrap.pg1-wrap', 'left')
    showPage('.page-wrap.pg2-wrap')
    var pg2_selection_check = false;
    pg2vischs.forEach(el => {    
        if (el.classList.contains("sel")) {
            console.log("what")
            pg2_selection_check = true;
            const el_id = el.getAttribute("id");
            if (el_id in pg2_visch_help_dict) {
                setRightSidebarContent(pg2_visch_help_dict[el_id][0], pg2_visch_help_dict[el_id][1])
            }            
        }
    })
    // set this only if no option on pg2 has been selected
    if (!pg2_selection_check) setRightSidebarContent(pg2_sdbrR_header, pg2_sdbrR_content)
}

btnBack_CreateProjectPage_2_DocType.onclick = () => {
    hidePage('.page-wrap.pg2-wrap', 'right')
    showPage('.page-wrap.pg1-wrap')
    setRightSidebarContent(pg1_sdbrR_header, pg1_sdbrR_content)
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

pg2vischs.forEach(el => {    
    el.onclick = () => {
        if (el.classList.contains("sel")) {
            clearAllVischsSel(pg2vischs);
            setRightSidebarContent(pg2_sdbrR_header, pg2_sdbrR_content)
        } else {
            clearAllVischsSel(pg2vischs, el);
            el.classList.add("sel")
            const el_id = el.getAttribute("id");
            if (el_id in pg2_visch_help_dict) {
                setRightSidebarContent(pg2_visch_help_dict[el_id][0], pg2_visch_help_dict[el_id][1])
            }
        }
    }
})