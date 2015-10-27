# You can place the script of your game in this file

init: 
  image movie = Movie(size=(800, 600), xalign=0.5, yalign=0.5)
  
init python:
  import renpy.store as store
  import renpy.exports as renpy
  from clockwork import clockwork

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
init:
  image bg menuscreen = "images/menuscreen.png"
  image bg autoshopmain = "images/carautoshop.jpg"
  image bg office = "images/office.png"
  image bg street = "images/street.png"
  image bg alley = "images/alley.png"
  image bg volbedroom = "images/volbedroom.png"
  image bg tv = "images/tv.png"
  image bg tvscreen = "images/tvscreen.png"
  image bg river = "images/river.png"
  image bg newsdesk = "images/newsdesk.png"
  image bg rental = "images/spaceship.png"
  image customer1 left = "images/cityroverleft.png"
  image customer1 right = "images/cityroverright.png"
  image customer1 death = "images/cityroverdeath.png"
  image bmwilson left = "images/bmwleft.png"
  image bwilson right = "images/bmwright.png"
  image bmwilson death = "images/bmwdeath.png"
  image saab left = "images/saableft.png"
  image saab right = "images/saabright.png"
  image boxguy right = "images/boxguy.png"
  image porscheright = "images/porscheright.png"
  image porscheleft = "images/porscheleft.png"
  image porschedead = "images/porschedead.png"
  image item wrench1 = "images/wrench.png"
  image item wrench2 = "images/wrench.png"
  image item trumpet = "images/trumpet.png"

# Declare characters used by this game.
define mystery = Character('????',  color = "#FF0000")
define volvaro = Character('Volvaro', color="#0066ff")
define bmwilson = Character('Boris', color = "#B800B8")
define porsche = Character('Porsche', color ="#ff9999")
define saab = Character('Saab', color = "#2eb82e")
define customer1 = Character('Customer', color ="#ffa347" )
define newscar = Character('NewsCarperson', color = "#00CC00")
define narrator = Character('Narrator', color = "#FF3300")
define bobcat = Character('Bobcat', color = "#404024")
define model = Character('Tow Truck', color = "#993300")
define boxguy = Character('Box Guy', color = "#CC9900")
define think = Character('')

define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define enter = Fade(1.4, 0.0, 0.5)
define bgshow = Fade(0.3, 0.0, 0.5)

# The game starts here.
label start:

  # VARIABLES FOR ENABLED CHOICES 
  $ morality = 0
  $ relationshipsaab = 1
  $ relationshipbmwilson = -1
  
  $ phonenumber = renpy.input("DO NOT BE ALARMED. Enter Your Phone Number To Play: ") 
  with Pause(3)
  show text "{b}Monday{/b}"
  call day1 from _call_day1

  return 


label resetcount:  
  $ charmcount = 0
  $ couragecount = 0
  $ diligencecount = 0
  $ expressioncount = 0
  $ intelligencecount = 0
  $ understandingcount = 0
  $ curtnesscount = 0
  return
  
label resetchoices:
  $ charm = False
  $ courage = False
  $ diligence = False
  $ expression = False
  $ intelligence = False
  $ understanding = False
  $ curtness = False
  return
  

    

