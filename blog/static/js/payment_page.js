$(document).ready(function () {
    $('#pay').click(function () {
        $.ajax({
            type: 'POST',
            url: '/payment_page/',
            success: function (){
                return location ='/shop_list/'
            }
        })
    })
})