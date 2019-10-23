$(document).ready(function() {
    $('.js-example-basic-single').select2();
});

$(document).ready(function() {
    
    $('#copia').on('change', function(){
        var selectValor = '#' + $(this).val();
        $('#pai').children('div').hide();
        $('#pai').children(selectValor).show();    
    });

});

$(document).ready(function() {
    
    $('#usuario').on('change', function(){
        var selectValor = '#' + $(this).val();
        $('#pai2').children('div').hide();
        $('#pai2').children(selectValor).show();
    });

});    