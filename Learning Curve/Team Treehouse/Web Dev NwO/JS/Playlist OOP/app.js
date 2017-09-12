var playlist = new Playlist(); 

var allAlongTheWatchTower = new Song("All Along the Watch Tower", "Jimmy Hendrix", "3:50");
var letMeEntertainYou = new Song("Let Me Entertain You", "Robbie Williams", "3:00");

playlist.add(allAlongTheWatchTower);
playlist.add(letMeEntertainYou);

var playlistElement = document.getElementById('playlist');

playlist.renderInElement(playlistElement);

var playButton = document.getElementById("play");
playButton.onclick = function() {
  playlist.play();
  playlist.renderInElement(playlistElement);
}
var nextButton = document.getElementById("next");
nextButton.onclick = function() {
  playlist.next();
  playlist.renderInElement(playlistElement);
}
var stopButton = document.getElementById("stop");
stopButton.onclick = function() {
  playlist.stop();
  playlist.renderInElement(playlistElement);
}