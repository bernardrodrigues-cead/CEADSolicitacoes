$('input').addClass('form-control');
$('textarea').addClass('form-control');
// Teremos que remover a classe form-control, uma vez que checkboxes também são inputs
$('input[type="checkbox"]').removeClass('form-control').addClass('form-check-input');
$('select').addClass('form-select');