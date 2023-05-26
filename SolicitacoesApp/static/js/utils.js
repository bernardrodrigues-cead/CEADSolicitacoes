function hideFields(){
    $('#id_data_agendamento').parent().hide();
    $('#id_horario_agendamento').parent().hide();
    $('#id_duracao_estimada').parent().hide();
    $('#id_equipamentos').parent().hide();
    $('#id_equipe_cead').parent().hide();
    $('#id_numero_participantes').parent().hide()
}

function showFields(){
    $('#id_data_agendamento').parent().show();
    $('#id_horario_agendamento').parent().show();
    $('#id_duracao_estimada').parent().show();
    $('#id_equipamentos').parent().show();
    $('#id_equipe_cead').parent().show();
    $('#id_numero_participantes').parent().show()
}

$(document).ready(function() {
    hideFields();
    $('#id_outro').hide();
    
    // Adiciona a classe bootstrap form-control a todos os inputs e textareas
    $('input, textarea').addClass('form-control');

    // Adiciona a classe bootstrap form-select a todos os select elements
    $('select').addClass('form-select');

    // Remove a classe form-control, uma vez que checkboxes e radios também são inputs
    // Adiciona a classe bootstrap form-check-input e me-2 a todos checkboxes e radio buttons
    $('input[type="checkbox"], input[type="radio"]').removeClass('form-control').addClass('form-check-input me-2');

    // Adiciona a classe bootstrap mb-1 a todos os labels
    $('label').addClass('mb-1')

    // Adiciona a classe bootstrap d-flex e justify-content-evenly a todos os radio buttons
    $('input[type="radio"]').parent().parent().parent().addClass('d-flex justify-content-evenly');

    // Acrescenta um asterisco vermelho na frente de todo label de campo obrigatório
    $('input[required').each(function() {
        var label = $('label[for="' + $(this).attr('id') + '"]');
        label.append('<span class="required">*</span>');
    });

    // Adiciona a classe bootstrap card a toda div contendo grupos de inputs
    $('.main-form').children('div').addClass('card p-4 mb-4');

    // Adiciona margem inferior entre cada input
    $('.main-form').children().children('div').addClass('mb-3');

    // Define tamanho rows=3 para todo textarea
    $('textarea').attr('rows', 3);

    // Mostra ou não os campos em caso de gravações no estúdio
    $('#id_servicos_0, #id_servicos_2').on('change', function(){
        if($('#id_servicos_0').is(':checked') || $('#id_servicos_2').is(':checked')){
            showFields();
        } else {
            hideFields();
        }
    });

    $('#id_servicos_6').on('change', function(){
        if($(this).is(':checked')){
            $('#id_outro').attr('required', true).show();
        } else {
            $('#id_outro').attr('required', false).hide();
        }
    })

    // Attach a resize event handler to the window
    $(window).resize(function() {
        var screenWidth = $(window).width();
        
        // Perform actions based on screen width
        if (screenWidth < 992) {
            // Screen width is less than 768px
            $('.main-form').removeClass('w-50');
        } else {
            $('.main-form').addClass('w-50');
        }
    });
})