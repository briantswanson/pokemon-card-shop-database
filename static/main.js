'use strict';


function showform(dowhat) {
    /*
    * four DIVS: browse, insert, update, delete
    * this function sets one visible the others not
    */
    if(dowhat == 'insert') {
        document.getElementById('browse').style.display = 'block';
        document.getElementById('insert').style.display = 'block';
    }  else { //by default display browse
        document.getElementById('browse').style.display = 'block';
        document.getElementById('insert').style.display = 'none';
    }
}


function insert() {
    showform('insert');
}

function browse() {
    showform('browse');
}


// LISTEN to the events
document.addEventListener('DOMContentLoaded', () => {
    showform('browse');


    const insertButton = document.getElementById('add_new');
    insertButton.addEventListener('click', insert);

    const cancelButton = document.getElementById('cancel');
    cancelButton.addEventListener('click', browse);

});