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
