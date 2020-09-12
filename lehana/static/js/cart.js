
// we are getting all of our buttons in a variable
var updateBtns = document.getElementsByClassName('update-cart');
for (var i = 0; i < updateBtns.length; i++){
  // for each button we're making an addEventListener (stuff that happens when we click)
  updateBtns[i].addEventListener('click', function(){
    console.log('first funck')
    var productId = this.dataset.product
    var action = this.dataset.action



    updateUserOrder(productId, action)
})
}

function updateUserOrder(productId, action){
  console.log('User connecté envoie de donné à url variable que je crée')
  console.log('second funck')
  var url = '/updateItem/'

  // To send POSt data
  //Sending POST data as first parameters we pass to the fetch the url we wanna send the data to the view
  // as second paramerter we want to define what kinda of data we wanna send to the view
  fetch(url, {

    method: 'POST',
    headers:{
      'content-Type':'application/json',
      'X-CSRFToken':csrftoken,
    },
    //the body is the data we're gonna send to the backend in a string form
    body:JSON.stringify({'productId':productId, 'action':action})
  })

  .then((response) =>{
    return response.json()
  })

  .then((data) =>{
    console.log('data:', data)
    location.reload()
  })

}
