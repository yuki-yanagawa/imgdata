$(function(){
    $("#bt").on('click',function(){
        $.post("/getSensorData", {  }, function( data ){})
        .done(function(data){
            debugger
        })
    });
})
