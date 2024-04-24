function showLinksSection() {
    console.log("Kliknięto Links button");
    fetch('/links')
        .then(response => response.text())
        .then(html => {
            document.getElementById("search-album-section").style.display = "none";
            document.getElementById("about-section").style.display = "none";
            document.getElementById("links-section").innerHTML = html;
            document.getElementById("links-section").style.display = "block";
        })
        .catch(error => console.error('Error:', error));
}