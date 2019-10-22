var paymentForm = document.getElementById('paymentForm');
paymentForm.addEventListener("submit", payWithPaystack, false);

function payWithPaystack(e) {  
  e.preventDefault();
  var config = {
    key: 'pk_test_448800889e222223b1407c1bae6e57b612aeb8f0', // Replace with your public key
    email: document.getElementById("email-address").value,
    amount: document.getElementById("amount").value * 100,
    firstname: document.getElementById("first-name").value,
    lastname: document.getElementById("first-name").value,
    ref: ''+Math.floor((Math.random() * 1000000000) + 1), // generates a pseudo-unique reference. Please replace with a reference you generated. Or remove the line entirely so our API will generate one for you
    // label: "Optional string that replaces customer email"
    onClose: function(){
      alert('Window closed.');
    },
    callback: function(response){
      var message = 'Payment complete! Reference: ' + response.reference;
      alert(message);
    }
  };
  
  var paystackPopup = new Popup(config);
  paystackPopup.open();
}