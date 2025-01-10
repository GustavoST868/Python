function validateForm() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const email = document.getElementById("email").value;

    // simple validation logic,if the fields are empty
    if (username === "") {
        document.getElementById("usernameError").textContent = "Campo obrigatório";
        return;
    } else {
        document.getElementById("usernameError").textContent = "";
    }
    //if the password field is empty
    if (password === "") {
        document.getElementById("passwordError").textContent = "Campo obrigatório";
        return;
    } else {
        document.getElementById("passwordError").textContent = "";
    }
    //if the email field is empty
    if (email === "") {
        document.getElementById("emailError").textContent = "Campo obrigatório";
        return;
    } else {
        document.getElementById("emailError").textContent = "";
    }

    // if all fields are filled in , submit the form
    document.getElementById("registerForm").submit();
}
