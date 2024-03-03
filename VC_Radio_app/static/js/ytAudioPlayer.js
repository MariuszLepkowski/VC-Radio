var duration;
var currentTime;
var player;
var isPlaying = false;
var previousVolume;

// Function called when the YouTube Iframe API is ready
function onYouTubeIframeAPIReady() {
    var container = document.getElementById("youtube-audio");
    var playerContainer = document.createElement("div");
    playerContainer.setAttribute("id", "youtube-player");
    container.appendChild(playerContainer);

    container.onclick = function () {
        togglePlayPause();
    };

    player = new YT.Player("youtube-player", {
        height: "0",
        width: "0",
        videoId: container.dataset.video,
        playerVars: {
            autoplay: container.dataset.autoplay,
            loop: container.dataset.loop
        },
        events: {
            onReady: function (event) {
                duration = player.getDuration();
                updateUI();
                setInterval(updateTimeInfo, 1000);
                startTitleChecking();
                updateVolumeIcon(); // Call the function when the player is ready
            },
            onStateChange: function (event) {
                if (event.data === YT.PlayerState.ENDED) {
                    isPlaying = false;
                } else if (event.data === YT.PlayerState.PLAYING) {
                    isPlaying = true;
                } else if (event.data === YT.PlayerState.PAUSED) {
                    isPlaying = false;
                }
                updateUI();
            },
            onError: function (event) {
                showAlternativeLink(event.target.getVideoData().video_id);
            },
            onVolumeChange: updateVolumeIcon // Call the function when volume changes
        }
    });
}

// Function to start checking for title availability
function startTitleChecking() {
    var titleCheckInterval = setInterval(function() {
        var titleElement = document.getElementById('title');
        if (titleElement && titleElement.textContent.trim() !== "") {
            clearInterval(titleCheckInterval);
        } else {
            showAlternativeLink(document.getElementById("youtube-audio").dataset.video);
        }
    }, 1000);
}

// Function to check if an element has a title
function hasTitle(element) {
    if (!element) {
        return false;
    }

    var titleElement = element.querySelector('#title');
    return titleElement && titleElement.textContent.trim() !== "";
}

// Function to toggle play/pause
function togglePlayPause() {
    if (isPlaying) {
        player.pauseVideo();
    } else {
        player.playVideo();
    }
    isPlaying = !isPlaying;
    updateUI();
}

// Function to update time information
function updateTimeInfo() {
    currentTime = player.getCurrentTime();
    updateUI();
}

// Function to update the UI
function updateUI() {
    var durationElement = document.getElementById('timeInfo');
    var progressBar = document.getElementById('progressBar');
    var progressThumb = document.getElementById('progressThumb');
    var progressContainer = document.getElementById('progressContainer');
    var progressPercentage = (currentTime / duration) * 100;
    progressBar.style.width = progressPercentage + '%';
    progressThumb.style.left = (progressPercentage - 1) + '%';

    var youtubeIcon = document.getElementById('youtube-icon');
    youtubeIcon.style.backgroundImage = 'url(' + (isPlaying ? '/static/assets/img/pause.png' : '/static/assets/img/play.png') + ')';

    var formattedTime = formatTime(currentTime) + ' / ' + formatTime(duration);
    durationElement.textContent = formattedTime;

    updateTitle();
}

// Function to update the video title
function updateTitle() {
    var currentTitleElement = document.getElementById('title');
    var videoData = player.getVideoData();
    var title = videoData.title;

    currentTitleElement.textContent = title;
}

// Function to format time
function formatTime(time) {
    var minutes = Math.floor(time / 60);
    var seconds = Math.floor(time % 60);
    return minutes + ':' + (seconds < 10 ? '0' : '') + seconds;
}

// Function to seek to a specific time
function seekToTime(event) {
    var progressBar = document.getElementById('progressContainer');
    var clickPosition = event.clientX - progressBar.getBoundingClientRect().left;
    var percentage = clickPosition / progressBar.clientWidth;
    var seekTime = duration * percentage;
    player.seekTo(seekTime);
}

