

function showSearchResults() {
    console.log("Kliknięto VC Album Generator");
    console.log("searchResultsGenerated = " + searchResultsGenerated);
    console.log("clicksOnAboutBtnAfterSearchResultsGenerated = " + clicksOnAboutBtnAfterSearchResultsGenerated);

    // Sprawdź, czy użytkownik kliknął przycisk "About" i czy wyniki już zostały wygenerowane
    if (document.getElementById("about-button").classList.contains("active") && searchResultsGenerated && clicksOnAboutBtnAfterSearchResultsGenerated === 0){
        // Jeśli tak, ukryj sekcję "search-album-section"
        document.getElementById("search-album-section").style.display = "none";
        return;
    }

    if (searchResultsGenerated && clicksOnAboutBtnAfterSearchResultsGenerated > 0){
        document.getElementById("about-section").style.display = "none";
        document.getElementById("search-album-section").style.display = "block";
        return;
    }

    // Jeśli wyniki już zostały wygenerowane, nie wykonuj ponownie żądania
    if (searchResultsGenerated) {
        return;
    }

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


