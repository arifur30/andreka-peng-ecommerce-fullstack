// Get the menu icon and navigation bar elements
const menuIcon = document.getElementById('menu');
const navbar = document.getElementById('navbar');

// Add a click event listener to the menu icon
menuIcon.addEventListener('click', () => {
    // Toggle the visibility of the navigation bar
    navbar.classList.add('active');
});


// Get the close icon element
const closeIcon = document.getElementById('close');

// Add a click event listener to the close icon
closeIcon.addEventListener('click', () => {
    // Remove the 'active' class from the navigation bar
    navbar.classList.remove('active');
});