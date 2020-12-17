// ####################################
//
// csrf cookie
//
// ####################################

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


var csrftoken = getCookie('csrftoken');

var headers = new Headers();
headers.append('X-CSRFToken', csrftoken);

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}





// ####################################
//
// common site functions/fixes
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


const mainContent = document.querySelector(".main-content");
const mainWin = document.querySelector(".main-win");

const btnLeftSidebarShowHide = document.getElementById("ls_show_hide");


toggleLeftSidebar = () => {
    if (!sdbrL.classList.contains("collapsed") && !sdbrL.classList.contains("sm-collapsed")) sdbrL.classList.add("collapsed");   // one of these classes must be present for this functionality
    if (sdbrL.classList.contains("show")) { 
        sdbrL.classList.remove("show");
        if (sdbrR) showRightSidebar();
    } else {
        sdbrL.classList.add("show");
        if (sdbrR) hideRightSidebar();
    }
}

if (btnLeftSidebarShowHide) btnLeftSidebarShowHide.onclick = toggleLeftSidebar

collapseLeftSidebar = () => {
    if (!sdbrL.classList.contains("collapsed") && !sdbrL.classList.contains("sm-collapsed")) sdbrL.classList.add("collapsed");    
    if (mainContent.classList.contains("small")) mainContent.classList.remove("small");    

    if (sdbrL.classList.contains("show")) { 
        sdbrL.classList.remove("show");
    }
    if (sdbrR) showRightSidebar();
}

expandLeftSidebar = () => {
    if (!sdbrL.classList.contains("collapsed") && !sdbrL.classList.contains("sm-collapsed")) sdbrL.classList.remove("collapsed");    
    if (!mainContent.classList.contains("small")) mainContent.classList.add("small");

    if (sdbrL.classList.contains("show")) { 
        sdbrL.classList.remove("show");
    }
    if (sdbrR) showRightSidebar();
}

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

hidePage = (sel, dir) => {
    if (dir === 'left') $(sel).css('transform', 'translateX(-100%').css('opacity', '0')
    else if (dir === 'right') $(sel).css('transform', 'translateX(100%').css('opacity', '0')
    else $(sel).css('transform', 'translateX(-100%').css('opacity', '0')

    setTimeout(function() {
        $(sel).addClass('hidden')
        $(sel).hide()
    }, 500)  
}

showPage = (sel, dir, callback) => {
    curr_page_sel = sel;

    $('.body-wrap')[0].scrollTop = 0
    
    $(sel).removeClass('hidden').show().css('transform', 'translateX(0%)').css('opacity', '1')
    
    fixMainWinHeight(sel);

    setTimeout(callback, 600)
}

if (sdbrR)
{
    hideRightSidebar = () => {
        if (!sdbrR.classList.contains("closed")) sdbrR.classList.add("closed");
    }
    
    showRightSidebar = () => {
        if (sdbrR.classList.contains("closed")) sdbrR.classList.remove("closed");
    }
    
    
    const sdbrR_id = sdbrR.querySelector(".side-id");
    
    const sdbrR_header = sdbrR.querySelector(".side-header");
    const $sdbrR_header = $('.sidebar.right .side-header')
    
    const sdbrR_content = sdbrR.querySelector(".side-content");
    const $sdbrR_content = $('.sidebar.right .side-content')
    
    
    setRightSidebarSecondaryContent = (page_sel, h_html, c_html, content_id, update_header, no_animation) => {
        
        const sdbrRsecondary_id = document.querySelector(`${page_sel} .sidebar-right-secondary .side-id`);
    
        const sdbrRsecondary_header = document.querySelector(`${page_sel} .sidebar-right-secondary .side-header`);
        const $sdbrRsecondary_header = $(`${page_sel} .sidebar-right-secondary .side-header`)
    
        const sdbrRsecondary_content = document.querySelector(`${page_sel} .sidebar-right-secondary .side-content`);
        const $sdbrRsecondary_content = $(`${page_sel} .sidebar-right-secondary .side-content`)
        
        if (sdbrRsecondary_id) {
            var curr_content_id = sdbrRsecondary_id.innerHTML;
            if (content_id !== null) {
                if (parseInt(curr_content_id) === parseInt(content_id)) return
                else {
                    sdbrRsecondary_id.innerHTML = content_id;
                    curr_content_id = content_id;
                }
            } else {
                sdbrRsecondary_id.innerHTML = "";
                curr_content_id = null;
            }
        }
    
        if (no_animation) {
            if (update_header && h_html) sdbrRsecondary_header.innerHTML = h_html
            if (c_html) sdbrRsecondary_content.innerHTML = c_html
        } else {
            if (update_header && h_html) {
                $sdbrRsecondary_header.stop().fadeOut(100, ()=> {
                    $sdbrRsecondary_header.html(h_html)
                    $sdbrRsecondary_header.fadeIn(50)
                })
            }
            if (c_html) {
                if (sdbrRsecondary_content.innerHTML !== c_html) {
                    $sdbrRsecondary_content.stop().fadeOut(100, ()=> {
                        $sdbrRsecondary_content.html(c_html)
                        $sdbrRsecondary_content.fadeIn(50)
                    })
                }
            }
        }
    
        fixMainWinHeight(page_sel);
    }
    
    
    setRightSidebarContent = (h_html, c_html, content_id, update_header, no_animation) => {

        if (sdbrR_id) {
            var curr_content_id = sdbrR_id.innerHTML;
            if (content_id !== null) {
                if (parseInt(curr_content_id) === parseInt(content_id)) return
                else {
                    sdbrR_id.innerHTML = content_id;
                    curr_content_id = content_id;
                }
            } else {
                sdbrR_id.innerHTML = "";
                curr_content_id = null;
            }
        }
        
        if (no_animation) {
            if (update_header && h_html) sdbrR_header.innerHTML = h_html
            if (c_html) sdbrR_content.innerHTML = c_html
        } else {
            if (update_header && h_html) {
                $sdbrR_header.stop().fadeOut(100, ()=> {
                    $sdbrR_header.html(h_html)
                    $sdbrR_header.fadeIn(50)
                })
            }
            if (c_html) {
                $sdbrR_content.stop().fadeOut(100, ()=> {
                    $sdbrR_content.html(c_html)
                    $sdbrR_content.fadeIn(50)
                })
            }
        }
    }    
}

disable_btnOpt = (btn) => {
    if (!btn.classList.contains("sel")) btn.classList.add("sel");
}

enable_btnOpt = (btn) => {
    if (btn.classList.contains("sel")) btn.classList.remove("sel");    
}
