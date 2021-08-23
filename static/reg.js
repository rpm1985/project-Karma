function validateFName() {
  var Fname = document.getElementById('first-name').value;

  if (Fname.length == 0) {
    errorMessage('First name is required', 'Fname-error', 'red')
    return false;
  }

  if (!Fname.match(/^[a-zA-Z\s]*$/)) {
    errorMessage('Letters only', 'Fname-error', 'red')
    return false
  }

  errorMessage('Valid', 'Fname-error', 'green');
  return true;
}

function validateSName() {
  var Sname = document.getElementById('surname').value;

  if (Sname.length == 0) {
    errorMessage('Surname is required', 'Sname-error', 'red')
    return false;
  }

  if (!Sname.match(/^[a-zA-Z\s]*$/)) {
    errorMessage('Letters only', 'Sname-error', 'red')
    return false
  }

  errorMessage('Valid', 'Sname-error', 'green');
  return true;
}

function validateDOB() {
  var DOB = document.getElementById('DOB').value;

  if (DOB.length == 0) {
    errorMessage('Enter DOB', 'DOB-error', 'red')
    return false;
  }

  if (!DOB.match(/^([0-9]{2})\/([0-9]{2})\/([0-9]{4})$/)) {
    errorMessage('DD/MM/YYYY', 'DOB-error', 'red');
    return false;
  }

  errorMessage('Valid', 'DOB-error', 'green');
  return true;
}

function validatePostCode() {
  var Pc = document.getElementById('postcode').value;

  if (Pc.length == 0) {
    errorMessage('Enter Postcode', 'PC-error', 'red');
    return false;
  }

  if (!Pc.match(/^([a-zA-Z]{1,2}[0-9]{1,2})\s([0-9][a-zA-Z]{2})$/)) {
    errorMessage('AA11 1AA or aa11 1aa Please include a spacing.', 'PC-error', 'red');
    return false;
  }

  errorMessage('Valid', 'PC-error', 'green');
  return true;
}

function validatePhone() {

  var phone = document.getElementById('phone-number').value;

  if (phone.length == 0) {
    errorMessage('Phone number is required. Ex: 01231231234', 'Phone-error', 'red');
    return false;
  }

  if (phone.length != 11) {
    errorMessage('Include area code. Ex: 01231231234 11-digits only', 'Phone-error', 'red');
    return false;
  }

  if (!phone.match(/^[0-9]{11}$/)) {
    errorMessage('Only digits, please. Ex: 01231231234', 'Phone-error', 'red');
    return false;
  }

  errorMessage('Valid', 'Phone-error', 'green');
  return true;

}

function validateEmail() {

  var email = document.getElementById('e-mail').value;

  if (email.length == 0) {

    errorMessage('Email Invalid', 'Email-error', 'red');
    return false;

  }

  if (!email.match(/^[A-Za-z\._\-[0-9]*[@][A-Za-z]*[\.][a-z]{2,4}$/)) {

    errorMessage('Email Invalid. Please insert an "@" sign', 'Email-error', 'red');
    return false;

  }

  errorMessage('Valid', 'Email-error', 'green');
  return true;

}

// function validateReg() {
//     if (!validateFName() || !validateSName() || !validateDOB() || !validatePostCode() || !validatePhone() || !validateEmail()) {
//         jsShow('submit-error');
//         errorMessage('Please fix errors to submit.', 'submit-error', 'red');
//         setTimeout(function () { jsHide('submit-error'); }, 2000);
//         return false;
//     }
// }

// function jsShow(id) {
//     document.getElementById(id).style.display = 'block';
// }
//
// function jsHide(id) {
//     document.getElementById(id).style.display = 'none';
// }

function errorMessage(message, promptLocation, color) {
  document.getElementById(promptLocation).innerHTML = message;
  document.getElementById(promptLocation).style.color = color;
}
