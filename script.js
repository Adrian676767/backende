async function loadStudents() {

    const sort = document.getElementById("sortSelect").value;

const response = await fetch(`/students?sort=${sort}`);
    const students = await response.json();

    const table = document.getElementById("studentsTable");

    table.innerHTML = "";

    students.forEach(student => {

        table.innerHTML += `
            <tr>
                <td>${student.id}</td>
                <td>${student.name}</td>
                <td>${student.age}</td>
                <td>${student.vyska} cm</td>
            </tr>
        `;
    });
}

loadStudents();
