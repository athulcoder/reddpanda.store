cartBtn = document.getElementById("add-to-cart-btn");

cartBtn.addEventListener("click", addToCart);



// <!--  add to cart function  -->
// <!-- This JavaScript allows to call the python function in server  -->
// Function for add to cart
function addToCart() {
  let productID = this.getAttribute("data-product-uid");

  Url = "/add_to_cart/" + productID;
  // This JavaScript function will be triggered when the button is clicked
  fetch(Url) // Sends a GET request to the Python function's URL
    .then((response) => response.text())
    .then((data) => {
      // Handle the response data (optional)
      cartBtn.innerHTML = "GO TO CART";
      cartBtn.addEventListener("click", goToCart);
      showToast(data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function goToCart() {
  window.location.href = "../cart/";
}
// Toasting Function
function showToast(message) {
  // Create a new toast element
  var toastElement = document.createElement("div");
  toastElement.className = "toast";
  toastElement.textContent = message;

  // Append the toast element to the container
  var toastContainer = document.getElementById("toastContainer");
  toastContainer.appendChild(toastElement);

  // Show the toast for a few seconds, then remove it
  setTimeout(function () {
    toastElement.classList.add("show");

    setTimeout(function () {
      toastElement.classList.remove("show");
      toastElement.remove();
    }, 3000); // Adjust the display time (in milliseconds) as needed
  }, 100); // Delay showing the toast for a brief moment (to allow for CSS transition)
}


// Remove item from cart
