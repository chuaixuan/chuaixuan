$(document).ready(function () {
    $("button").click(function(){
        var id = $(this).attr('id')
        var cl=$(this).attr('class')
        var count = $(this).attr('plus_less_number')
        $.ajax({
            url:'/pay_list/',
            type:'POST',
            data:{id:id,co:count},
            success:function(data){
                if (data.gift_count>0){
                    $('#original_price'+id).text(data.sumtotal.toFixed(1)+
                        '(原价:'+data.original_price.toFixed(1))
                }
                else{
                    $('#discounted_prices'+id).text(data.sumtotal.toFixed(1))
                }
                $("#"+id).next().text(data.number)
                $('#shop_count').text(data.total_count)
                $('#original_price'+id).text(data.original_price.toFixed(1))
                $('#discounted_prices'+id).text(data.sumtotal.toFixed(1))
                $('#total').text(data.total_price.toFixed(1))
                if(data.number==0){
                    $('#'+id).parents('tr').remove()
                }
            }
        })
    })
})