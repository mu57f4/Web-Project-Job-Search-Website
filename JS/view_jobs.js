const jobs = [
    {
        title: "Sofware Engineer",
        salary: "10,000",
        link: "jobs/software_engineer.html"
    },
    {
        title: "Data Analyst",
        salary: "7,000",
        link: "jobs/data_analyst.html"
    },
    {
        title: "UX/UI Designer",
        salary: "12,000",
        link: "jobs/ux_designer.html"
    },
    {
        title: "Project Manager",
        salary: "20,000",
        link: "jobs/project_manager.html"
    },
];

function display(){
    const container = document.getElementById('job');
    container.innerHTML = '';

    jobs.forEach(job => {
        const jobDiv = document.createElement('div');
        jobDiv.classList.add('css_class');
        jobDiv.innerHTML = `
            <div class="details">
                <h3><strong></strong> ${job.title}</h3>
                <p>Salary: ${job.salary}</p>
                <a href="${job.link}" class="borrow-button">Show details</a>
                <br><br>
            </div>
        `;
        container.appendChild(jobDiv);

    })
}

window.onload = display;