// Get the modal
var playlistModal = document.getElementById('playlist-dialog');

// Function to open the playlist modal
function openPlaylist() {
    playlistModal.style.display = 'block';
}

// Function to close the playlist modal
function closePlaylist() {
    playlistModal.style.display = 'none';
}

// Function to add a track to the playlist
function addToPlaylist(trackUrl, trackTitle) {
    var playlist = document.getElementById("playlist");
    var li = document.createElement("li");
    var a = document.createElement("a");
    var button = document.createElement("button");

    a.href = trackUrl;
    a.textContent = trackTitle;

    button.textContent = "Remove";
    button.onclick = function() {
        li.remove();
    };

    li.appendChild(a);
    li.appendChild(button);
    playlist.appendChild(li);

    // Check if the playlist is empty
    if (playlist.children.length === 1) {
        openPlaylist(); // Open modal if it's the first track
    }
}

// Function to toggle tracklist visibility
function toggleTracklist(element) {
    var tracklist = element.nextElementSibling;
    if (tracklist.classList.contains('hidden')) {
        tracklist.classList.remove('hidden');
        element.textContent = 'Click to hide tracklist';
    } else {
        tracklist.classList.add('hidden');
        element.textContent = 'Click to show tracklist';
    }
}
