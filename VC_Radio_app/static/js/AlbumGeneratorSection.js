function showSearchResults() {
    console.log("Kliknięto VC Album Generator");
    console.log("searchResultsGenerated = " + searchResultsGenerated);
    console.log("clicksOnAboutBtnAfterSearchResultsGenerated = " + clicksOnAboutBtnAfterSearchResultsGenerated);


    if (document.getElementById("about-button").classList.contains("active") && searchResultsGenerated && clicksOnAboutBtnAfterSearchResultsGenerated === 0){
        document.getElementById("search-album-section").style.display = "none";
        return;
    }

    if (searchResultsGenerated && clicksOnAboutBtnAfterSearchResultsGenerated > 0){
        document.getElementById("about-section").style.display = "none";
        document.getElementById("search-album-section").style.display = "block";
        return;
    }


    if (searchResultsGenerated) {
        return;
    }


    document.getElementById("about-section").style.display = "none";
    document.getElementById("links-section").style.display = "none";

    fetch('/album-generator')
        .then(response => response.text())
        .then(html => {
            document.getElementById("search-album-section").innerHTML = html;
            document.getElementById("search-album-section").style.display = "block";
        })
        .catch(error => console.error('Error:', error));
}
