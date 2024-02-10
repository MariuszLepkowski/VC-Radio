// Get the modal
var modal = document.getElementById('playlist-modal');

// Get the <span> element that closes the modal
var closeBtn = document.getElementsByClassName('close')[0];

// Function to open the playlist modal
function openPlaylistModal() {
    modal.style.display = 'block';
}

// Function to close the playlist modal
function closePlaylistModal() {
    modal.style.display = 'none';
}

// When the user clicks on <span> (x), close the modal
closeBtn.onclick = function () {
    closePlaylistModal();
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target === modal) {
        closePlaylistModal();
    }
};

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
        openPlaylistModal(); // Open modal if it's the first track
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
