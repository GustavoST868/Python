//wait for the event,executes when it occurs
document.addEventListener('DOMContentLoaded', function () {
    var registerLink = document.querySelector('.register-link a');
    //reference to an element in html,waint for click element
    registerLink.addEventListener('click', function (event) {
        event.preventDefault(); 

        // Redirect to the register page
        window.location.href = '/register'; 
    });
});
