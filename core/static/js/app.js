$(function () {
    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
        }
    return cookieValue;
    }
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    setInterval(function (crsftoken) {
        $.ajax({
            url: "/update",
            type: 'POST',
            data: {'check': true
            },

            success: function (json) {
                if (json.result) {
                    $('#notify_icon').addClass("notification");
                    json._data = JSON.parse(json._data);
                    var doc = $.parseHTML(json._data);
                    $('#_data').html(doc);
                }
            }
        });
    }, 10000)
})


function isMobile() {
    if (navigator.userAgent.match(/Android/i) ||
        navigator.userAgent.match(/webOS/i) ||
        navigator.userAgent.match(/iPhone/i) ||
        navigator.userAgent.match(/iPad/i) ||
        navigator.userAgent.match(/iPod/i) ||
        navigator.userAgent.match(/BlackBerry/i) ||
        navigator.userAgent.match(/Windows Phone/i)) {
        return true;
    }
    else {
        return false;
    }
}

window.utils = {
    notification: function (message, duration) {
        var $new_message = $('<div class="notification"></div>'),
            $opened_messages = $('.notification');

        $new_message.html(message);

        if ($opened_messages.length) {
            var $last_message = $opened_messages.last(),
                top_offset = $last_message[0].offsetTop + $last_message.outerHeight() + 15;

            $new_message.css('top', top_offset + 'px')
        }

        $new_message.appendTo('body');
        $new_message.css('opacity'); //reflow hack for transition
        $new_message.addClass('notification--show');

        if (duration) {
            setTimeout(function () {
                $new_message.fadeOut(function () {
                    $new_message.remove();
                })
            }, duration);
        }

        $('.notification').click(function () {
            $(this).fadeOut(function () {
                $new_message.remove();
            })
        });
    },


    validateForm: function ($form) {
        $form.find('.form__field-alert').remove();

        function showAlert(message) {
            return $('<div class="form__field-alert">').html(message);
        }

        function checkRequiredField(field) {
            if (field.value) {
                return true;
            }
            else {
                showAlert('Обязательное поле').insertBefore(field);
                return false;
            }
        }

        function checkNumericField(field) {
            var val = field.value,
                regexp = /^[^a-zA-Z]*$/g;

            if (val !== '' && val.match(regexp)) {
                return true;
            }
            else {
                showAlert('Введите корректное значение').insertBefore(field);
                return false;
            }
        }

        function checkEmailField(field) {
            var val = field.value,
                regexp = /^[0-9a-zА-Яа-я\-\_\.]+\@[0-9a-zА-Яа-я-]{2,}\.[a-zА-Яа-я]{2,}$/i;

            if (val !== '' && val.match(regexp)) {
                return true;
            }
            else {
                showAlert('Введите корректный адрес').insertBefore(field);
                return false;
            }
        }

        function validateField(field) {
            if ($(field).hasClass('js-required')) {
                return checkRequiredField(field);
            }
            else if ($(field).hasClass('js-required-email')) {
                return checkEmailField(field);
            }
            else if ($(field).hasClass('js-required-numeric')) {
                return checkNumericField(field);
            }
            else {
                return true;
            }
        }

        var fields = $form.find('input, textarea'),
            isFormValid = true;

        $.each(fields, function (ind, el) {
            var checkedField = validateField(el);
            isFormValid = isFormValid && checkedField;
        });

        return isFormValid;
    }
}