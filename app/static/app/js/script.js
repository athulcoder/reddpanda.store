
const bar = document.getElementById('bar');
const nav = document.getElementById('navbar');


if(bar.onclick){
}


function showNav(){
    nav.style.right=0;

}

function closeNav(){
    console.log('closed')
    nav.style.right ='-310px'
}

// Cart Quantity
// $('.increase-btn').click(function(){
//     var id = $(this).attr("pid").toString();
    
//     $.ajax({
//         type:'GET',
//         url: "/increase_quantity",
//         data:  {
//             prod_id:id
//         },
//         success: function(data){
//             document.getElementById('p'+id).innerHTML = data.quantity
//             document.getElementById('amount').innerHTML ='Rs. '+ data.amount
//             document.getElementById('total').innerHTML = 'Rs. ' +data.total
//         }
//     })
// })

// $('.decrease-btn').click(function(){
//     var id = $(this).attr("pid").toString();
    
//     $.ajax({
//         type:'GET',
//         url: "/decrease_quantity",
//         data:  {
//             prod_id:id
//         },
//         success: function(data){
//             document.getElementById('p'+id).innerHTML = data.quantity
//             document.getElementById('amount').innerHTML ='Rs. '+ data.amount
//             document.getElementById('total').innerHTML = 'Rs. ' +data.total
//         }
//     })
// })
// document.getElementById('increase-btn').addEventListener('click', () => {
//     const productId = document.getElementById('increase-btn').getAttribute('data-product-id');
//     updateQuantity(productId, 'increase');
// });

// document.getElementById('decrease-btn').addEventListener('click', () => {
//     const productId = document.getElementById('decrease-btn').getAttribute('data-product-id');
//     updateQuantity(productId, 'decrease');
//     console.log('derrrr')
// });

// function updateQuantity(productId, action) {
//     fetch(`/increase_quantity/${productId}/`, {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json', 'X-CSRFToken': '{{ csrf_token }}' },
//     })
//     .then(response => response.json())
//     .then(data => {
//         document.querySelector('p'+productId).textContent = data.quantity;
//     })
//     .catch(error => console.error('Error:', error));
// }