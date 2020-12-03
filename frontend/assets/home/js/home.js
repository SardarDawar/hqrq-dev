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

hidePage = (sel, dir) => {
    if (dir === 'left') $(sel).css('transform', 'translateX(-100%').css('opacity', '0')
    else if (dir === 'right') $(sel).css('transform', 'translateX(100%').css('opacity', '0')
    else $(sel).css('transform', 'translateX(-100%').css('opacity', '0')

    setTimeout(function() {
        $(sel).addClass('hidden')
        $(sel).hide()
    }, 500)  
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

var curr_page_sel = '.page-wrap.pg0-wrap'

fixMainWinHeight(curr_page_sel);

window.onresize = () => {
    fixMainWinHeightImmediate(curr_page_sel);
}

showPage = (sel, dir) => {
    curr_page_sel = sel;

    $('.body-wrap')[0].scrollTop = 0
    
    $(sel).removeClass('hidden').show().css('transform', 'translateX(0%)').css('opacity', '1')
    
    fixMainWinHeight(sel);
}


const sdbrR_header = sdbrR.querySelector(".side-header");
const $sdbrR_header = $('.sidebar.right .side-header')

const sdbrR_content = sdbrR.querySelector(".side-content");
const $sdbrR_content = $('.sidebar.right .side-content')



setRightSidebarSecondaryContent = (page_sel, h_html, c_html) => {

    const sdbrRsecondary_header = document.querySelector(`${page_sel} .sidebar-right-secondary .side-header`);
    const $sdbrRsecondary_header = $(`${page_sel} .sidebar-right-secondary .side-header`)

    const sdbrRsecondary_content = document.querySelector(`${page_sel} .sidebar-right-secondary .side-content`);
    const $sdbrRsecondary_content = $(`${page_sel} .sidebar-right-secondary .side-content`)

    if (sdbrRsecondary_header.innerHTML !== h_html) {
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

    fixMainWinHeight(page_sel);
}

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
    setRightSidebarSecondaryContent('.page-wrap.pg1-wrap', pg1_sdbrR_header, pg1_sdbrR_content)
    setRightSidebarContent(pg1_sdbrR_header, pg1_sdbrR_content)
}

btnBack_CreateProjectPage_1_Name.onclick = () => {
    enable_btnOpt(btnCreateProject)
    expandLeftSidebar()
    hidePage('.page-wrap.pg1-wrap', 'right')
    showPage('.page-wrap.pg0-wrap')
    setRightSidebarSecondaryContent('.page-wrap.pg0-wrap', pg0_sdbrR_header, pg0_sdbrR_content)
    setRightSidebarContent(pg0_sdbrR_header, pg0_sdbrR_content)
}

btnNext_CreateProjectPage_1_Name.onclick = () => {
    hidePage('.page-wrap.pg1-wrap', 'left')
    showPage('.page-wrap.pg2-wrap')
    var pg2_selection_check = false;
    pg2vischs.forEach(el => {    
        if (el.classList.contains("sel")) {
            pg2_selection_check = true;
            const el_id = el.getAttribute("id");
            if (el_id in pg2_visch_help_dict) {
                setRightSidebarSecondaryContent('.page-wrap.pg2-wrap', pg2_visch_help_dict[el_id][0], pg2_visch_help_dict[el_id][1])
                setRightSidebarContent(pg2_visch_help_dict[el_id][0], pg2_visch_help_dict[el_id][1])
            }            
        }
    })
    // set this only if no option on pg2 has been selected
    if (!pg2_selection_check) 
    {
        setRightSidebarSecondaryContent('.page-wrap.pg2-wrap', pg2_sdbrR_header, pg2_sdbrR_content)
        setRightSidebarContent(pg2_sdbrR_header, pg2_sdbrR_content)
    }
}

btnBack_CreateProjectPage_2_DocType.onclick = () => {
    hidePage('.page-wrap.pg2-wrap', 'right')
    showPage('.page-wrap.pg1-wrap')
    setRightSidebarSecondaryContent('.page-wrap.pg1-wrap', pg1_sdbrR_header, pg1_sdbrR_content)
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
            setRightSidebarSecondaryContent('.page-wrap.pg2-wrap', pg2_sdbrR_header, pg2_sdbrR_content)
            setRightSidebarContent(pg2_sdbrR_header, pg2_sdbrR_content)
        } else {
            clearAllVischsSel(pg2vischs, el);
            el.classList.add("sel")
            const el_id = el.getAttribute("id");
            if (el_id in pg2_visch_help_dict) {
                setRightSidebarSecondaryContent('.page-wrap.pg2-wrap', pg2_visch_help_dict[el_id][0], pg2_visch_help_dict[el_id][1])
                setRightSidebarContent(pg2_visch_help_dict[el_id][0], pg2_visch_help_dict[el_id][1])
            }
        }
    }
})