function showNotification({top = 0, right = 0, className, html}) {

  let notification = document.createElement('div');
  notification.className = "notification";
  if (className) {
    notification.classList.add(className);
  }

  notification.style.top = top + 'px';
  notification.style.right = right + 'px';

  notification.innerHTML = html;
  document.body.append(notification);

  setTimeout(() => notification.remove(), 1500);
}


function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

$('.btn-send-message').click(function() {
  var title = document.getElementById('formName').value;
  var number = document.getElementById('formNumber').value;
  var message = document.getElementById('formText').value;

  $.ajax({
    url: '/send-message/',
    method: 'POST',
    dataType: 'json',
    headers: {
      'X-CSRFToken': getCookie('csrftoken')
    },
    data: {
      title: title,
      number: number,
      message: message
    },
    success:
      function(e){
        $.notify("Успешно отправлено!", "success");
        document.getElementById('formName').value = "";
        document.getElementById('formNumber').value = "";
        document.getElementById('formText').value = "";
      },
    error: 
      function(e){
        $.notify("Произошла ошибка!", "warn");
        document.getElementById('formName').value = "";
        document.getElementById('formNumber').value = "";
        document.getElementById('formText').value = "";
      }
  })
})