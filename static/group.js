function validategroupName(){
  var GroupName = document.getElementById('GroupName').value;

  if (GroupName.length == 0) {
    errorMessage('Group name is required','GroupName-error','red')
    return false;
  }

  if (!GroupName.match(/^[a-zA-Z\s]*$/)){
    errorMessage('Letters only', 'GroupName-error','red')
    return false
  }

  errorMessage('Valid','GroupName-error','green');
  return true;
}

function validategroupDescription() {

    var GroupDescription = document.getElementById('GroupDescription').value;

    if (GroupDescription.length == 0) {

        errorMessage('Please type a message. 200 characters max', 'GroupDescription-error', 'red');
        return false;

    }

    if (GroupDescription.length > 200) {

        errorMessage('Please type a message. 200 characters max', 'GroupDescription-error', 'red');
        return false;

    }

    errorMessage('Valid', 'GroupDescription-error', 'green');
    return true;

}

function validategroupArea(){
  var GroupArea = document.getElementById('GroupArea').value;

  if (GroupArea.length == 0) {
    errorMessage('Group area is required','GroupArea-error','red')
    return false;
  }

  if (!GroupArea.match(/^[a-zA-Z\s]*$/)){
    errorMessage('Letters only', 'GroupArea-error','red')
    return false
  }

  errorMessage('Valid','GroupArea-error','green');
  return true;
}
