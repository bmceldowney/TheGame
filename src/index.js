/**
 * It's the game!
 *
 */

const canvas = document.getElementById('game')
const context = canvas.getContext('2d')
const width = 10
const height = 10
const canvasWidth = 640
const canvasHeight = 480

let directionIndex = 0
let x = 10
let y = 10

context.fillStyle = 'green'

function draw () {
  context.clearRect(0, 0, 640, 480)

  switch (directionIndex) {
    case 0:
      if (x < canvasWidth - (width * 2)) {
        x += 10
      } else {
        directionIndex++
      }
      break
    case 1:
      if (y < canvasHeight - (height * 2)) {
        y += 10
      } else {
        directionIndex++
      }
      break
    case 2:
      if (x > width) {
        x -= 10
      } else {
        directionIndex++
      }
      break
    case 3:
      if (y > height) {
        y -= 10
      } else {
        directionIndex = 0
      }
  }

  context.fillRect(x, y, width, height)
  window.requestAnimationFrame(draw)
}

window.requestAnimationFrame(draw)
