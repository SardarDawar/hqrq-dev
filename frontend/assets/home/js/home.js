// ####################################
//
// page 0
//
// ####################################


const sdbrL = document.querySelector(".sidebar.left")
const sdbrL_ddws = document.querySelectorAll(".opt-dropdown-wrap")

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

const btnCreateProject = document.getElementById("create_new_project");
const mainContent = document.querySelector(".main-content");

collapseLeftSidebar = () => {
    if (!sdbrL.classList.contains("collapsed")) sdbrL.classList.add("collapsed");    
    if (mainContent.classList.contains("small")) mainContent.classList.remove("small");    
}

expandLeftSidebar = () => {
    if (sdbrL.classList.contains("collapsed")) sdbrL.classList.remove("collapsed");    
    if (!mainContent.classList.contains("small")) mainContent.classList.add("small");
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

const sdbrR_header = document.querySelector(".sidebar.right .side-header");
const $sdbrR_header = $('.sidebar.right .side-header')

const sdbrR_content = document.querySelector(".sidebar.right .side-content");
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

const btnBack_CreateProjectPage_1_Name = document.getElementById("btn_back_crprojName");

btnCreateProject.onclick = () => {
    collapseLeftSidebar()
    hidePage('.page-wrap.pg0-wrap')
    showPage('.page-wrap.pg1-wrap')
    setRightSidebarContent(pg1_sdbrR_header, pg1_sdbrR_content)
}

btnBack_CreateProjectPage_1_Name.onclick = () => {
    expandLeftSidebar()
    hidePage('.page-wrap.pg1-wrap', 'right')
    showPage('.page-wrap.pg0-wrap')
    setRightSidebarContent(pg0_sdbrR_header, pg0_sdbrR_content)
}

// btnCreateProject.click()