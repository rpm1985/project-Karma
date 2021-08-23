$(init);

function init() {
  
  $("#addbtn").click( function() {
    
    addNewToDo();
  });
}

function addNewToDo() {
  var itemText = $("#todo-text").val();
  
  if( itemText !== "" ) {
    
    var item = $("<li>").addClass("todo-item").html( itemText );
    
    $("#todo-list").append( item );
    $("#todo-list").listview('refresh');
    
    //empty the text input
    $("#todo-text").val("");
  
    item.click( function(event) {
      addToCompleted( event.target );
    });
  }
  
}

function addToCompleted( item ) {
  
  $(item).remove();
  $("#completed-list").append( $(item) );
  
  $(item).off("click");
  $(item).click( function( event ) {
    addToDoFromCompleted( event.target );
  });
}

function addToDoFromCompleted( item ) {
  $(item).remove();
  $("#todo-list").append( $(item) );
  
  $(item).off("click");
  $(item).click( function( event ) {
    addToCompleted( event.target );
  });
}