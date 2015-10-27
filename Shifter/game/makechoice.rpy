label makechoice:
  $ ui.window()
  $ ui.vbox() 
  if charm == True:
    $ ui.textbutton("Appeal To Sensitive Nature", clicked =ui.returns("charm"))
  if courage == True:
    $ ui.textbutton("Get Behind The Wheel And Take Them For A Few Laps", 
                   clicked =ui.returns("courage"))
  if diligence == True:
    $ ui.textbutton("Use Sales Tactics", clicked =ui.returns("diligence"))
  if expression == True:
    $ ui.textbutton("Put On A Menacing Tone", clicked =ui.returns("expression"))
  if intelligence == True:
    $ ui.textbutton("Think Outside The Chassis", clicked =ui.returns("intelligence"))
  if understanding == True:
    $ ui.textbutton("Pat Them On The Bonnet", clicked =ui.returns("understanding"))
  if curtness == True:
    $ ui.textbutton("Make Your Excuses And Book It", clicked =ui.returns("curtness"))

  $ ui
  $ ui.close()
  $ choice = ui.interact(suppress_overlay=True)
  return 
