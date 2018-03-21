var url = 'http://localhost:5000/push';

var timeTag = document.getElementById('time');

function poll() {
  var request = new XMLHttpRequest();
  request.open('GET', url, true);

  request.onload = function() {
    if (request.status >= 200 && request.status < 400) {
      // Success!
      var data = JSON.parse(request.responseText);
      console.log(data);
      lastPushTS = Date.parse(data.last_push);
      now = new Date().getTime();
      timeTag.innerText = Math.floor((now - lastPushTS) / 1000).toString();
    } else {
      // We reached our target server, but it returned an error
      console.log('Failed to poll server...')
    }
  };

  request.onerror = function() {
    // There was a connection error of some sort
  };

  request.send();

}

setInterval(poll, 1000);
