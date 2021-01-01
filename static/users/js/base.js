// ####################################
//
// page 0
//
// ####################################


var curr_page_sel = '.page-wrap'

fixMainWinHeightImmediate(curr_page_sel);

window.onresize = () => {
    fixMainWinHeightImmediate(curr_page_sel);
}
