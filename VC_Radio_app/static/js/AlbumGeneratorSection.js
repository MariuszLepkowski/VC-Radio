function showSearchResults() {
    console.log("Kliknięto Search results");
    fetch('/album-generator')
        .then(response => response.text())
        .then(html => {
            document.getElementById("search-album-section").innerHTML = html;
            document.getElementById("search-album-section").style.display = "block";
        })
        .catch(error => console.error('Error:', error));
}






