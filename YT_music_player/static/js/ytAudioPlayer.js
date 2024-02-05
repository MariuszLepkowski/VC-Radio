var duration;
var currentTime;
var player;
var isPlaying = false;

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
            }
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
    var progressPercentage = (currentTime / duration) * 100;
    progressBar.style.width = progressPercentage + '%';

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
