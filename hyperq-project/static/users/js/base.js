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

fixMainWinHeight = (sel) => {
    if (window.innerWidth <= 750)
    {
        setTimeout(()=> {
            $('.main-win').css('min-height', `${$(sel).height()}px`)
            $('.main-win').css('max-height', `${$(sel).height()}px`)
            
        }, 500)
    }
    else {
        $('.main-win').css('min-height', `unset`)
        $('.main-win').css('max-height', `unset`)
        setTimeout(()=> {
            $('.main-win').css('min-height', `unset`)
            $('.main-win').css('max-height', `unset`)
    
        }, 550)
    }
}

fixMainWinHeightImmediate = (sel) => {
    if (window.innerWidth <= 750)
    {
        setTimeout(() => {
            $('.main-win').css('min-height', `${$(sel).height()}px`)
            $('.main-win').css('max-height', `${$(sel).height()}px`)
    
        }, 200)
    }
    else {
        $('.main-win').css('min-height', `unset`)
        $('.main-win').css('max-height', `unset`)
        setTimeout(() => {
            $('.main-win').css('min-height', `unset`)
            $('.main-win').css('max-height', `unset`)
    
        }, 250)
    }
}

var curr_page_sel = '.page-wrap'

fixMainWinHeightImmediate(curr_page_sel);

window.onresize = () => {
    fixMainWinHeightImmediate(curr_page_sel);
}


const btnLeftSidebarShowHide = document.getElementById("ls_show_hide");


toggleLeftSidebar = () => {
    if (!sdbrL.classList.contains("sm-collapsed")) sdbrL.classList.add("sm-collapsed");   // this class must be present for this functionality
    if (sdbrL.classList.contains("show")) { 
        sdbrL.classList.remove("show");
    } else {
        sdbrL.classList.add("show");
    }
}

btnLeftSidebarShowHide.onclick = toggleLeftSidebar