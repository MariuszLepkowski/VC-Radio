document.addEventListener('DOMContentLoaded', function() {
    const sidebarButtons = document.querySelectorAll('.nav-link');

    sidebarButtons.forEach(button => {
        button.addEventListener('click', function() {
            document.getElementById('welcome-section').style.display = 'none';
        });
    });
});


function showHomeView() {
    console.log("Kliknięto Home");
    fetch('/home')
        .then(response => response.text())
        .then(html => {
            document.getElementById("search-album-section").innerHTML = html;
            document.getElementById("search-album-section").style.display = "block";
        })
        .catch(error => console.error('Error:', error));
}