const form = document.getElementById('inspection-form');
form.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(form);
        fetch('/api/inspections',
        {
            method: 'POST',
            body: formData,
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                fetch('/api/inspections')
                    .then(response => response.json())
                    .then(data => {
                        const InspectionTable = document.getElementById('inspection-table');
                        inspectionTable.innerHTML = '';
                        data.forEach(inspection => {
                            const row = document.createElement('tr')
                                ;
                            row.innerHTML = `
<td>${inspection.food_item_id}</td>
<td>${inspetion.inspection_date}</td>
<td>${inspection.result}</td>
<td>${inspection.temperature}</td>
`;
                            inspectionTable.appendChild(row);
                        });
                    });
            });
});