function generateAlbum() {
    console.log("kliknięto przycisk GENERATE ALBUM");
    fetch('/album-generator', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({})
    })
    .then(response => response.text()) // Odczytanie odpowiedzi jako tekst HTML
    .then(data => {
        // Tutaj możesz obsłużyć odpowiedź HTML, np. umieścić ją w odpowiednim elemencie na stronie
        document.getElementById('search-album-section').innerHTML = data;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

