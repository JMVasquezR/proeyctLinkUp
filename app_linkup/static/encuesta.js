$(document).ready(function () {

    $('#block_encuesta').show()
    $('#block_detalle').hide()

    const form = $("#form")

    $('.descripcion').hide()
    $('#categoria').change(function () {
        let id = $(this).val()
        $('.descripcion').hide()
        $('#descripcion_' + id).show()
    })


    form.on('submit', function (e) {
        e.preventDefault();

        var formData = new FormData(this);

        ls_data = {
            "cliente": {
                "nombre": formData.get('nombre'),
                "apellido": formData.get('apellido'),
                "fecha_de_nacimiento": formData.get('fecha_de_nacimiento'),
                "numero_de_documento": formData.get('numero_de_documento'),
                "correo": formData.get('correo'),
                "tipo_documento": formData.get('tipo_documento')
            },
            "categoria": formData.get('categoria'),
            "motivo_o_porque": formData.get('motivo_o_porque')
        }

        $.ajax({
            type: "POST",
            headers: {
                'X-CSRFToken': CSRF_TOKEN,
            },
            url: form.data('url'),
            data: JSON.stringify(ls_data),
            processData: false,
            contentType: "application/json",
            success: function (data) {
                window.location.href = form.data('url-refresh')

            },
            error: function (result) {
                console.log(result)
            }

        })
    });

})