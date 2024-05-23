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


function newCustomer() {
    showform('insert');
}

function browseCustomers() {
    showform('browse');
}

// LISTEN to the events
document.addEventListener('DOMContentLoaded', () => {
    showform('browse');


    const insertButton = document.getElementById('addNew');
    insertButton.addEventListener('click', newCustomer);

    const browseButton = document.getElementById('cancel');
    browseButton.addEventListener('click', browseCustomers);
});