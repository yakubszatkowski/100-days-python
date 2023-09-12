function createStar() {
  // Creates shootingStar element and adds shooting-star class to it
  const shootingStar = document.createElement('span')
  shootingStar.classList.add('shooting-star')

  // Generates random height and width parameters
  const randX = Math.random() * window.innerWidth
  const randY = Math.random() * window.innerHeight
  shootingStar.style.left = `${randX}px`
  shootingStar.style.top = `${randY}px`

   // Generates random number for animation delay in ms
  var delay = Math.floor(Math.random() * 5000)

  // Selects section by class ands appends shooting_star to it
  const glowingBg = document.querySelector('.glowing-bg')
  glowingBg.appendChild(shootingStar)
}

function createStars() {
  for (let step = 0; step < 5; step++) {
    createStar()
  }
}

function deleteStars() {
  const stars = Array.from(document.getElementsByClassName('shooting-star'))
  stars.forEach(star => {
    star.remove()
  })
}

const glowingBg = document.querySelector('.glowing-bg');
glowingBg.add
createStars()

