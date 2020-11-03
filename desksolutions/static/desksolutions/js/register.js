

$(document).ready(function () {


    const form = document.getElementById('register-form')
    // console.log(form)
    var form_message = document.getElementById('form-message')
    const success_message = document.getElementById('success-message')

    const handle_alert = (type, text) => {
        success_message.innerHTML += "<div class='alert alert-${type}' role='alert'>${text}</div>"
    }


    console.log(handle_alert)

    const title = document.getElementById('id_title')
    const email = document.getElementById('id_email')
    const description = document.getElementById('id_description')
    const phone = document.getElementById('id_phone')
    const url = document.getElementById('id_url')

    const csrf = document.getElementsByName('csrfmiddlewaretoken')
    console.log('csrf', csrf)

    const ajax_url = ""

    function block_form() {
        $("#loading").show();
        $('textarea').attr('disabled', 'disabled');
        $('input').attr('disabled', 'disabled');
    }

    function unblock_form() {
        $('#loading').hide();
        $('textarea').removeAttr('disabled');
        $('input').removeAttr('disabled');
        $('.errorlist').remove();
    }

    $("#register-form").submit(function (e) {
        e.preventDefault()
        console.log("submit pressed")

        $.ajax({
            type: 'POST',
            url: ajax_url,
            // data: {
            //     'csrfmiddlewaretoken': csrf[0].value,
            //     'title': title.value,
            //     'email': email.value,
            //     'description': description.value,
            //     'phone': phone.value,
            //     'url': url.value
            // },
            data: $(form).serialize(),
            success: function (response) {
                $("#form_ajax").show();
                setTimeout(function () {
                    $("#form_ajax").hide();
                }, 5000);
                var form_msg = response['form']
                if (form_msg) {
                    for (var i in form_msg) {
                        var error_message = "<p style='color: red'>" + form_msg[i] + "</p>"
                        var id = '#id_' + i;
                        $(id).parent('p').append(error_message);
                    }
                }
                else {
                    console.log("Form submitted")
                }

                // const sText = 'Successfully saved ${response.email}'
                // console.log(response.email)
                // handle_alert('success', sText)
            },
            error: function (error) {
                console.log(error)
            }
        })
    })
})