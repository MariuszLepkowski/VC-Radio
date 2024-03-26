function showSearchResults() {
    console.log("Kliknięto VC Album Generator");

    // Ukryj sekcję "About", jeśli istnieje
    document.getElementById("about-section").style.display = "none";

    fetch('/album-generator')
        .then(response => response.text())
        .then(html => {
            // Wczytaj treść sekcji "VC Album Generator"
            document.getElementById("search-album-section").innerHTML = html;
            document.getElementById("search-album-section").style.display = "block";
        })
        .catch(error => console.error('Error:', error));
}