// Function to display an alternative link
function showAlternativeLink(videoId) {
    var alternativeLinkDiv = document.getElementById('alternative-link');
    alternativeLinkDiv.style.display = 'block';
    alternativeLinkDiv.innerHTML = '<p>The audio/video available only on <a href="https://www.youtube.com/watch?v=' + videoId + '" target="_blank"><img id="youtube-logo" src="static/assets/img/YouTubeLogo.png" alt="YouTube Logo"> <br> Click to listen/watch.</a></p>';

    var playerContainer = document.getElementById('container');
    playerContainer.style.display = 'none';

    var loadingDiv = document.getElementById('title');
    loadingDiv.style.display = 'none';
}

// Load modal and close button
var modal = document.getElementById('playlist-modal');
var closeBtn = document.getElementsByClassName('close')[0];

// Function to display modal
function displayModal() {
    modal.style.display = 'block';
}

// Function to close modal when close button or outside modal is clicked
closeBtn.onclick = function() {
    modal.style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}

// Function to display audio player
function displayAudioPlayer(videoId) {
    var modal = document.getElementById('audio-player-modal');
    var iframe = document.getElementById('audio-player-iframe');
    iframe.src = 'https://www.youtube.com/embed/' + videoId;
    modal.style.display = 'block';
}

// Function to close audio player
function closeAudioPlayer() {
    var modal = document.getElementById('audio-player-modal');
    modal.style.display = 'none';
}

// Get all "Play track" buttons
var playTrackButtons = document.querySelectorAll('.play-track-btn');

// Add click event handling for each button
playTrackButtons.forEach(function(button) {
    button.addEventListener('click', function() {
        var videoId = button.dataset.url;
        displayAudioPlayer(videoId);
    });
});

// Function to update volume button based on volume slider value
function updateVolumeButton() {
    var volumeSlider = document.getElementById('volumeSlider');
    var volumeButton = document.getElementById('volumeButton');

    if (player.isMuted() || player.getVolume() === 0) {
        volumeButton.classList.add('muted');
    } else {
        volumeButton.classList.remove('muted');
    }
}

// Call the function to update volume button after each volume change
document.getElementById('volumeSlider').addEventListener('input', updateVolumeButton);

// Function to change volume
function changeVolume(volume) {
    var volumeSlider = document.getElementById('volumeSlider');
    var volumeButton = document.getElementById('volumeButton');

    if (volume === 0) {
        volumeButton.classList.add('muted');
        volumeSlider.value = 0;
        player.mute();
    } else {
        volumeButton.classList.remove('muted');
        volumeSlider.value = volume;
        player.unMute();
    }

    player.setVolume(volume);
}

// Function to update volume slider value based on current player volume
function updateVolumeSlider() {
    var volumeSlider = document.getElementById('volumeSlider');
    if (player && volumeSlider) {
        var currentVolume = player.getVolume();
        volumeSlider.value = currentVolume;
    }
}

// Call the function to update volume slider after the player is ready
player.addEventListener('onReady', updateVolumeSlider);



var previousVolume = 100;

function toggleMute() {
    var volumeSlider = document.getElementById('volumeSlider');
    var volumeButton = document.getElementById('volumeButton');

    if (player.isMuted()) {

        player.unMute();
        volumeButton.classList.remove('muted');
        volumeSlider.value = previousVolume;
        player.setVolume(previousVolume);
    } else {
        previousVolume = volumeSlider.value;
        player.mute();
        volumeButton.classList.add('muted');
        volumeSlider.value = 0;
    }
}

// Add event handling for the volume icon click
document.getElementById('volume-icon').addEventListener('click', function() {
    toggleMute();
});

// Function to update volume icon based on volume slider value
function updateVolumeIcon() {
    var volumeIcon = document.getElementById('volume-icon');
    var volumeSlider = document.getElementById('volumeSlider');
    var volumeValue = parseInt(volumeSlider.value);

    if (volumeValue === 0) {
        volumeIcon.src = '/static/assets/img/volume-mute.png';
    } else {
        volumeIcon.src = '/static/assets/img/volume-up.png';
    }
}

// Add event listener to update volume icon when volume slider value changes
document.getElementById('volumeSlider').addEventListener('input', updateVolumeIcon);

// Call the function to update volume icon after the player is ready
player.addEventListener('onReady', updateVolumeIcon);



