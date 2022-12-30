!function ($) {
    "use strict";

    var SweetAlert = function () {
    };

    //examples
    SweetAlert.prototype.init = function () {

        // LOGIN
        $('#validate_login_error').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops...',
                    text: 'Usuario o Contraseña incorrecta',
                }
            )
        });


        // INVOICE
        $('#Add_not_quanty_invoice').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops...',
                    text: 'No puede facturar en cero o vacio',
                    timer: 1500,
                    showConfirmButton:false
                }
            )
        });
        $('#Product_DoesNotExist').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops...',
                    text: 'El producto que busca no existe',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });







    },
        //init
        $.SweetAlert = new SweetAlert, $.SweetAlert.Constructor = SweetAlert
}(window.jQuery),

//initializing
    function ($) {
        "use strict";
        $.SweetAlert.init()
    }(window.jQuery);