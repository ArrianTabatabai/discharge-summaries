document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Hardcoded discharge summary and timeline
    const dischargeSummary = `
        <h2>Discharge Summary</h2>
        <p>Patient: John Doe</p>
        <p>Admission Date: 2024-05-01</p>
        <p>Discharge Date: 2024-05-10</p>
        <p>Summary: Patient admitted with symptoms X. Diagnosis confirmed as Y. Treated with Z. Discharged in stable condition.</p>
        <a href="timeline.html">View Patient Stay Timeline</a>
    `;

    document.getElementById('output').innerHTML = dischargeSummary;
});
