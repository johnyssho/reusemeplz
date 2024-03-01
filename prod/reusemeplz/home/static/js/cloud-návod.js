
let btns = document.querySelectorAll('.js-more-button')

console.log(btns)

btns.forEach((btn) => {
  let parentDiv = btn.parentElement
  let textDiv = parentDiv.querySelector('.js-more-text')
  console.log(textDiv)
  btn.addEventListener('click', () => {
    if (textDiv.classList.contains('hidden')) {
      textDiv.classList.remove('hidden')
      btn.innerHTML = 'Méně' 
    } else {
      textDiv.classList.add('hidden')
      btn.innerHTML = 'Více' 
    }
  })
})