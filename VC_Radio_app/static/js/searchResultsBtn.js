// Function to toggle search results visibility
function toggleSearchResults(button) {
    var searchResults = document.getElementById('search-results');
    if (searchResults.classList.contains('hidden')) {
        searchResults.classList.remove('hidden');
        button.textContent = 'Hide search results';
    } else {
        searchResults.classList.add('hidden');
        button.textContent = 'Show search results';
    }
}
// Function to toggle tracklist visibility
function toggleTracklist(button) {
    var tracklist = button.nextElementSibling;
    if (tracklist.classList.contains('hidden')) {
        tracklist.classList.remove('hidden');
        button.textContent = 'Hide tracklist';
    } else {
        tracklist.classList.add('hidden');
        button.textContent = 'Show tracklist';
    }
}