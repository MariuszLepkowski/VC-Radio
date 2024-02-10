// Get the modal
var playlistModal = document.getElementById('playlist-dialog');

// Variable to store the initial mouse position during dragging and resizing
var initialMouseX;
var initialMouseY;

// Variables to store the initial modal position and size during dragging and resizing
var initialModalX;
var initialModalY;
var initialModalWidth;
var initialModalHeight;

// Constants for resizing direction
const RESIZE_TOP = 1;
const RESIZE_RIGHT = 2;
const RESIZE_BOTTOM = 3;
const RESIZE_LEFT = 4;

// Variable to store the current resize direction
var resizeDirection;

// Variable to track if modal is being dragged or resized
var isDragging = false;
var isResizing = false;

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

    // Open playlist modal after adding a track
    openPlaylist();
}


// Event listener for mouse down event on the entire modal
playlistModal.addEventListener('mousedown', function(e) {
    // Prevent text selection while dragging or resizing
    e.preventDefault();

    // Store the initial mouse position and modal position and size
    initialMouseX = e.clientX;
    initialMouseY = e.clientY;
    initialModalX = playlistModal.offsetLeft;
    initialModalY = playlistModal.offsetTop;
    initialModalWidth = playlistModal.offsetWidth;
    initialModalHeight = playlistModal.offsetHeight;

    // Check if the mouse is over the resize handle
    var resizeHandle = e.target.closest('.resize-handle');
    if (resizeHandle) {
        // Set the resize direction based on the position of the resize handle
        if (resizeHandle.classList.contains('top')) {
            resizeDirection = RESIZE_TOP;
        } else if (resizeHandle.classList.contains('right')) {
            resizeDirection = RESIZE_RIGHT;
        } else if (resizeHandle.classList.contains('bottom')) {
            resizeDirection = RESIZE_BOTTOM;
        } else if (resizeHandle.classList.contains('left')) {
            resizeDirection = RESIZE_LEFT;
        }

        // Set resizing flag to true
        isResizing = true;

        // Add event listeners for mouse move and mouse up events
        document.addEventListener('mousemove', resizeModal);
        document.addEventListener('mouseup', releaseModal);
    } else {
        // Set dragging flag to true
        isDragging = true;

        // Add event listeners for mouse move and mouse up events
        document.addEventListener('mousemove', dragModal);
        document.addEventListener('mouseup', releaseModal);
    }
});

// Function to handle modal dragging
function dragModal(e) {
    if (!isDragging) return; // Exit if not dragging

    // Calculate the new modal position based on the mouse movement
    var deltaX = e.clientX - initialMouseX;
    var deltaY = e.clientY - initialMouseY;
    var newModalX = initialModalX + deltaX;
    var newModalY = initialModalY + deltaY;

    // Update the modal position
    playlistModal.style.left = newModalX + 'px';
    playlistModal.style.top = newModalY + 'px';
}

// Function to handle modal resizing
function resizeModal(e) {
    if (!isResizing) return; // Exit if not resizing

    // Calculate the change in mouse position
    var deltaX = e.clientX - initialMouseX;
    var deltaY = e.clientY - initialMouseY;

    // Calculate the new modal size based on the resize direction
    var newWidth = initialModalWidth + (resizeDirection === RESIZE_LEFT ? -deltaX : (resizeDirection === RESIZE_RIGHT ? deltaX : 0));
    var newHeight = initialModalHeight + (resizeDirection === RESIZE_TOP ? -deltaY : (resizeDirection === RESIZE_BOTTOM ? deltaY : 0));

    // Update the modal size
    playlistModal.style.width = newWidth + 'px';
    playlistModal.style.height = newHeight + 'px';
}

// Function to release the modal when mouse is up
function releaseModal() {
    // Reset dragging and resizing flags
    isDragging = false;
    isResizing = false;

    // Remove the event listeners for mouse move and mouse up events
    document.removeEventListener('mousemove', dragModal);
    document.removeEventListener('mousemove', resizeModal);
    document.removeEventListener('mouseup', releaseModal);
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
