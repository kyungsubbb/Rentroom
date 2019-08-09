(function($) {
    'use strict';
    $(function() {
        $('.cancel-link').on('click', function(e) {
            e.preventDefault();
            if (window.location.search.indexOf('&_popup=1') === -1) {
<<<<<<< HEAD
<<<<<<< HEAD
                window.history.back();  // Go back if not a popup.
=======
                window.history.back(); // Go back if not a popup.
>>>>>>> dacd6c24a3172085053810ea16d8bf730b721346
=======
                window.history.back(); // Go back if not a popup.
>>>>>>> 134c83ce8c0895bebd16f54ec13d3f1f39921512
            } else {
                window.close(); // Otherwise, close the popup.
            }
        });
    });
})(django.jQuery);
