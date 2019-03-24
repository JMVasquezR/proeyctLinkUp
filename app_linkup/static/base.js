$(document).ready(function () {

    $('.button-act').on('click', function () {
        $('.button-act').removeClass('active')
        id = $(this).data('block')
        $('.block').hide()
        console.log('=>', id)
        $('#' + id).show()
    })

})