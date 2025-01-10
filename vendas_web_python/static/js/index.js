//wait for the event,executes when it occurs
document.addEventListener("DOMContentLoaded", function() {
  // related to user icon element
  var userIcon = document.getElementById("user-icon");

  // waint for click event
  userIcon.addEventListener("click", function() {
      // Redirect to the login page
      window.location.href = "/login";
  });
});
  
