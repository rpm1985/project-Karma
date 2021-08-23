function validateBdesc() {

  var bds = document.getElementById('BDesc').value;

  if (bds.length == 0) {

    errorMessage('Please type a brief description with 500 characters max', 'Bdesc-error', 'red');
    return false;

  }

  if (bds.length > 500) {

    errorMessage('Please type a brief description with 500 characters max', 'Bdesc-error', 'red');
    return false;

  }

  errorMessage('Valid', 'Bdesc-error', 'green');
  return true;

}


function errorMessage(message, promptLocation, color) {
  document.getElementById(promptLocation).innerHTML = message;
  document.getElementById(promptLocation).style.color = color;
}
