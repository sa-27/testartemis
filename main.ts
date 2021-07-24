input.onButtonPressed(Button.A, function () {
    basic.showString("Hello world!")
})
input.onGesture(Gesture.TiltLeft, function () {
    basic.showIcon(IconNames.Asleep)
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(27)
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("sup?")
})
let myImage = images.createImage(`
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    . . . . .
    `)
myImage.showImage(0, 400)
basic.forever(function () {
	
})
