const watchlistCount = document.getElementById('watchlist-count')
const ajaxHeaders = { 
  headers: {
    'X-Requested-With': 'XMLHttpRequest'
  } }



function watchlistUpdate(e) {
  e.preventDefault()
  console.log(e.target)
  const formAction = e.target.action
  const productId = e.target[0].value
  fetch(formAction, ajaxHeaders).then(res => {
    return res.json()
  }).then(data => {
    console.log(data)
    console.log(`item-${productId}`)
    const removedItem = document.getElementById(`item-${productId}`)
    removedItem.remove()
    watchlistCount.innerHTML = data.watchlist_length
    
    
  })
}



// ---------------------  NAV BAR WATCHLIST LENGTH -------------------------

