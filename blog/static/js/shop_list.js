$(document).ready(function () {
    $('.add-btn').click(function () {
        var id=$(this).attr('id');
        $.ajax({
            url:"/shop_list/",
            type:'POST',
            data:{id:id},
            success:function (total_count) {
                $("#shop_count").text(total_count)
            }
        })
    })
})
