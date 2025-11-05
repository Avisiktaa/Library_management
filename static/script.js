// Dummy book data
const books = [
  { id: 1, title: "Data Structures in C", author: "Seymour Lipschutz", available: "Yes" },
  { id: 2, title: "Python Crash Course", author: "Eric Matthes", available: "No" },
  { id: 3, title: "Database System Concepts", author: "Henry Korth", available: "Yes" },
  { id: 4, title: "Operating System Concepts", author: "Abraham Silberschatz", available: "Yes" },
  { id: 5, title: "Let Us Java", author: "Yashavant Kanetkar", available: "No" }
];

function searchBooks() {
  const query = document.getElementById("searchBook").value.toLowerCase();
  const tableBody = document.getElementById("bookTable").querySelector("tbody");
  tableBody.innerHTML = "";

  const filteredBooks = books.filter(
    b => b.title.toLowerCase().includes(query) || b.author.toLowerCase().includes(query)
  );

  if (filteredBooks.length === 0) {
    tableBody.innerHTML = "<tr><td colspan='4'>No books found</td></tr>";
  } else {
    filteredBooks.forEach(b => {
      const row = `<tr>
        <td>${b.id}</td>
        <td>${b.title}</td>
        <td>${b.author}</td>
        <td>${b.available}</td>
      </tr>`;
      tableBody.innerHTML += row;
    });
  }
}
