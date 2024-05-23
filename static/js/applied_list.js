document.addEventListener('DOMContentLoaded', function() {
    fetchApplications();
});

function fetchApplications() {
    fetch("/applied/ajax/applied/")
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('applications-table-body');
            tableBody.innerHTML = '';
            data.forEach(applied_job => {
                const row = document.createElement('tr');

                row.innerHTML = `
                    <td>${applied_job.title}</td>
                    <td>${applied_job.location}</td>
                    <td>${applied_job.salary}</td>
                    <td>${applied_job.job_type}</td>
                    <td>${applied_job.applied_date}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => {
            const messages = document.getElementById('messages');
            messages.innerHTML = `<div class="alert-warning"><strong>Error loading applications</strong></div>`;
        });
}
