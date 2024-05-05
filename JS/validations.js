function validateLoginForm(event) {
    event.preventDefault(); 

    document.getElementById('username_error').textContent = ''; 
    document.getElementById('password_error').textContent = '';

    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;    
    
    if (
    username.trim() === "") {
        document.getElementById('username_error').textContent = 'Error, Username cannot be emtpy';
        return false;
    }
    if (password.trim() === "") {
        document.getElementById('password_error').textContent = 'Error, Password cannot be empty';
        return false;
    }
    
    return true; 
}


function validateSignupForm(event) {
    event.preventDefault();

    document.getElementById('username_error').textContent = '';
    document.getElementById('password_error').textContent = '';
    document.getElementById('email_error').textContent = '';

    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var confirm_password = document.getElementById("confirm_password").value;
    var email = document.getElementById("email").value;

    if (username.trim() === ""){
        document.getElementById('username_error').textContent = 'Error, Username cannot be empty';
        return false;
    }
    if (password.trim() === "") {
        document.getElementById('password_error').textContent = 'Error, Password cannot be empty';
        return false;
    }

    if (password.trim().length < 8){
        document.getElementById('password_error').textContent = 'Error, Password must be at least 8 characters';
        return false;
    }
    
    if (password != confirm_password){
        document.getElementById('password_error').textContent = 'Error, Password does not match';
        return false;
    }

    if (email.trim() === "") {
        document.getElementById('email_error').textContent = 'Error, Email cannot be empty';
        return false;
    }

    return true;
}

function validateAddNewJobForm(event) {
    event.preventDefault();

    document.getElementById('job_id_error').textContent = '';
    document.getElementById('job_title_error').textContent = '';
    document.getElementById('salary_error').textContent = '';
    document.getElementById('company_name_error').textContent = '';
    document.getElementById('description_error').textContent = '';
    document.getElementById('years_of_experience_error').textContent = '';

    var job_id = document.getElementById("job_id").value;
    var job_title = document.getElementById("job_title").value;
    var salary = document.getElementById("salary").value;
    var company_name = document.getElementById("company_name").value;
    var description = document.getElementById("description").value;
    var years_of_experience = document.getElementById("years_of_experience").value;

    if (job_id.trim() === ""){
        document.getElementById('job_id_error').textContent = 'Job ID cannot be empty';
        return false;
    }
    
    if (job_title.trim() === ""){
        document.getElementById('job_title_error').textContent = 'Job title cannot be empty';
        return false;
    }
    
    if (salary.trim() === "" || isNaN(parseFloat(salary))){
        document.getElementById('salary_error').textContent = 'Enter a valid salary in numbers';
        return false;
    } 
    
    if (company_name.trim() === "") {
        document.getElementById('company_name_error').textContent = 'Please enter a Company Name';
        return false;
    }

    var wordsCount = description.trim().split(/\s+/).length
    if (wordsCount < 20){
        document.getElementById('description_error').textContent = 'Description must contain at least 20 words';
        return false;
    }

    if (years_of_experience.trim() === "" || isNaN(parseInt(years_of_experience))) {
        document.getElementById('years_of_experience_error').textContent = 'Enter a valid numeric Years of Experience';
        return false;
    }
    return true;
}

function validateApplyForm(event) {
    event.preventDefault();

    document.getElementById('applicant_name_error').textContent = '';
    document.getElementById('applicant_email_error').textContent = '';

    var name = document.getElementById("applicant_name").value;
    var email = document.getElementById("applicant_email").value;
    var resume = document.getElementById("resume").value;

    if (name.trim() === ""){
        document.getElementById('applicant_name_error').textContent = 'Name cannot be empty';
        return false;
    }
    if (email.trim() === ""){
        document.getElementById('applicant_email_error').textContent = 'Email cannot be empty';
        return false;
    }
    if (resume.trim() === ""){
        alert('Upload your resume');
        return false;
    }
    
    return true;
}

function validateEditJobForm(event) {
    event.preventDefault();

    document.getElementById('job_title_error').textContent = '';
    document.getElementById('salary_error').textContent = '';
    document.getElementById('company_name_error').textContent = '';
    document.getElementById('description_error').textContent = '';
    document.getElementById('years_of_experience_error').textContent = '';

    var job_title = document.getElementById("job_title").value;
    var salary = document.getElementById("salary").value;
    var company_name = document.getElementById("company_name").value;
    var description = document.getElementById("description").value;
    var years_of_experience = document.getElementById("years_of_experience").value;
    
    if (job_title.trim() === ""){
        document.getElementById('job_title_error').textContent = 'Job title cannot be empty';
        return false;
    }
    
    if (salary.trim() === "" || isNaN(parseFloat(salary))){
        document.getElementById('salary_error').textContent = 'Enter a valid salary in numbers';
        return false;
    } 
    
    if (company_name.trim() === "") {
        document.getElementById('company_name_error').textContent = 'Please enter a Company Name';
        alert();
        return false;
    }

    var wordsCount = description.trim().split(/\s+/).length
    if (wordsCount < 20){
        document.getElementById('description_error').textContent = 'Description must contain at least 20 words';
        return false;
    }

    if (years_of_experience.trim() === "" || isNaN(parseInt(years_of_experience))) {
        document.getElementById('years_of_experience_error').textContent = 'Enter a valid numeric Years of Experience';
        return false;
    }
    return true;
}

function validateSearchForm(event){
    event.preventDefault();

    document.getElementById('search_query_error').textContent = '';
    var search_query = document.getElementById('search_query').value.trim();

    if (search_query === ""){
        document.getElementById('search_query_error').textContent = 'Error, Enter a job title';
        return false;
    }

}