// Function to move the progress thumb when clicked
function moveProgressThumb(event) {
    // Get the progress container element
    var progressBar = document.getElementById('progressContainer');

    // Calculate the click position relative to the progress container
    var clickPosition = event.clientX - progressBar.getBoundingClientRect().left;

    // Calculate the percentage of the progress
    var percentage = clickPosition / progressBar.clientWidth;

    // Calculate the seek time based on the percentage
    var seekTime = duration * percentage;

    // Seek to the calculated time in the video player
    player.seekTo(seekTime);

    // Update the position of the progress thumb
    var progressThumb = document.getElementById('progressThumb');
    progressThumb.style.left = percentage * 100 + '%';
}

// Add event listener for clicking on the progress container to move the progress thumb
document.getElementById('progressContainer').addEventListener('click', moveProgressThumb);

// Function for smooth transition of the progress thumb
function smoothMoveProgressThumb() {
    // Get the progress thumb element
    var progressThumb = document.getElementById('progressThumb');

    // Add transition property for smooth movement
    progressThumb.style.transition = 'left 0.1s linear';
}

// Add event listener for transition end to remove transition property
document.getElementById('progressThumb').addEventListener('transitionend', function() {
    // Remove the transition property after transition ends
    this.style.transition = '';
});

// Function to update the time on seeking
function updateTimeOnSeek() {
    // Get the current time of the video player
    currentTime = player.getCurrentTime();

    // Update the UI to reflect the new time
    updateUI();
}

// Add event listener for transition end to update time on seeking
document.getElementById('progressThumb').addEventListener('transitionend', updateTimeOnSeek);

// Function to continuously update the progress thumb position based on the current time
function updateProgressThumb() {
    // Calculate the percentage progress of the video
    var progressPercentage = (currentTime / duration) * 100;

    // Get the progress thumb element
    var progressThumb = document.getElementById('progressThumb');

    // Set the left position of the progress thumb to match the progress percentage
    progressThumb.style.left = progressPercentage + '%';
}

// Call the function to update the progress thumb position continuously
setInterval(updateProgressThumb, 100); // Adjust the interval for smoother movement



// Function to move the progress thumb and progress bar together when clicked and dragged
function moveProgressThumbAndBar(event) {
    // Prevent default behavior to avoid text selection
    event.preventDefault();

    // Get the progress container element
    var progressBar = document.getElementById('progressContainer');

    // Calculate the click position relative to the progress container
    var clickPosition = event.clientX - progressBar.getBoundingClientRect().left;

    // Calculate the percentage of the progress
    var percentage = clickPosition / progressBar.clientWidth;

    // Limit the percentage to be within 0 and 1
    percentage = Math.max(0, Math.min(1, percentage));

    // Calculate the seek time based on the percentage
    var seekTime = duration * percentage;

    // Seek to the calculated time in the video player
    player.seekTo(seekTime);

    // Update the position of the progress thumb and progress bar
    var progressThumb = document.getElementById('progressThumb');
    progressThumb.style.left = percentage * 100 + '%';
    var progressBar = document.getElementById('progressBar');
    progressBar.style.width = percentage * 100 + '%';
}

// Add event listener for mousedown to start dragging the progress thumb and progress bar
document.getElementById('progressContainer').addEventListener('mousedown', function(event) {
    // Call the function to move the progress thumb and progress bar together
    moveProgressThumbAndBar(event);

    // Add event listener for mousemove to continue dragging
    document.addEventListener('mousemove', moveProgressThumbAndBar);

    // Function to handle mouseup event
    function handleMouseUp() {
        // Remove event listeners for mousemove and mouseup when dragging stops
        document.removeEventListener('mousemove', moveProgressThumbAndBar);
        document.removeEventListener('mouseup', handleMouseUp);
    }

    // Add event listener for mouseup to stop dragging
    document.addEventListener('mouseup', handleMouseUp);
});


function updateVolumeIcon() {
    var volumeButton = document.getElementById('volumeButton');
    if (volumeButton) {
        var volumeSlider = document.getElementById('volumeSlider');
        var volumeValue = parseInt(volumeSlider.value);

        if (volumeValue === 0) {
            volumeButton.classList.add('muted');
        } else {
            volumeButton.classList.remove('muted');
        }
    }
}


document.getElementById('volumeSlider').addEventListener('input', updateVolumeIcon);
