// ####################################
//
// modals api
//
// ####################################

var infoModalCloseAction = null;

function showInfoModal_info(title, subtext, content, type, closeAction) {
    $('body').css('overflow', 'hidden');

    if (title!==null) $('#infoModalTitle').html(title)
    if (subtext!==null) $('#infoModalTitleSecondary').html(subtext)
    $('#infoModalTitleSpecial').html("").hide()

    if (content!==null) $('#infoModalContent-text').html(content).show();

    infoModalCloseAction = closeAction;
    if (type) setInfoModalType(type)

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

function setInfoModalType(type) {
    if (type === 'info') {
        $('#infoModalClose').attr("class", "btn btn-primary")
    } else if (type === 'error') {
        $('#infoModalClose').attr("class", "btn btn-danger")
    } else if (type === 'success') {
        $('#infoModalClose').attr("class", "btn btn-success")
    } else {
        $('#infoModalClose').attr("class", "btn btn-secondary")
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
    setInfoModalType();
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