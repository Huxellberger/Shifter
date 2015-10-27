
image splash = "images/logo.png"

label splashscreen:
  scene black
  with Pause(1)
  
  play sound "soundeffects/trumpet.mp3" 
  show splash at truecenter with dissolve
  
  with Pause(8)

  return

  
