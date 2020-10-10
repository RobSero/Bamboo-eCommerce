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
    const watchButton = '<button type="submit"><i class="fa fa-star" aria-hidden="true"></i> Save to wishlist</button>'
    const unwatchButton = '<button type="submit"  class="watching" ><i class="fa fa-star" aria-hidden="true"></i> Remove wishlist</button>'
    if (data.added){
      buttonOptions.innerHTML = unwatchButton
    } else {
      buttonOptions.innerHTML = watchButton
    }
    watchlistCount.innerHTML = data.watchlist_length
  })
}

