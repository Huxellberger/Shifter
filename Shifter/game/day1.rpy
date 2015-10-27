label day1:

  call resetchoices from _call_resetchoices

  # *SCENE 1*
  play sound "soundeffects/caralarm.mp3" 
  with flash
  customer1 '{cps=50}WHAT ARE YOU DOING?! WAS YOUR MOTHER A ROVER CITYROVER WITH A DODGY FIVE DOOR HATCHBACK THAT STUCK ON EVERY FAMILY PICNIC?!{/cps}'
  scene bg autoshopmain with bgshow
  show customer1 left at left with enter
  with Pause(1)
  stop sound 
  volvaro '{cps=35}What\'s going on in here? Mr. Wilson is gonna flip if we fall any further behind today\'s schedule{/cps}{cps=5}...{/cps}'
  play music "music/saabtheme.mp3"
  play sound "soundeffects/caralarm.mp3"
  with flash
  customer1 '{cps=50}This is the absolute {b}WORST SERVICE{/b} I have ever recieved. My window wipers are {b}RUINED!{/b}.{/cps}'
  with Pause (1)
  show saab right at right with enter
  saab '{cps=30}If I\'m going to be totally honest{/cps}{cps=2}...{/cps}{cps=50}{b}I have absolutely no idea what\'s the problem!{/b}{/cps}'
  volvaro '{cps=40}{i}The car on the right is Saabrina, but most people just call her Saab.{/i}{/cps}'
  volvaro '{cps=40}{i}Her decision to pursue car repair without posable thumbs has made her somewhat inept at her profession.{/i}{/cps}'
  volvaro '{cps=40}{i}The person on the left is just another satisfied customer of {/cps}{cps=15}{b}Wilson\'s Hit Auto Motors!{/b}{/i}{/cps}'
  volvaro '{cps=30}{i}Sometimes I feel like I\'m the only sane one around here.{/i}{/cps}'
  saab '{cps=30}I just don\'t know what her beef is Vol,{/cps} {cps=40}I used the wrench on the squeaky wheel and everything!{/cps}'
  customer1 '{cps=50}You used {/cps}{cps=10}{b}a wrench{/b}{/cps}, {cps=40}you might be horrified to know that there\'s more than one variety of wrench you brainless chrome clutz!{/cps}' with vpunch
  customer1 '{cps=30}If you only cared to look a little closer at what your rotund extremities were grasping{/cps}{cps=2}...{/cps}'
  hide customer1 left
  hide saab right
  scene black with bgshow
  show item wrench1 at left with dissolve
  with Pause(2)
  customer1 '{cps=25}This is the two-sprong-twister that you used to {b}maul{/b} my exterior{/cps}'
  show item wrench2 at right with dissolve
  customer1 '{cps=15}...and {b}HERE{/b} is the wrench you should have been using. The fact that you muddled these two is{/cps}'
  play sound "soundeffects/caralarm.mp3"
  show bg autoshopmain with flash
  show saab right at right 
  show customer1 left at left
  customer1 '{cps=10}{b}Absolutely Ludicrous!{/b}{/cps}'
  volvaro '{cps=25}{i}Well...time to jerry rig this scrap heap.{/cps} {cps=4}{b}Again.{/i}{/b}{/cps}'
  stop sound
  volvaro '{cps=25}{i}First I have to get Saab to leave before the tools do!{/i}{/cps}'
  hide customer1 left with dissolve
  show saab right at center 

  # *CHOICE ONE*
  call resetcount from _call_resetcount
  $ charm = True
  $ diligence = True
  $ expression = True
  label treesaab:
    call makechoice from _call_makechoice 

    if choice == "charm":
      if charmcount == 0: 
        volvaro '{cps=15}I\'m sure if you just apologise she\'ll calm down and maybe even call you "Miss chrome clutz".{/cps}'   
        saab '{cps=20}Chrome? But red isn\'t even close to chrome!{/cps}{cps=15} Maybe her headlights are faulty too...{/cps}'
        volvaro '{cps=20}{b}She{/b} needs to change her headlights? You cracked yours from careening off the car lift last week!{/cps}'
        play sound "soundeffects/caralarm.mp3"
        with flash
        saab '{cps=40}I wanted to see how it felt and then I got spooked by the lofty heights!{/cps}'
        stop sound 
        volvaro '{cps=25}{i}Uh oh. I don\'t think "charmed" is within a ditzy pedal car\'s range of emotions. Maybe I should try something a bit more explicit.{/i}{/cps}'
        $ charmcount += 1
      elif charmcount == 1:
        volvaro '{cps=25}You\'re a nice car and I\'m sure if you just explain it was an honest mistake she\'ll-{/cps}'
        play sound "soundeffects/caralarm.mp3"
        with flash
        saab '{cps=40}{b}Mistake?! I used the spoony-wrench-thingy just like in all the manuals!{/b}{/cps}'
        volvaro '{cps=20}You do realise those manuals were designed for humans?{/cps}'
        saab '{cps=40}And you do realise that I am in fact{/cps} {cps=10}a car,{/cps} {cps=30}and thus know far more about the intricate wrenchings than {b}you{/b}!{/cps}'
        volvaro '{cps=25}Didn\'t you pick the wrong wrench anyway...?{/cps}'
        saab '{cps=2}......{/cps}'
        volvaro '{cps=25}{i}Well, I sussed her. The only thing that gained was silence...which is almost good enough for the time being.{/i}{/cps}'
        $ charm = False
      jump treesaab
      
    elif choice == "diligence":
      if diligencecount == 0:
        volvaro '{cps=25}That\'s not the right wrench, but maybe I can order one in that is {b}just perfect{/b} for you!{/cps}'
        saab '{cps=20}That\'s very kind of you, but I don\'t think a wrench will fix the noxious gas coming out of{/cps} {cps=5}{b}her exhaust!{/b}{/cps}'
        volvaro '{cps=25}{i}Legitimate customer complaints handled with such professionalism...{/i}{/cps}'
        $ diligencecount += 1
      else: 
        volvaro '{cps=25}{i}I\'m not sure that\'s going to be particularly effective right now. People have no need for sales tactics when they smash everything like it\'s their own anyway...{/i}{/cps}'
      jump treesaab
    
    elif choice == "expression":
      volvaro '{cps=25}Maybe you should just go hide in the office before you make the whole building crumble in on itself.{/cps}'
      saab '{cps=20}You\'re right! There\'s a leak in the ceiling! I should go tell Mr. Wilson before the whole floor is engulfed in sogginess!{/cps}'
      saab '{cps=15}Time to {b}put the pedal to the metal!{/b}{/cps}'
      hide saab with flash
      play sound "soundeffects/squeak.mp3"
      volvaro '{cps=25}{i}Well that\'s not what I wanted, but that\'s what I wanted...I think?{/i}{/cps}'
      stop sound
      play sound "soundeffects/yahoo.mp3"
      show text "{b}{color=#f00}You got 957 score! What a great conversation you did!!{/color}{/b}"
      stop sound
      with Pause(3)
      hide text
    
  show customer1 left at center with dissolve
  volvaro '{cps=25}{i}Right...time to put those posable thumbs to good use...as always.{/i}{/cps}'

  # CHOICE 2
  stop music
  call resetcount from _call_resetcount_1
  call resetchoices from _call_resetchoices_1
  play music "music/customer1theme.mp3"
  $ charm = True
  $ diligence = True
  $ intelligence = True

  label treecustomer1:
    call makechoice from _call_makechoice_1

    if choice == "charm":
      volvaro '{cps=20}I hope that this experience wasn\'t too uncomfortable.{/cps}'
      customer1 '{cps=30}It was absolutly un{b}BEAR{/b}able! What sort of malfunctioning contraptions do you people hire these days?!{/cps}'
      volvaro '{cps=20}I assure you she only has the best of intentions.{/cps}'
      customer1 '{cps=30}That thing isn\'t even motorised. She would be better used as scrap!{/cps}'
      volvaro '{cps=25}{i}She\'s really getting on my nerves. Saabrina is a clumsy bafoon but she\'s always caring.{/cps}{cps=2}...{/cps}{cps=25}{/i} I feel that you are being unreasonable.{/cps}'
      customer1 '{cps=20}HA HA HA HA HA! Unreasonable, I was being generous. Why would you care what happens to such a failure anyway?{/cps}'
      volvaro '{cps=20}{i} Alright....she\'s in a fairly bad mood and not one for positive thinking...how should I proceed...{/i}{/cps}'
      $ morality -= 1
      call makechoice from _call_makechoice_2
      if choice == "charm":
        volvaro '{cps=20}{i}I should continue to try to appeal to her sensitivity or what\'s left of it...{/i}{/cps}'
        customer1 '{cps=20}Are you waiting for an invitation or are you going to repair my wheel?{/cps}'
        volvaro '{cps=20}I\'ll be right there!{/cps}'
        scene black with bgshow
        play sound "soundeffects/crank.mp3"
        with Pause(5)
        stop sound
        scene bg autoshopmain with bgshow
        show customer1 left at center
        volvaro '{cps=20}{i}I had to listen to her bad mouth Saabrina throughtout the repair, I hope i didn\'t miss anything...{/i} I\'m done, that will be 1000 bolts.'
        customer1 '{cps=30}Hmph, here you go friend of a mongrel.{/cps}'
        $ morality -= 1
      elif choice == "diligence":
        volvaro '{cps=20}{i}I should focus on my work and ignore my personal feelings.{/i}{/cps}'
        customer1 '{cps=20}Are you waiting for an invitation or are you going to repair my wheel?{/cps}'
        volvaro '{cps=20}I apologise for my hostility, I meant no offence{/cps}'
        customer1 '{cps=20}Oh, so finally realise that it is not worth anything{/cps}'
        volvaro '{cps=20}I understand your frustration and would like to offer you a complementary accessory of your choice, I\'d highly recommend the dice{/cps}'
        customer1 '{cps=25}That\'s more like it, I\'d like a dangling die!{/cps}'
        volvaro '{cps=20}Ofcourse, here you are, I\'d like to begin the repairs now{/cps}'
        scene black with bgshow
        play sound "soundeffects/crank.mp3"
        with Pause(5)
        stop sound
        scene bg autoshopmain with bgshow
        show customer1 left at center
        customer1 '{cps=20}Finally, here\'s your fee for the repairs, I will now be on my merry way.{/cps}'
        volvaro '{cps=20}Please come again{/cps}'
        $ morality += 1 
      elif choice == "intelligence":
        volvaro '{cps=20}{i}I should handle this with my intelligence{/i}{/cps}'
        customer1 '{cps=20}Are you waiting for an invitation or are you going to repair my wheel?{/cps}'
        volvaro '{cps=25}Just allow me to get the two-sprong-rotator.{/cps}'
        customer1 '{cps=25}Thank you, finally someone with enough common sense to tell the difference between a two-sprong-twister and a two-sprong-rotator!{/cps}'
        volvaro '{cps=25}I shall now commence the repairs.{/cps}'
        scene black with bgshow
        play sound "soundeffects/crank.mp3"
        with Pause(5)
        stop sound
        scene bg autoshopmain with bgshow
        show customer1 left at center
        volvaro '{cps=25}All done, that will be 2000 bolts.{/cps}'
        customer1 '{cps=20}Charging me after the hell I\'ve been put through you have some nerve!{/cps}'
        volvaro '{cps=20}Take any complaints to the manager, I\'m sure he\'ll be delighted to discuss your menial problem.{/cps}'
        customer1 '{cps=30}I do not have the time to deal with managers, just take your fee.{/cps}'
        volvaro '{cps=20}Thank you for your business! {i}And don\'t come back.{/i}{/cps}'
        $ morality += 2      
    elif choice == "diligence":
      $ intelligence = False
      volvaro '{cps=20}I am sorry for the inconvenience, I can offer you a 25\% discount on all our accessories. Would you like to buy our highly collectable dangling dice? There are many different varieties from blazing red to ocean blue!{/cps}'
      customer1 '{cps=20}Aha this is the perfect opportunity to add to my collection, three more and I would have a full set!{/cps}'
      volvaro '{cps=30}In that case I\'ll sell you the three for the price of two.{/cps}'
      customer1 '{cps=20}{b}BRILLIANT{/b} I will finally be able to rub my dangling dice into my neighbour\'s faces, just as they have done to me in the past!{/cps}'
      volvaro '{cps=20}I will now fix your wheel. Please try to keep your handbrake on and your engine off, I know it\'s difficult with all the excitement going on.{/cps}'
      customer1 '{cps=25}Thank you, please start whenever you are ready.{/cps}'
      scene black with bgshow
      play sound "soundeffects/crank.mp3"
      with Pause(5)
      stop sound
      scene bg autoshopmain with bgshow
      show customer1 left at center
      $ morality += 2
      call makechoice from _call_makechoice_3
      if choice == "charm":
        volvaro '{cps=20}{i}Now that she\'s in a good mood I should try and charm her a little{/i}{/cps}'
        volvaro '{cps=20}I hope your axles are feeling better.{/cps}'
        customer1 '{cps=20}It was the most pleasing experience I\'ve had in a while.{/cps}'
        volvaro '{cps=15}I\'m glad I have satisfied your needs.{/cps}'
        customer1 '{cps=20}Here\'s the 2000 bolts for the repairs, here\'s the 100 for the dice and here\'s something special for you{/cps}{cps=3}...{/cps}'
        volvaro '{cps=20}Thank you very much.{/cps}'
        customer1 '{cps=10}I\'ll definitely be coming back{/cps}'
        $ morality += 2
      elif choice == "diligence":
        volvaro '{cps=20}{i}I should remain diligent{/i} All done, I hope the experience was a decent one.{/cps}'
        customer1 '{cps=20}It was {/cps}{cps=3}AMAZING!{/cps}'
        volvaro '{cps=30}In addition to the dangling dice we have a special rarity die that I can sell you for 1000 bolts, jangle it everyday and you may find the secret it holds within.{/cps}'
        customer1'{cps=30}{b}NOT THE MAGNIFICENT RAINBOW DIE!{/b} That is the desire of all vehicles everywhere...{/cps}{cps=3}I... must... have {b}IT!{/b}{/cps}'
        volvaro '{cps=20}That will be 1000 bolts for the special die, 2000 for repairs and 100 for the 3 normal dice.{/cps}'
        customer1'{cps=20}Here you go young man.{/cps}'
        volvaro '{cps=20}Have a nice day and please come again.{/cps}'
        $ morality += 1
    elif choice == "intelligence":
      volvaro '{cps=20}It appears that your front wheel is badly damaged. I will repair it to the best of my abilities.{/cps}'
      customer1 '{cps=25}Thank you, finally someone with enough common sense to tell the difference between a two-sprong-twister and a two-sprong-rotator!{/cps}'
      scene black with bgshow
      play sound "soundeffects/crank.mp3"
      with Pause(5)
      stop sound
      scene bg autoshopmain with bgshow
      show customer1 left at center
      volvaro '{cps=25}All done, that will be 2000 bolts.{/cps}'
      customer1 '{cps=20}Charging me after the hell I\'ve been put through you have some nerve!{/cps}'
      volvaro '{cps=20}Take any complaints to the manager, I\'m sure he\'ll be delighted to discuss your menial problem.{/cps}'
      customer1 '{cps=30}I do not have the time to deal with managers, just take your fee.{/cps}'
      volvaro '{cps=20}Thank you for your business! {i}And don\'t come back.{/i}{/cps}'
      $ morality += 2
    call resetcount from _call_resetcount_2
    call resetchoices from _call_resetchoices_2

  #SCENE BOSS MAN
  hide customer1 left with enter
  stop music
  volvaro '{cps=20}{i}Another happy customer...I think.{/i}{/cps}'
  volvaro '{cps=5}{i}Well...{/cps}{cps=20} considering the silence I should probably make sure Saab hasn\'t entered a drag race or something-{/i}{/cps}'
  play sound "soundeffects/caralarm.mp3"
  with flash
  mystery '{cps=6}{b}VOLVOOOOOOO{/b}{/cps}'
  volvaro '{cps=15}{i}Great, now the cars are shouting at me.{/i}{/cps}'
  scene black with bgshow
  stop sound
  scene bg office with bgshow
  show bmwilson left at center with enter
  volvaro '{cps=20}{i}Oh boy, the big cheese himself. And I\'m not talking about the tacky paintjob.{/i}{/cps}'
  volvaro '{cps=25}What\'s wrong Mr. Wilson? I was just finishing up with a customer out there and was about to-{/cps}'
  play music "music/bmwilsontheme.mp3"
  bmwilson '{cps=25}Never mind about that young Volvo! There\'s {/cps}{cps=1}   {/cps}{cps=20}{b}sales{/b} to discuss!{/cps}'
  volvaro '{cps=25}Mr. Wilson I\'d be happy to discuss-{/cps}'
  bmwilson '{cps=25}Or maybe {b}"sale"{/b} would be more accurate? You fleshy fellows with your thumbs continuing to put us to shame!{/cps}'
  bmwilson '{cps=35}Today has surpassed the previous most disappointing day of my life, that being the day I hired you to fill the damn diversity quota!{/cps}'
  bmwilson '{cps=25}Do you have {b}anything{/b} to say for your below sub-expectations performance then?{/cps}'

  $ ui.window()
  $ ui.vbox() 
  $ ui.textbutton("Justify With High Bolt Profit Margins", clicked =ui.returns("good"))
  $ ui.textbutton("Blame It On Saab\'s Ridiculous Behaviour And Hat", clicked =ui.returns("bad"))
  $ ui
  $ ui.close()
  $ choice = ui.interact(suppress_overlay=True)

  if choice == "good":
    $ relationshipbmwilson -= 3
    $ relationshipsaab += 2
    volvaro '{cps=25}{i}Well, try to make the best of another bad day of sales Vol.{/i}{/cps}'
    volvaro '{cps=25}Actually Mr. Wilson, if you\'ll just examine the bolt to profit margin of the last customer I serviced-{/cps}'
    play sound "soundeffects/caralarm.mp3"
    bmwilson '{cps=35}{b}Bolt to profit? Bolt to profit?! Why did you sell our good name to a somewhat grossly proportionally large bag of..{/b}{/cps}'
    stop sound
    with flash
    bmwilson '{b}rusty{/b}'
    with flash
    bmwilson '{b}Grossly unhygienic{/b}'
    with flash
    bmwilson '{cps=2}{b}BOOOLTS.....{/b}{/cps}' with hpunch
    volvaro '{cps=25}But Mr. Wilson, you explicitly stated that I should keep a keen eye out for the rustiest bolts out there, since their owners are probably the most carele-{/cps}'
    bmwilson '{cps=20}That was {b}yesterday{/b}, Mr. Wilson. Times change. You\'re really starting to bruise my bonnet here. One more slip-up and I might just have good cause to-{/cps}'
 
  else:
    $ relationshipbmwilson -= 1
    $ relationshipsaab -= 2
    volvaro '{cps=25}Sir, I was actually on good time for the day. That was at least, until Saab stepped in and-{/cps}'
    bmwilson '{cps=40}{b}Oh I see!{/b} It was Saab\'s fault you failed to make any sales! It was her fault when you were the one that sent her on a wacky misadventure to my office prophesising bad omens through the next great flood of our times!{/cps}'
    volvaro '{cps=15}{i}Great flood? Saab is underplaying it a bit for her standards there.{/i}{/cps}'
    bmwilson '{cps=25}Cars are excellent forders Mr. Vargo, and if they get all slogged up with water in here then just run an engine refurbish too. Make their bad situation worse, at least until the final billing or until they try to stutter out.{/cps}'
    bmwilson '{cps=25}And the fact that you blamed your abject failures on such a hard worker as Saab? Letting your {b}bigoted{/b} ideas get in the way again? I upgraded my window wipers just to handle the {/cps}{cps=10}endless, pouring shame you cause me!{/cps}'
    play sound "soundeffects/caralarm.mp3"
    bmwilson '{cps=25}Being forced to take you on to satisfy the diversity quota was a crime. A double decker staff force with not an engine between the two of them. Miserable days indeed.{/cps}'
    volvaro '{cps=25}{i}Bigoted? Engines? I thought his horn was the most obnoxious trite to come out of that{/cps}{cps=3}....well,{/cps}{cps=25} whatever makes him talk.{/i}{/cps}'
    stop sound
    bmwilson '{cps=25}Speechless I see? Well isn\'t that a reversal of roles young man? Us cars have had a lot to say for a while now, and if you\'re not careful I might be just telling the firm I had to-{/cps}'

  # REVELATIONS
  scene black with flash
  show bmwilson left 
  stop music 
  bmwilson '{cps=25}Let you go.{/cps}'
  with flash
  volvaro '{cps=10}{i}Let me....let me go?{/i}{/cps}'
  volvaro '{cps=15}{i}Of course that\'s what it all comes back to. He won\'t be satisfied with anything less than watching my utter annihilation{/i}{/cps}'
  volvaro '{cps=25}{i}Or failing that, seeing me asleep under the drive-thru racks everytime he hankers getting in a bit of grease and gloating.{/i}{/cps}'
  bmwilson '{cps=25}Don\'t even think you have a chance of appealing it either.{/cps}'
  bmwilson '{cps=25}I know all about what you {b}used to get up to{/cps}{cps=5}...{/b}{/cps}{cps=20} and need I elaborate anymore-{/cps}'
  with flash
  play music "music/darkpast.mp3"
  bmwilson '{cps=8}{b}About A Certain Used Car Dealership?{/b}{/cps}'
  volvaro '{cps=2}.....{/cps}'
  bmwilson '{cps=25}I think it\'s time you left through the garage door,{/cps} {cps=15}old Varago.{/cps}'
  volvaro '{cps=20}Gladly.{/cps}'
  bmwilson '{cps=25}Have a nice evening Mr. Volvaro. Careful near the roads, it is rush hour after all!{/cps}'
  hide bmwilson left with enter
  scene bg street with bgshow
  volvaro '{cps=25}I hate it when he mentions rush hour. Like it\'s my fault all the cars chugged off to somewhere else.{/cps}'
  volvaro '{cps=25}Trust me Marmaduke, I would have paid for them to take you if I could. Paid with two misproportionally large bags of rusty bolts. {b}The lot!{/b}{/cps}'
  scene bg alley with flash
  volvaro '{cps=30}I mean, it sort of is my fault. But you have to be taking quite a few liberties to get to that conclusion. It\'s a definite jump of logic for sure.{/cps}'
  volvaro '{cps=30}{b}I\'m the one with the crummy house, in the deadend neighbourhood alone{/cps}{cps=2}..{/b}..?{/b}'
  volvaro '{cps=25}{i}Great, talking to myself. In a putrid alley in geographically defined "middle of nowhere".{/i}{/cps}'
  volvaro '{cps=25}Could be worse...could be talking to the cars or something!{/cps}'
  play sound "soundeffects/rustle.mp3" 
  with flash
  stop music 
  mystery '{cps=12}{b}....*crunch*...*crunch*...{/b}{/cps}'
  volvaro '{cps=25}{i}Uh oh...sounds like I offended one of the locals. The amount of lipservice from zero lips I have endured today is breaking national records at this point...{/i}{/cps}' 
  stop sound
  play sound "soundeffects/crash.mp3"
  with hpunch
  show boxguy right at right with flash 
  mystery '{cps=60}{b}YOU\'RE WAY OFF ROAD NOW LITTLE TRIKE. PREPARE TO RUSHT OVER 3 TO 5 DAYSSH BETWEEN MY SHTEEL BRASHESH OF....JUSHTEESH{/b}{/cps}'
  stop sound
  with vpunch
  play sound "soundeffects/crash.mp3"
  with flash
  volvaro '{cps=40}{b}I\'M NOT A CAR. LOOK AT HOW I\'M MADE OF ABSOLUTELY ZERO ALUMINIUM. PLEASE{/cps}{cps=12}-...?{/b}{/cps}'
  volvaro '{cps=25}{i}Is that box actually talking to me? Surely not..{/i}{/cps}'
  hide boxguy with enter
  stop sound
  volvaro '{cps=25}Crikey...cars and now boxes. Maybe I have gone insane...{/cps}'
  show boxguy right at right with flash 
  play music "music/boxcotheme.mp3"
  boxguy '{cps=50}{b}SHon, lisHten to me. The whole world has gone batshHite ugly. And I\'d know, I once went camping with my dead wife in the bat cavesH.{/b}{/cps}'
  boxguy '{cps=75}Well by that I mean sHhe\'sH wasH\'nt dead at that point, that was before the carsH were on every sHReet corner and life was a lot prettier back then, esHpeSHially my wife who was absHuletely fit as a fiddle{/cps=75}' 
  boxguy '{cps=75}SHe\'sH gone a bit downhill sHince then of coursH, losHt a lot of colour and all. SHe alwaysH complained about the bat caves too, {b}fucking {/cps}{cps=2}b-b-{/cps}{cps=30}bITCH.{/b}{/cps}'
  boxguy '{cps=75}My boy JHAmeSH was alaysHH getting really into it too, asking me about how there parentSH were let them sHleep in all day and let them play all night. JHAmeSH, a good kid...alwaySH looking out for his old man{/cps}{cps=5}....?{/cps}'
  boxguy '{cps=40}WhatSH up my boy? You\'re looking awfully pale. Have you made sHure to have a proper breakfaSht today?{/cps}'
  boxguy '{cps=75}And I don\'t mean any of that "Continental BreakfasHt" sHHite and all that. A proper breakfasHt sHHould at least have a little bacon and meat in it. I mean really it sHHould have a lot of meat, but my wife usHed to sHay it wasH "bad for my heart" {b}fucking {/cps}{cps=2}b-b-b-bi-b....{/b}{/cps}'
  volvaro '{cps=25}{i}This is the day Vol, the day your life of complete nonsense somehow went off the rails. Or is it railsHHH?{/i}{/cps}'
  boxguy '{cps=35}I can\'t remember what I wasH gonna sHay, but I think sHomehow by the look on your faSH I can sHe I made my point. You have a good sHtrong faSH by the way. BreakfasHt or no BreakfasHt you\'ve got big thingsH coming I can tell.{/cps}'
  call resetcount from _call_resetcount_3
  call resetchoices from _call_resetchoices_3
  $ diligence = True
  $ intelligence = True 
  $ curtness = True
  label treeboxguy1: 
    call makechoice from _call_makechoice_4
    if choice == "diligence":
      if diligencecount == 0:
        volvaro '{cps=25}Spending every second of your life in such a tiny cardboard box must be very difficult for you. How about getting your head, shoulders and knees if they fit into a new, used roomy box that will keep you as cool on those hot summer days as its fridge based origins?{/cps}'
        boxguy '{cps=40}It\'sH a tempting offer lad, and I don\'t want to cause offenSH, but thisH one isH handling jusHt peaSHy right now.{/cps}'
        boxguy '{cps=60}Now don\'t go worrying about my kneesH either. It can get cramped but I alwaysH make sHure to sHpend at leasHt 20 minutesH a day sHretching out thesHe tasHty thighsH and raSHor sHHarp paSHersH!{/cps}'
        boxguy '{cps=50}SHHarp from yearsH of my wife not picking me up after work becausHe she had to go to JHameSH\'sH band practisH. Hah, band practiSH, I uShed to asHk JHameSH how it wasH afterwardsH and he alwaysH had thisH vacant look in hiSH eyesH. The kind a lad getsH when hiSH mother makesH him lie about band practiSH.{/cps}'
        boxguy '{cps=50}sHasHHing boy though, my village bycycle of a wife, sHHe wasH the devil. Telling JHameSH to lie like that...if I sHtill had a belt...and sHe wasHn\'t dead...and I wasHn\'t in thiSH box...{/cps}'
        volvaro '{cps=30}{i}I don\'t even know why I tried to sell a fridge box to this guy. I think whoever gave him that last scruffy container set the return address to the sanatorium.{/i}{/cps}'
        $ diligencecount += 1
        jump treeboxguy1
      elif diligencecount > 0:
        volvaro '{cps=30}{i}Just between you and me. I think even if I did have something he wanted, I\'d never be able to figure out what it was through his anecdotal assaults.{/i}{/cps}'
        boxguy '{cps=40}Uh oh. I sHe it again. That vacant look in your eyesH. Too muSH sHon can kill a man you know. Take a look at me for example, darting pasHt 52 and sHtill going sHtrong! You could probably fit in here if you needsH a little tuckering out...{/cps}'
        volvaro '{cps=50}{b}That\'s quite alright, home is very close and I wouldn\'t want to intrude!{/b}{/cps}' with flash
        volvaro '{cps=30}{i}It would be a lot closer if I hadn\'t taken the most catastrophic shortcut of my life down here too.{/i}{/cps}'
        jump treeboxguy1
    elif choice == "intelligence":
      if intelligencecount == 0:
        volvaro '{cps=30}You know it\'s getting fairly late, surely you should be...relinquishing yourself from your day\'s labours and heading home to take care of your son now?{/cps}' with hpunch
        with flash
        play sound "soundeffects/crash.mp3"
        boxguy '{cps=55}{b}Watch your tone with me little sHquirty or you\'ll be needing a SHesHeSHction of my fisHt tonight!{/b} You think I would ever leave old JHameSH in the dark at home! The boy hasH band practiSH tonight!{/cps}'
        volvaro '{cps=15}He has....{b}band practice?{/b}{/cps}'
        boxguy '{cps=50}Yeah I bet you\'re sHHocked. Here you are sHirking your adult life away like a sHloucSH, and yet a boy half your age is channeling all the AerosHmithsHs with his banging flute riffsH! PractisH, that\'sH how progesH getsH made. AlwaysH tell him that.{/cps}'
        boxguy '{cps=55}CoursH I never have heard him play at a consHert...or ever for that matter. You know how the offiSH getsH. nine to five is jusHt a catchy tagline, it\'sH really more like "pre five sHHite, to a brief lunSHtime jife, to the dead of night only to be rewarded for your dedication with a lecture from your {b}{/cps}{cps=2}b-b-bi-bi..{/cps}{/b}'
        volvaro '{cps=25}Right...of course he is...my mistake-{/cps}'
        boxguy '{cps=55}My sHon isH a real Leonardo you know. He can sHWing that flute around hisH musHical melodiesH like the besHt ninja turtlesH..well sHo the wife sHaysH when sHHe actually bothersH to sHpeak to me in a tone that isHn\'t jusHt a sHplurge of whining and sHelf pity. sHe must get through a entire hanky factory with her sHelf pity.{/cps}'
        volvaro '{cps=25}{i}His analogy made little sense with the painter Leonardo, but somehow I\'m not surprised he went with the even more unintelligble Ninja Turtle comparison. Wasn\'t Donatello the one with the polearm anyway?{/i}{/cps}'
        boxguy '{cps=45}A jife isH masHturbating by the way sHonny. JusHt in casHe you weren\'t down with the lingo. Wife sHtopped putting out a long time ago. MakesH death valley look like the great valley, if you undersHtand what I mean.{/cps}'
        volvaro '{cps=25}{i}Dead people do tend to be pretty inefectual in that respect. Looks like you\'re very considerate to that fact.{/i}{/cps}'
        $ intelligencecount += 1
        jump treeboxguy1
      else:
        volvaro '{cps=25}{i}This man is beyond reason. I should just get out of here. I might not be the fittest guy alive but outrunning a box on shuffling knees seems well within my capabilities. And if not there\'s always the slow, agonising death of tangental regurgitation.{/i}{/cps}'
        jump treeboxguy1 
    else:  
      volvaro '{cps=25}Thank you for stopping by, I\'ve thoroughly enjoyed the conversation we\'ve shared. Must get home though, you know how it is and all...{/cps}'
      $ ui.window()
      $ ui.vbox() 
      $ ui.textbutton("Wife Is Expecting", clicked =ui.returns("a"))
      $ ui.textbutton("Dog Needs A Walk", clicked =ui.returns("b"))
      $ ui.textbutton("My Kidneys Are Failing", clicked =ui.returns("c"))
      $ ui
      $ ui.close()
      $ choice = ui.interact(suppress_overlay=True)
      if choice == "a":
        volvaro '{cps=25}My Wife is expecting me back home soon and I really don\'t want to upset her tonight. We were planning to have sex and everything.{/cps}'
        boxguy '{cps=30}I sHee, trading me up for a bit of leg over. I can relate, well {b}could{/b}, back when my wife wasHn\'t a complete-{/cps}'
        volvaro '{cps=40}She\'s also expecting a baby, two of them, and I just heard she\'s gone into labour. Must be going right now, after all imagine if I got there in the middle and one of my kids was already out? Can\'t seem like I have a favourite. Good night!{/cps}'
      elif choice == "b":
        volvaro '{cps=25}My Dog Roger has a really weak bladder after his colon cancer and is bursting for a bit of fresh air. Best get home before he leaves some more "Roger Dodgers" lying around the place!{/cps}'
        boxguy '{cps=30}You got a dog eh? Wouldn\'t figure you for the dog type, not muSH compasHion behind thosHe eyesH. Got more of a cadaverousH look to \'em, sHort of like my good old wife, not sHure if I mentioned but sHe-{/cps}'
        volvaro '{cps=40}Yes I know, you mentioned it only eight million times previously. I have to go home before my dog drowns everyone in shit, goodnight.{/cps}'
      else:
        volvaro '{cps=25}Ooof....oh...{b}yowch!{/b}{/cps}' with flash
        boxguy '{cps=30}Are you alright lad? I know I mentioned the breakfasHt but thisH isH frankly getting a tad ridiculousH now.{/cps}'
        volvaro '{cps=25}I know this feeling too well. My kindeys are failing, and it\'s not the first time. You know how it is, always when you have so much to say! Best get home and turn on the dialysis machine; always takes a bit to get going what with all the electric things!{/cps}'
        boxguy '{cps=30}Wait, I think I know basHic resHursHitation. JusHt lie down and let me take one to five deep inhalesH...{/cps}'

  hide boxguy right 
  volvaro '{cps=25}{i}Don\'t look back into those slurpy green eyes, just keep...moving...{/i}{/cps}'
  show boxguy right at center with flash
  volvaro '{cps=25}{i}...This is it...this is how I die. Not by being run over..or shot...but by lethal exposure to verbal diarrhea.{/i}{/cps}'
  show item trumpet with flash
  boxguy '{cps=30}Here....I want you to have it.{/cps}'
  volvaro '{cps=25}This...this trumpet?{/cps}'
  boxguy '{cps=30}Go on, take it before I change my mind. ThisH usHed to be JHameSH\'SH when he was a tyke. If you need me jusHt blow and I\'ll come running. I\'ll never forget it\'s dullard tonesH after...well..{/cps}'
  volvaro '{cps=25}{i}Do I detect a hint of humanity in this carboard box? No, that can\'t be right, for several easily explainable reasons.{/i}{/cps}'
  hide item trumpet
  think '{cps=25}{i}I stuff it in my pocket quickly.{/i}{/cps}'
  volvaro '{cps=25}Thanks...I\'ll make sure to do just that if I ever need....{b}something{/b}.{/cps}'
  boxguy '{cps=35}Good sHtuff lad. JusHt remember to come visHit me onSHe in a while down here, exSHept if it\'sH raining. Can\'t be mesHing about in that sHtuff, need to presHerve my home and all.{/cps}'
  volvaro '{cps=25}Right....I\'ll be off now.{/cps}'
  boxguy '{cps=50}ThanksH for visHiting, it\'sH been.....it\'sH been sHomething!{/cps}'
  with flash
  play sound "soundeffects/crash.mp3"
  volvaro '{cps=25}{i}Oh god...did he just wink? I need to get out of this alley, and place warning signs up in a fifty metre radius for every rational thinker in this cruel world.{/i}{/cps}'
     
  stop music
  with flash   
  scene black with enter
  play sound "soundeffects/door.mp3"
  show text "{b}Click!{/b}" with flash
  stop sound
  scene bg volbedroom with enter
  stop music 

  # *TV SCENE*
  volvaro '{cps=20}{i}Back home after another long day of back and forth between fixing buggered cars and fixing the approval ratings of a certain buggered old goit.{/i}{/cps}'

  if morality < 0:
    volvaro '{cps=25}{i}I had a pretty bad day today. The only rusty bolts were my sales skills...and every car that came in of course.{/i}{/cps}'
  else:
    volvaro '{cps=25}{i}Today went fairly well, for a day filled with people who are actually cars. If I keep this up I might not get fired until next week! One can hope.{/i}{/cps}'
  if relationshipsaab < 0:
    volvaro '{cps=25}{i}I probably shouldn\'t have blamed Saab back there. A pain in the bumper, true, but with good intentions.{/i}{/cps}'
  else:
    volvaro '{cps=25}{i}I\'m Glad I covered for Saab today. It\'s probably not easy being both a glorified trike in a car\'s world and completely nuts. I could relate. {/i}{/cps}' 
  volvaro '{cps=25}{i}And I just don\'t think old Boris is ever going to take a shine to me when blatant racism is so much more natural to him. Best to make an effort to the man you depend on though.{/i}{/cps}'
  volvaro  '{cps=25}{i}I\'d complain a bit more internally, but why do that when I can complain about the constantly repeating automovies on the old television box?{/i}{/cps}'
  
  scene bg tv with enter
  play music "music/tvtheme.mp3"
  volvaro '{cps=25}{i}It\'s getting pretty late, probably only have time for one program before hitting the hay. Time for life\'s most crucial choice of all...{/i}{/cps}'
  $ ui.window()
  $ ui.vbox() 
  $ ui.textbutton("The Shifting Gears At 7", clicked =ui.returns("news"))
  $ ui.textbutton("The Rental Cars Team With B.A Bobcat", clicked =ui.returns("rental"))
  $ ui.textbutton("Erotic Pillow Fights With Minis", clicked =ui.returns("porn"))
  
  $ ui.close()
  $ choice = ui.interact(suppress_overlay=True)

  if choice == "news":
    volvaro '{cps=20}{i}Might as well tune in and see what\'s going on in New Autobahn{/i}{/cps}'
    scene bg tvscreen with enter
    scene bg newsdesk with flash
    play music "music/news.mp3"
    newscar '{cps=25}Hello and welcome to New Autobahn\'s Monday news! I\'m a car lodged between a chair and a desk too big for my slender chassis.{/cps}'
    newscar '{cps=25}Because the fire department is still on strike I\'ll be presenting your news for tonight! At least until I fall down, smash my sunroof in and choke on the resulting glass shards.{/cps}'
    newscar '{cps=25}{b}Your news tonight!{/b}{/cps}'
    stop music
    if morality < 0:
      scene bg river with flash
      newscar '{cps=25}After a tire spinout on the localish motorway, Autobahn resident Sindy Rodgers went cascading into the local river estuary.{/cps}'
      newscar '{cps=25}If currents encourage her close to the edge you are advised to keep clear, she is highy buoyant and obnoxious to be around.{/cps}'
      volvaro '{cps=25}{i}Oh crikey. Guess I should have paid more attention to what I was doing during the repair job...{/i}{/cps}'
      $ text = "This is Mr. Watson. Just texting to let you know how utterly embarassed I continue to be by your every action in this visual novel. You\'re lucky this is only the first day! Don\'t worry, I\'ll be watching your every move."
      call phonenumbers from _call_phonenumbers 
      $ morality -= 2
      scene bg newsdesk with enter 
      newscar '{cps=25}That\'s literally the only news to come up today. As always, I\'m NewsCarperson, and for such a smart car I\'m unbelievably bollocked. See you again tomorrow New Autobahn!{/cps}'
      scene bg tv with flash
      volvaro '{cps=25}Well that was distressing.{/cps}'
    else:
      stop music
      with flash
      newscar '{cps=25}The scandal between President Harry Ford and the people of Guacamanalona continues as he once again causes great insult for honking the national anthem before flashing at the ceremony for the local war heroes.{/cps}'
      newscar '{cps=25}This unwarrented outburst continues to paint the picture to the people of Gucannelloni that he\'s the worst thing since child molestors.{/cps}'
      newscar '{cps=25}That man is never a let down, and I\'m sure he\'ll be up to his usual antics tomorrow that keep me in the job in this otherwise solitary and vacuous world.{/cps}'
      newscar '{cps=25}That\'s literally the only news to come up today. As always, I\'m NewsCarperson, and for such a smart car I\'m unbelievably bollocked. See you again tomorrow New Autobahn!{/cps}'
      $ text = "This is Mr. Watson, but you can call me Marmadukey. It was fantastic watching you work on the shop floor today, even if you are limited by being a useless flesh man. I look forward to viewing your future endeavours."
      call phonenumbers from _call_phonenumbers_1 
      scene bg tv with flash
      volvaro '{cps=25}Well that was business as usual.{/cps}'

  elif choice == "rental":
    scene bg tvscreen with enter 
    volvaro '{cps=20}Time for my favourite weekly show, The Rental Cars Team. It\'s incredible just how much quality they pack into 10 minutes of unreliably scheduled programming!{/cps}'
    play music "music/rentaltheme.mp3"
    scene bg rental with flash
    narrator '{cps=30}Tonight on the clutch network! The Rental Cars Team find themselves in the greatest jam so far when important human thing John Doegon requires a lift directly to the surface of car mars!{/cps}'
    narrator '{cps=30}It\'s once again up to B.A Bobcat to step in and save the galaxy from impending minor delays and inconvenience!{/cps}'
    bobcat '{cps=20}{b}I \'aint getting in no zero gravity environment!{/b}{/cps}'
    volvaro '{cps=25}Cars in a vacuum. This is probably the best thing that\'s ever happened in existence. I should go hire one myself just for the thrill of it. The prices are like suspension...{b}but lower!{/b}{/cps}'
    volvaro '{cps=25}What am I doing here sitting around and moping with myself. I need to get out there and share the heartfelt message of The Rental Team with the whole world! Life is measured on borrowed time... and now so is your car!!! I can relate {b}so hard!{/b}{/cps}'
    scene black with flash
    show text "You share the joys of Rental Cars with the rest of the intelligent and free world!"
    scene bg tv with enter
    volvaro '{cps=25}Wow...that was the best 24 and a half minutes of my entire life. That was better than when the score text flashes up. I need to have a sit down and calm myself before I have a stroke.{/cps}'
    $ morality += 2
    
  else: 
    scene bg tvscreen with enter 
    volvaro '{cps=25}I always feel dirty when I watch the Eastern European Carwash Channel, but for some reason the volumptous material seems to transcend flesh and dodgy fibreglass.{/cps=25}'
    show black with dissolve
    play music "music/porn.mp3"
    model '{cps=15}Hello there ladies, I have a big long rope on the back of my truck that\'s just asking to drag you back to the shop. Who want\'s an early and ultimately useless {b}MOT{/b}?{/cps}'
    show text "Please enable mature content in preferences if you wish to view these scenes."
    with Pause(4)
    show bg tv with enter
    volvaro '{cps=25}The cars come out of it cleaner, but I just feel dirty inside...{/cps}' 
    $ morality -= 1
  
  stop music
  scene bg volbedroom with enter
  volvaro '{cps=25}{i}Maybe I have time for this one last program that\'s on tonight...it\'s a trailer for some big car thing that\'s coming out soon...{/i}{/cps}'
  play movie "images/trailer.mp4"
  with Pause(60)
  stop movie
  hide movie
  volvaro '{cps=25}My God that was utterly incredible! I can\'t wait for Hack Manchester 2019 where it might be half fucking done!!!!{/cps}'
  return
