$(document).ready(function () {
    $("button").click(function(){
        var id = $(this).attr('id')
        var cl=$(this).attr('class')
        var count = $(this).attr('plus_less_number')
        $.ajax({
            url:'/pay_list/',
            type:'POST',
            data:{id:id,co:count},
            success:function(total){
                $("#"+id).next().text(total.number)
                $('#shop_count').text(total.total_count)
                $('#a'+id).text(total.original_price)
                if(total.number==0){
                    $('#'+id).parents('tr').remove()
                }
            }
        })
    })
})