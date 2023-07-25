const currentPath = window.location.pathname;

// Get all the anchor tags within the navigation bar
const navLinks = document.querySelectorAll('#sub-cat-nav a');

// Loop through each anchor tag to find the one with a matching href to the current path
navLinks.forEach(link => {
  if (link.getAttribute('href') == currentPath) {
    // Add the "active" class to the anchor tag with the matching href
    link.classList.add('active');
  }
});