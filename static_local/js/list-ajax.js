const watchlistCount = document.getElementById('watchlist-count')
const ajaxHeaders = { 
  headers: {
    'X-Requested-With': 'XMLHttpRequest'
  } }

function watchToggle(e){
  e.preventDefault()
  const formAction = e.target.action
  const productId = e.target[0].value
  fetch(formAction, ajaxHeaders).then(res => {
    return res.json()
  }).then(data => {
    console.log(data)
    const buttonOptions = document.getElementById(`watch-buttons${productId}`)
    const watchButton = '<button type="submit" class="no-watch"><img class="like-icon" src="https://res.cloudinary.com/dy7eycl8m/image/upload/v1602405638/likethumb_setair.png" /> Save to wishlist</button>'
    const unwatchButton = '<button type="submit"  class="watching" ><img class="like-icon" src="https://res.cloudinary.com/dy7eycl8m/image/upload/v1602405836/likethumbWhite_zwq7fm.png" /> Remove wishlist</button>'
    if (data.added){
      buttonOptions.innerHTML = unwatchButton
    } else {
      buttonOptions.innerHTML = watchButton
    }
    watchlistCount.innerHTML = data.watchlist_length
  })
}

