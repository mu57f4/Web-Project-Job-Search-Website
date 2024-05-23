function validateLoginForm(event) {
    event.preventDefault();

    var errorElement = document.getElementById('error');
    errorElement.textContent = '';

    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    if (email.trim() === "") {
        errorElement.textContent = 'Email cannot be empty';
        return false;
    }
    if (password.trim() === "") {
        errorElement.textContent = 'Password cannot be empty';
        return false;
    }

    event.target.submit();
    return true;
}


function validateSignupForm(event) {
    event.preventDefault();

    var errorElement = document.getElementById('error');
    errorElement.textContent = '';

    var password = document.getElementById("id_password1").value;
    var confirm_password = document.getElementById("id_password2").value;

    // Validate password strength
    var passwordPattern = /^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*])/;
    if (!passwordPattern.test(password)) {
        errorElement.textContent = 'Password must contain at least one letter, one number, and one special character';
        return false;
    }

    if (password.trim().length < 8){
        errorElement.textContent = 'Password must be at least 8 characters length';
        return false;
    }
    
    if (password != confirm_password){
        errorElement.textContent = 'Password does not match';
        return false;
    }

    event.target.submit();
    return true;
}

function validateUpdateResumeForm(event){
    event.preventDefault();

    var errorElement = document.getElementById('error');
    errorElement.textContent = '';

    var first_name = document.getElementById("id_first_name").value;
    var last_name = document.getElementById("id_last_name").value;
    var location = document.getElementById("id_location").value;
    var job_title = document.getElementById("id_job_title").value;

    if (first_name.trim() === "") {
        errorElement.textContent = 'First name cannot be empty';
        return false;
    }

    if (last_name.trim() === "") {
        errorElement.textContent = 'First name cannot be empty';
        return false;
    }

    if (location.trim() === "") {
        errorElement.textContent = 'First name cannot be empty';
        return false;
    }

    if (job_title.trim() === "") {
        errorElement.textContent = 'First name cannot be empty';
        return false;
    }

    event.target.submit();
    return true;
}


function validateSearchForm(event){
    event.preventDefault();

    var errorElement = document.getElementById('error');
    errorElement.textContent = '';

    var search_query = document.getElementById('id_title').value.trim();
    var location = document.getElementById('id_location').value.trim();
    var job_type = document.getElementById('id_job_type').value.trim();
    
    if (search_query === "" & location === "" & job_type === ""){
        errorElement.textContent = 'Please, enter at least one search filter';
        return false;
    }
    
    event.target.submit();
    return true;
}


function validateCreateJobForm(event){
    event.preventDefault();

    var errorElement = document.getElementById('error');
    errorElement.textContent = '';

    var description = document.getElementById('id_description').value.trim();

    var wordsCount = description.trim().split(/\s+/).length
    if (wordsCount < 20){
        errorElement.textContent = 'Description must contain at least 20 words';
        return false;
    }

    event.target.submit();
    return true;
}


function validateUpdateCompanyForm(event) {
    event.preventDefault();

    var errorElement = document.getElementById('error');
    errorElement.textContent = '';

    var name = document.getElementById("id_name").value;
    var est_date = document.getElementById("id_establish_date").value;
    var city = document.getElementById("id_city").value;
    var state = document.getElementById("id_state").value;

    if (name.trim() === "") {
        errorElement.textContent = 'Name cannot be empty';
        return false;
    }

    if (est_date.trim() === "") {
        errorElement.textContent = 'Establish Year cannot be empty';
        return false;
    }

    if (city.trim() === "") {
        errorElement.textContent = 'City cannot be empty';
        return false;
    }

    if (state.trim() === "") {
        errorElement.textContent = 'State cannot be empty';
        return false;
    }

    event.target.submit();
    return true;
}

function confirmDelete(event) {
    if (!confirm("Are you sure you want to delete this job? you can't undo this process")) {
        event.preventDefault();
    }
}