$(document).ready(function () {
    // Test for placeholder support
    $.support.placeholder = (function () {
        var i = document.createElement('input');
        return 'placeholder' in i;
    })();

    // Hide labels by default if placeholders are supported
    if ($.support.placeholder) {
        $('.form-label').each(function () {
            $(this).addClass('js-hide-label');
        });

        // Code for adding/removing classes here
        $('.form-group').find('input, textarea').on('keyup blur focus', function (e) {

            // Cache our selectors
            var $this = $(this),
                $parent = $this.parent().find("label");

            switch (e.type) {
                case 'keyup': {
                    $parent.toggleClass('js-hide-label', $this.val() == '');
                } break;
                case 'blur': {
                    if ($this.val() == '') {
                        $parent.addClass('js-hide-label');
                    } else {
                        $parent.removeClass('js-hide-label').addClass('js-unhighlight-label');
                    }
                } break;
                case 'focus': {
                    if ($this.val() !== '') {
                        $parent.removeClass('js-unhighlight-label');
                    }
                } break;
                default: break;
            }
            // previous implementation with ifs
            /*if (e.type == 'keyup') {
                if( $this.val() == '' ) {
                    $parent.addClass('js-hide-label'); 
                } else {
                    $parent.removeClass('js-hide-label');   
                }                     
            } 
            else if (e.type == 'blur') {
                if( $this.val() == '' ) {
                    $parent.addClass('js-hide-label');
                } 
                else {
                    $parent.removeClass('js-hide-label').addClass('js-unhighlight-label');
                }
            } 
            else if (e.type == 'focus') {
                if( $this.val() !== '' ) {
                    $parent.removeClass('js-unhighlight-label');
                }
            }*/
        });
    }
});

/*jQuery---------------------------------------------------------------------------
$(function () {
    function after_form_submitted(data) {
        if (data.result == 'success') {
            $('form#reused_form').hide();
            $('#success_message').show();
            $('#error_message').hide();
        }
        else {
            $('#error_message').append('<ul></ul>');

            jQuery.each(data.errors, function (key, val) {
                $('#error_message ul').append('<li>' + key + ':' + val + '</li>');
            });
            $('#success_message').hide();
            $('#error_message').show();

            //reverse the response on the button
            $('button[type="button"]', $form).each(function () {
                $btn = $(this);
                label = $btn.prop('orig_label');
                if (label) {
                    $btn.prop('type', 'submit');
                    $btn.text(label);
                    $btn.prop('orig_label', '');
                }
            });

        }//else
    }

    $('#reused_form').submit(function (e) {
        e.preventDefault();

        $form = $(this);
        //show some response on the button
        $('button[type="submit"]', $form).each(function () {
            $btn = $(this);
            $btn.prop('type', 'button');
            $btn.prop('orig_label', $btn.text());
            $btn.text('Sending ...');
        });


        $.ajax({
            type: "POST",
            url: 'handler.php',
            data: $form.serialize(),
            success: after_form_submitted,
            dataType: 'json'
        });

    });
});*/
/*Validation-------------------------------------------------------------------------------*/
function validateName() {
    var Yname = document.getElementById('Yname').value;

    if (Yname.length == 0) {
        errorMessage('Name is required', 'Yname-error', 'red')
        return false;
    }

    if (!Yname.match(/^[a-zA-Z\s]*$/)) {
        errorMessage('Letters only', 'Yname-error', 'red')
        return false
    }

    errorMessage('Valid', 'Yname-error', 'green');
    return true;
}

function validateEmail() {

    var email = document.getElementById('e-mail').value;

    if (email.length == 0) {

        errorMessage('Email Invalid', 'Email-error', 'red');
        return false;

    }

    if (!email.match(/^[A-Za-z\._\-[0-9]*[@][A-Za-z]*[\.][a-z]{2,4}$/)) {

        errorMessage('Email Invalid. Please insert an "@" sign', 'Email-error', 'red');
        return false;

    }

    errorMessage('Valid', 'Email-error', 'green');
    return true;

}

function validateMsg() {

    var msg = document.getElementById('msg').value;

    if (msg.length == 0) {

        errorMessage('Please type a message. 200 characters max', 'Msg-error', 'red');
        return false;

    }

    if (msg.length == 200) {

        errorMessage('Please type a message. 200 characters max', 'Msg-error', 'red');
        return false;

    }

    errorMessage('Valid', 'Msg-error', 'green');
    return true;

}

function errorMessage(message, promptLocation, color) {
    document.getElementById(promptLocation).innerHTML = message;
    document.getElementById(promptLocation).style.color = color;
}

var nameValue = document.getElementById("Yname").value;
console.log('this is my string',nameValue)

