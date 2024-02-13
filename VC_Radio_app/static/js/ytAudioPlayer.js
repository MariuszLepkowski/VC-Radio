var duration;
var currentTime;
var player;
var isPlaying = false;
var previousVolume; // Zmienna globalna do przechowywania poprzedniej głośności

function onYouTubeIframeAPIReady() {
    var e = document.getElementById("youtube-audio");
    var a = document.createElement("div");
    a.setAttribute("id", "youtube-player");
    e.appendChild(a);

    e.onclick = function () {
        togglePlayPause();
    };

    player = new YT.Player("youtube-player", {
        height: "0",
        width: "0",
        videoId: e.dataset.video,
        playerVars: {
            autoplay: e.dataset.autoplay,
            loop: e.dataset.loop
        },
        events: {
            onReady: function (e) {
                duration = player.getDuration();
                updateUI();
                setInterval(updateTimeInfo, 1000);
                startTitleChecking();
                updateVolumeIcon(); // Dodajemy wywołanie funkcji w momencie gotowości odtwarzacza
            },
            onStateChange: function (e) {
                if (e.data === YT.PlayerState.ENDED) {
                    isPlaying = false;
                } else if (e.data === YT.PlayerState.PLAYING) {
                    isPlaying = true;
                } else if (e.data === YT.PlayerState.PAUSED) {
                    isPlaying = false;
                }
                updateUI();
            },
            onError: function (e) {
                showAlternativeLink(e.target.getVideoData().video_id);
            },
            onVolumeChange: updateVolumeIcon // Dodane wywołanie funkcji przy zmianie głośności
        }
    });
}

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

function hasTitle(element) {
    if (!element) {
        return false;
    }

    var titleElement = element.querySelector('#title');
    return titleElement && titleElement.textContent.trim() !== "";
}

function togglePlayPause() {
    if (isPlaying) {
        player.pauseVideo();
    } else {
        player.playVideo();
    }
    isPlaying = !isPlaying;
    updateUI();
}

function updateTimeInfo() {
    currentTime = player.getCurrentTime();
    updateUI();
}

function updateUI() {
    var durationElement = document.getElementById('timeInfo');
    var progressBar = document.getElementById('progressBar');
    var progressThumb = document.getElementById('progressThumb'); // Dodajemy pobranie elementu kółka
    var progressContainer = document.getElementById('progressContainer'); // Dodajemy pobranie kontenera paska postępu
    var progressPercentage = (currentTime / duration) * 100;
    progressBar.style.width = progressPercentage + '%';
    progressThumb.style.left = (progressPercentage - 1) + '%'; // Ustawiamy pozycję kółka (odejmujemy połowę szerokości)

    var youtubeIcon = document.getElementById('youtube-icon');
    youtubeIcon.style.backgroundImage = 'url(' + (isPlaying ? '/static/assets/img/pause.png' : '/static/assets/img/play.png') + ')';

    var formattedTime = formatTime(currentTime) + ' / ' + formatTime(duration);
    durationElement.textContent = formattedTime;

    updateTitle();
}

function updateTitle() {
    var currentTitleElement = document.getElementById('title');
    var videoData = player.getVideoData();
    var title = videoData.title;

    currentTitleElement.textContent = title;
}

function formatTime(time) {
    var minutes = Math.floor(time / 60);
    var seconds = Math.floor(time % 60);
    return minutes + ':' + (seconds < 10 ? '0' : '') + seconds;
}

function seekToTime(event) {
    var progressBar = document.getElementById('progressContainer');
    var clickPosition = event.clientX - progressBar.getBoundingClientRect().left;
    var percentage = clickPosition / progressBar.clientWidth;
    var seekTime = duration * percentage;
    player.seekTo(seekTime);
}

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

// Function to add track to playlist
function addToPlaylist(url) {
    // Get existing playlist from browser's memory (if exists)
    var playlist = JSON.parse(localStorage.getItem('playlist')) || [];
    // Add new URL to playlist
    playlist.push(url);
    // Save updated playlist back to browser's memory
    localStorage.setItem('playlist', JSON.stringify(playlist));
    // Display playlist
    displayPlaylist(playlist);
    // Display modal if it's the first track added
    if (playlist.length === 1) {
        displayModal();
    }
    // Confirmation message for adding to playlist
    alert('Track has been added to your playlist!');
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
        volumeButton.classList.add('muted'); // Dodaj klasę muted dla przycisku głośności
        volumeSlider.value = 0; // Ustaw suwak głośności na zero
        player.mute(); // Wycisz odtwarzacz, jeśli głośność wynosi zero
    } else {
        volumeButton.classList.remove('muted'); // Usuń klasę muted dla przycisku głośności
        volumeSlider.value = volume; // Ustaw wartość suwaka głośności na aktualną wartość
        player.unMute(); // Włącz dźwięk, jeśli głośność jest większa niż zero
    }

    player.setVolume(volume); // Ustaw głośność odtwarzacza na nową wartość
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

// Function to toggle mute/unmute
function toggleMute() {
    var volumeSlider = document.getElementById('volumeSlider');
    var volumeButton = document.getElementById('volumeButton');

    if (player.isMuted()) {
        player.unMute(); // Wyłącz tryb wyciszenia
        volumeButton.classList.remove('muted'); // Usuń klasę muted dla przycisku głośności
        volumeSlider.value = previousVolume; // Przywróć poprzednią wartość głośności
        changeVolume(previousVolume); // Ustaw poprzednią wartość głośności
    } else {
        previousVolume = volumeSlider.value; // Zapamiętaj poprzednią wartość głośności
        player.mute(); // Włącz tryb wyciszenia
        volumeButton.classList.add('muted'); // Dodaj klasę muted dla przycisku głośności
        volumeSlider.value = 0; // Ustaw suwak głośności na zero
        changeVolume(0); // Ustaw głośność na zero
    }
}

// Add event handling for the volume icon click
document.getElementById('volume-icon').addEventListener('click', function() {
    toggleMute();
});

// Function to update volume icon based on player's mute status and volume level
function updateVolumeIcon() {
    var volumeButton = document.getElementById('volumeButton');
    var volumeIcon = document.getElementById('volume-icon');
    var volumeSlider = document.getElementById('volumeSlider'); // Dodajemy pobranie elementu suwaka głośności

    if (player.isMuted() || player.getVolume() === 0 || volumeSlider.value == 0) {
        volumeIcon.src = '/static/assets/img/volume-mute.png'; // Set the icon to muted when the player is muted or volume is 0
    } else {
        volumeIcon.src = '/static/assets/img/volume-up.png'; // Otherwise, set the icon to volume up
    }
}

// Call the function to update volume icon after each volume change
player.addEventListener('onVolumeChange', updateVolumeIcon);

// Call the function to update volume icon after the player is ready
player.addEventListener('onReady', updateVolumeIcon);
