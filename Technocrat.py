import pygame, time, random
from random import randint
#begins a few pointless questions to the user.
lucid = 'none'
while True:
    if lucid == "no":
        break
    elif lucid == "yes":
        break
    elif lucid == "maybe":
        break
    lucid = input('Are you awake?').lower()

    if lucid == "no":
        print("""Enjoy some coffee. 
        
(Your alertness has been documented.) """)
        time.sleep(2.5)#2.5
        print("Let's continue.")

    elif lucid == "yes":
        print("""Could a person ever truly know that?
         
(Your alertness has been documented.) """)
        time.sleep(2.5)#2.5
    elif lucid == "maybe":
        print("""You set the tone today, my fiend. 
        
(Your alertness has been documented.)""")
        time.sleep(2.5)#2.5
    else:
        print("""I'm a robot Jim, not a dictionary!"
Please, Use simple words while I repeat my query.""")

# I'm pleased with how this question feels from the users perspective.
# It gives feedback on their age based on my age, plus there are two seperate fail states
# that feel fairly dynamic for anyone attempting to bypass the question.
low = 0
high = 1990
DoB = -1
while True:
    if DoB >= 1991:
        print("""A perfect age full of youth.
         
(Your biometrics are now being recorded)""")
        time.sleep(2.5)#2.5
    elif low <= DoB <= high:
        print("""What were the dinosaurs like back then?
You may be too old for this test.

(Your biometrics are now being recorded)""")
        time.sleep(2.5)#2.5
    elif DoB != -1:
        print("If you don't understand the question, have your mom help you.")

    if DoB >= 0: break
    try:
        DoB = int(input("lets start with your age. What year were you born, hmmm?"))
    except ValueError:
        print("We will use that as a birth year once we have run out of numbers."
              " For now lets just use a four digit year, ok?")
# Ok, let's add an inventory system.

print("""However my webcams can see you are beginning to lose interest. Humans like
things, what if I give you something to play with?""")


time.sleep(4)#4

inv_items = ["chapstick", "comb",
             "fortunecookie"]  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<player inventory
inv_details = ["A glossy stick of lip sealant.", "Looking dapper with a fine toothed comb is easy",
               "That is probably stale. maybe it will give you direction when you need it."]
# first choice of the game, which bag they will use.

print("Here is a fanny pack.")
time.sleep(3)#3
bagtype = "unselected"
while bagtype != "click":
    if bagtype == "no click": break
    bagtype = input(">>>Choice: Click the fanny pack around your waist or continue unarmed. click/no click:").lower()
    if bagtype == "click":
        print(">>>You look as glorious as your mother.")
    elif bagtype == "no click":
        print("""Are you sure?
What about storing knick knacks you find?""")
    else:
        print("Failed to understand your ranting inputs. Just make a choice and move on.")

if bagtype == "no click":
 print("""Well you probably will get made fun of and bullied, but that is not my fault.
Put on this backpack.""")
 time.sleep(2)#2
if bagtype == "no click":
    bagtype = "backpack"
else:
    bagtype = "fanny pack"
print(">>>Against your better judgement you have equipped the", bagtype, """
   Cue the triumphant music!""")
time.sleep(4)#4
print(""">>>You now have an inventory.
You may look in your""", bagtype, """at any time by typing """ + bagtype)
print(">>>to continue adventuring type next.")




coms_input = "none"
brute_force_guard = (0)
held_item = "none"
coms_dex = [str(dex).zfill(3) for dex in range(1000)]#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<console
coms_script = {"666":"Seek your fortune with lucky numbers,and you will see what is next."
    , "000":"The package should have been recieved already. You are running out of time.", "429":"""You have assumed to
stop the shadow arcitects work I see...that makes us allies. Connect to port 746.""", "746":"Downloading virus>>>>"}





while True:#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<This is the main game loop, it contains the
           #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<def functions that the player interacts with.


# def combat():
 def coms():
    global coms_input
    global brute_force_guard
    global coms_dex
    print(">Attempting to redirect to an unsecured port")
    time.sleep(randint(2,4))#2,4
    print(">>>>Port found")
    time.sleep(randint(1,3))#1,3
    print(">>>>>>>>Detection module overridden")
    time.sleep(randint(1,3))#1,4
    print(">>>>>>>>>>>>>>>>Port open.")
    time.sleep(randint(1,2))#1,2
    print(""">To disconect console type close.
Enter target tri-digit(___):""")
    while True:
     brute_force_guard += (1)#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Should be obvious, but this is to limit players
     if brute_force_guard == (6):#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<from just guessing 3 digit numbers.
         print("You are drawing too much attention to your ip address, human..(six hundred sixty six)")
     if brute_force_guard == (11):
         print(">>>To many modules accessed///protocol activated///disconnected")
         break
     if coms_input == "746":
         time.sleep(3)
         print("(; thanks for playing for real. bye now.")
         time.sleep(5)
         break
     coms_input = input(">>").lower()
     if coms_input == "close": break
     for digit in coms_dex:
         if digit == coms_input.zfill(3):
             try:print(coms_script[coms_input])
             except:
                 print("...no server port discovered.")
     if not coms_input.zfill(3) in coms_dex:
      print("""<Not a valid input.>
Security protocols intiated: Port closed""")
      break


 def bag():# Access to their chosen bag.
  print(">>>You opened your " + str(bagtype) + """. 
   To close your """ + str(bagtype) + """ type close.
   To view the items you are carrying type rummage.
   To view an item in more detail type its name.""")
  while True:
   global held_item
   action = input(">>").lower()
   for pockets in inv_items:
       if action == ("take "+pockets):
           if held_item != "none":
               print("You stored your " +str(held_item)+ " in your "+bagtype+ """, 
and are now holding your """+str(pockets))
               held_item = pockets
               break
           else:
               held_item = pockets
               print("You took out your " + held_item)
               break
   if action == "rummage":
    for pockets in inv_items:
     print(pockets)
    print(">>To take an item out of your " + bagtype + ", type take *item*")
   else:
    for pockets in inv_items:
     if pockets == str(action):
      examine = inv_items.index(action)
      print(inv_details[examine])
      break
     if action == "close":
      if bagtype == "fanny pack":
       print("You zipped your " + str(bagtype) + " closed.")
       break
      else:
       print("Your " + str(bagtype) + " was buckled up tightly.")
      break
    if action == "close":
        break

 if coms_input == "746":
     break
 action = input(">").lower()
 if action == bagtype:
  bag()
 if action == "console":
     coms()
 if action == "next":
  if held_item != "fortunecookie":
    print("Thanks for playing!")
    time.sleep(3)
    print("...if you want more, try accessing the shadow architects contacts through his console.")
  if held_item == "fortunecookie":
      print("You break open the fortunecookie. There is no fortune here; Only a three digit lucky number: 429")
      inv_items.remove("fortunecookie")
      held_item = "none"
