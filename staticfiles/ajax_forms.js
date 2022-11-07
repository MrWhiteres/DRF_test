$(function ($) {
    function clear_class_data() {
        if (!$('.alert-success').hasClass('d-none')) {
            $('.alert-success').addClass('d-none')
        }
        if (!$('.alert-danger').hasClass('d-none')) {
            $('.alert-danger').addClass('d-none')
        }
    }

    function add_success_data() {
        $('.alert-success').text("Продукт добавлен!").removeClass('d-none')
    }

    function add_error_data() {
        $('.alert-danger').text("Не все поля заполнены!").removeClass('d-none')
    }

    $('#product_ajax').submit(function (event) {
        event.preventDefault()
        $.ajax({
            type: "POST",
            url: this.action,
            data: new FormData(document.getElementById("product_ajax")),
            processData: false,
            contentType: false,
            cache: false,
            success: function (response) {
                if (response.status === 400) {
                    console.log(123)
                    clear_class_data()
                    add_error_data()
                }
                if (response.status === 201) {
                    console.log(321)
                    clear_class_data()
                    add_success_data()
                }
                console.log(response.status)
            },
            error: function (response) {
                clear_class_data()
                add_error_data()
            }
        })
    })
})