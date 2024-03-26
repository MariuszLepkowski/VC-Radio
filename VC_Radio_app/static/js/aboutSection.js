document.addEventListener('DOMContentLoaded', function() {
    const sidebarButtons = document.querySelectorAll('.nav-link');

    sidebarButtons.forEach(button => {
        button.addEventListener('click', function() {
            document.getElementById('welcome-section').style.display = 'none';
        });
    });
});


function showHomeView() {
    console.log("Kliknięto About");
    fetch('/about')
        .then(response => response.text())
        .then(html => {
        // Ukryj sekcję VC Album Generator
            document.getElementById("search-album-section").style.display = "none";
            document.getElementById("about-section").innerHTML = html;
            document.getElementById("about-section").style.display = "block";
        })
        .catch(error => console.error('Error:', error));
}