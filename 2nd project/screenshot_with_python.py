import pyscreenshot

# to capture the screen
image = pyscreenshot.grab()

# to display the captured screenshot
image.show()

image.save("newshot.png")
