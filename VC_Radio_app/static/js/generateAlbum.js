let searchResultsGenerated = false;
let clicksOnAboutBtnAfterSearchResultsGenerated = 0;

function generateAlbum() {
    console.log("kliknięto przycisk GENERATE ALBUM");

    document.getElementById("loading-spinner").style.display = 'block'

    clicksOnAboutBtnAfterSearchResultsGenerated += 1;

    fetch('/album-generator', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({})
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('search-album-section').innerHTML = data;

        searchResultsGenerated = true;

        console.log("searchResultsGenerated = " + searchResultsGenerated);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

