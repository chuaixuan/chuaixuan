$(document).ready(function () {
    $('#confirm').click(function () {

        $.ajax({
            type: 'POST',
            url: '/payment_page/',
            success: function () {
                 location = '/shop_list';
            }
        })
    });

});