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

const btnCreateProject = document.getElementById("create_new_project");
const btnBack_CreateProjectPage_1_Name = document.getElementById("btn_back_crprojName");

disable_btnOpt = (btn) => {
    if (!btn.classList.contains("sel")) btn.classList.add("sel");
}

enable_btnOpt = (btn) => {
    if (btn.classList.contains("sel")) btn.classList.remove("sel");    
}

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

// btnCreateProject.click()