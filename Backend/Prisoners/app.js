document
  .getElementById("searchForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const columnValue = document.getElementById("columnValue").value;

    fetch(
      `http://localhost:3000/documents?value=${encodeURIComponent(columnValue)}`
    ) // Replace with your API URL
      .then((response) => response.json())
      .then((data) => {
        const resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = ""; // Clear previous results

        if (data.length === 0) {
          resultsDiv.innerText = "No documents found";
        } else {
          data.forEach((doc) => {
            const docDiv = document.createElement("div");
            docDiv.innerText = JSON.stringify(doc, null, 2); // Display document details
            resultsDiv.appendChild(docDiv);
          });
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
