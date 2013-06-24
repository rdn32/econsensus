/*
Disables an element (e.g. submit button) of
the "once" class the first time it is clicked
*/
$(document).ready(function() {
    $(".once").live("click", function(e) {
        this.disabled = true;
    });
});
