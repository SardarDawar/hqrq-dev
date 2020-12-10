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

var curr_page_sel = '.page-wrap'

fixMainWinHeightImmediate(curr_page_sel);

window.onresize = () => {
    fixMainWinHeightImmediate(curr_page_sel);
}