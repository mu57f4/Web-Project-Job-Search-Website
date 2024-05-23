document.addEventListener('DOMContentLoaded', function() {
    var numApplicantsElements = document.querySelectorAll('.num-applicants');

    numApplicantsElements.forEach(function(element) {
        var jobId = element.getAttribute('data-job-id');
        element.textContent = '0';
        fetch(`/job/${jobId}/num-applicants/`)
            .then(function(response) {
                if (!response.ok) {
                    throw new Error(`Failed to fetch number of applicants for job ${jobId}: ${response.statusText}`);
                }
                return response.json();
            })
            .then(function(data) {
                element.textContent = data.num_applicants;
            })
            .catch(function(error) {
                console.error(error);
            });
    });
});
