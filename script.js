document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Hardcoded discharge summary
    const dischargeSummary = `
        <h2>Discharge Summary</h2>
        <p>Patient: John Doe</p>
        <p>Admission Date: 2024-05-01</p>
        <p>Discharge Date: 2024-05-10</p>
        <p class="section-title">Reason for Admission:</p>
        <p>Patient admitted with symptoms of severe chest pain and shortness of breath.</p>
        <p class="section-title">Diagnosis:</p>
        <p>Diagnosis confirmed as acute myocardial infarction (heart attack).</p>
        <p class="section-title">Treatment Administered:</p>
        <ul>
            <li>Immediate administration of aspirin and nitroglycerin.</li>
            <li>Emergency percutaneous coronary intervention (PCI) performed.</li>
            <li>Started on beta-blockers, ACE inhibitors, and statins.</li>
            <li>Cardiac rehabilitation initiated.</li>
        </ul>
        <p class="section-title">Hospital Course:</p>
        <p>Patient was monitored in the ICU for 3 days post-PCI. Transferred to a general ward on 2024-05-04. Patient showed significant improvement with stable vital signs and no further chest pain episodes.</p>
        <p class="section-title">Discharge Condition:</p>
        <p>Patient discharged in stable condition with instructions to continue medications, follow a heart-healthy diet, and attend follow-up appointments.</p>
        <p class="section-title">Follow-up Instructions:</p>
        <ul>
            <li>Follow-up appointment with cardiologist in 1 week.</li>
            <li>Continue prescribed medications: Aspirin 81 mg daily, Metoprolol 25 mg twice daily, Lisinopril 10 mg daily, Atorvastatin 40 mg daily.</li>
            <li>Engage in light physical activities as tolerated and gradually increase intensity based on the rehabilitation program.</li>
            <li>Avoid smoking and limit alcohol intake.</li>
            <li>Contact healthcare provider if experiencing any new or worsening symptoms such as chest pain, shortness of breath, or swelling in legs.</li>
        </ul>
        <p class="section-title">Contact Information:</p>
        <p>-</p>
    `;

    document.getElementById('output').innerHTML = dischargeSummary;

    // Show the "Download PDF" button
    document.getElementById('download-pdf-button').classList.remove('hidden');
    document.getElementById('timeline-button').classList.remove('hidden');
});

// Generate PDF function
document.getElementById('download-pdf-button').addEventListener('click', function() {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    // Get the HTML content
    const content = document.getElementById('output').innerHTML;
    const div = document.createElement('div');
    div.innerHTML = content;

    // Convert HTML to plain text (jsPDF doesn't support HTML directly)
    const textContent = div.innerText || div.textContent;

    // Add the text content to the PDF
    doc.text(textContent, 10, 10);

    // Save the PDF
    doc.save('discharge_summary.pdf');
});