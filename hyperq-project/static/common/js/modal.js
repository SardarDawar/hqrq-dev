// ####################################
//
// modals api
//
// ####################################

var infoModalCloseAction = null;

function showInfoModal_info(title, subtext, content, closeAction) {
    $('body').css('overflow', 'hidden');

    if (title!==null) $('#infoModalTitle').html(title)
    if (subtext!==null) $('#infoModalTitleSecondary').html(subtext)
    $('#infoModalTitleSpecial').html("").hide()

    if (content!==null) $('#infoModalContent-text').html(content).show();

    infoModalCloseAction = closeAction;

    $('#infoModal').modal('show')
    $('#infoModal').modal('handleUpdate')
}

function hideInfoModal() {
    $('#infoModal').modal('hide')
    if ($('#infoModal').hasClass('show'))
    {
        setTimeout(hideInfoModal, 250)
    }
}

$('#infoModal').on('hidden.bs.modal', function(){
    // enable only if other modals are not visible
    if(!$('#infoModal').hasClass('show'))
    {
        $('body').css('overflow', 'auto');
    }
    $('#infoModalTitle').html('')
    $('#infoModalTitleSecondary').html('')
    $('#infoModalTitleSpecial').html("").hide()
    $('#infoModalContent-text').html('').hide()
    $('#infoModalHeader-close').hide();
}).on('shown.bs.modal', function(){
    $('body').css('overflow', 'hidden');
})

$('#infoModal').on('hide.bs.modal', function(){
    if (infoModalCloseAction) infoModalCloseAction();
    infoModalCloseAction = null;
})

function showInfoModal_infoSpecial(special, content, closeAction) {
    $('body').css('overflow', 'hidden');

    $('#infoModalTitle').html("")
    $('#infoModalTitleSecondary').html("")
    $('#infoModalTitleSpecial').html(special).show()

    if (content!==null) $('#infoModalContent-text').html(content).show();

    infoModalCloseAction = closeAction;

    $('#infoModal').modal('show')
    $('#infoModal').modal('handleUpdate')
}


// showInfoModal_info("Title", "", "Content", ()=>{
//     console.log("Modal Closed");
// })