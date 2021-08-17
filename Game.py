def personality_quiz():
    garnet = 0
    steven = 0
    amethyst = 0
    pearl = 0

    print('"Cool!  Hey, uh, there\'s this gem quiz, like, uh, which Crystal Gem are you?  You wanna take it?"')
    print("[Y]es or [N]o?")
    take_quiz = input(">   ")
    take_quiz = take_quiz.upper()
    if take_quiz == "Y":
        print('"Okay, first question.  How would you describe your personality? A, Leader, B, Friendly, C, Impulsive, or D, Tidy?"')
        quiz1 = input(">  ")
        quiz1 = quiz1.upper()
        if quiz1 == 'A':
            garnet += 1
        elif quiz1 == "B":
            steven += 1
        elif quiz1 == "C":
            amethyst += 1
        elif quiz1 == "D":
            pearl += 1
        print('"Okay, second question.  What animal do you like better?  A, Cat, B, Dogcopter, C, Puma, or D, Swan?"') 
        quiz2 = input(">  ")
        quiz2 = quiz2.upper()
        if quiz2 == 'A':
            garnet += 1
        elif quiz2 == "B":
            steven += 1
        elif quiz2 == "C":
            amethyst += 1
        elif quiz2 == "D":
            pearl += 1
        print('"Cool, cool.  Okay, Which of the following colors would you pick?  A, Maroon, B, Pink, C, Purple, or D, Pastels?"')
        quiz3 = input(">  ")
        quiz3 = quiz3.upper()
        if quiz3 == 'A':
            garnet += 1
        elif quiz3 == "B":
            steven += 1
        elif quiz3 == "C":
            amethyst += 1
        elif quiz3 == "D":
            pearl += 1
        print('"Okay, last question.  What\'s your favorite hobby?  Is it A, Stargazing, B, Playing Music, C, Eating, or D, Sword Fighting?"')
        quiz4 = input(">  ")
        quiz4 = quiz4.upper()
        if quiz4 == 'A':
            garnet += 1
        elif quiz4 == "B":
            steven += 1
        elif quiz4 == "C":
            amethyst += 1
        elif quiz4 == "D":
            pearl += 1
        if garnet + steven + pearl + amethyst < 4:
            print('"You coulda just said you didn\'t want to do the quiz."')
            print('The boys starts looking at his phone again, clearly ignoring you.')
        else:
            if garnet == steven == amethyst == pearl:
                print('"You got Obsidian!  That\'s fucking sick, dude!"')
            elif (garnet > steven) and (garnet > amethyst) and (garnet > pearl):
                print('"You got Garnet!  Yo, square mom is the best!"') 
            elif (steven > garnet) and (steven > amethyst) and (steven > pearl):
                print('"You\'re Steven!  I love that funky little dude!"')
            elif (amethyst > garnet) and (amethyst > steven) and (amethyst > pearl):
                print('"You\'re Amethyst?  Yeah, that tracks."')
            elif (pearl > garnet) and (pearl > steven) and (pearl > amethyst):
                print('"You got Pearl? What are you doing here?"')
            elif garnet == steven == 2:
                print('"Sunstone!  Sick!"')
            elif garnet == amethyst == 2:
                print('"Yo, Sugilite is fucking hot!  Did you know she\'s voiced by Nicki Minaj?"')
            elif garnet == pearl == 2:
                print('"You got Sardonyx.  Kinda a weird one."')
            elif steven == amethyst == 2:
                print('"Smoky Quartz!  Cool!"')
            elif steven == pearl == 2:
                print('"You got Rainbow Quartz!  I wonder which version?"')
            elif amethyst == pearl == 2:
                print('"All I wanna do, is see you turn into, a giant woman!  A GIANT WOMAN!"')
            print("He grins at you for a second before looking at his phone again.  It only takes a few seconds for him to become oblivious to your presence again.")
    else:
        print('"Oh, whatever, that\'s cool."')

def game():
    spoke_to_burly_boy = False
    current_room = "start"
    wrong_input = 0
    times_in_diningroom = 0

    def entryway():
        print("But, wait. \n You can't leave now, you don't have your keys yet. \n")
        print("Ugh!  This is the worst, but you need to find them! \n You turn back around to search some more. \n")
        livingroom()
    def livingroom():
        print("\n Alright, you're in the livingroom.  What would you like to do next?")
        print("[S]earch the living room. \n [E]xit through the front door.")
        print("[H]allway seems promising.\n [D]ining room, I guess?")
    def hallway():
        print("You're in a very long hallway, with several doors.  What would you like to do next?")
        print("[B]ack to the living room.")
        print("[G]otta check the dining room.")
        print("[M]aybe the bathroom?")
        print("[T]hat bedroom seems likely.")
        print("[K]itchen's always a good idea.")
        print("[U]pstairs, for sure.")
        print("[C]heck for my keys.")   
    def diningroom():        
        print("You're in the dining room, where the band was playing last night.")
        print("What do you want to do?")
        print("[R]eturn to the living room.")
        print("[V]eer back towards the hallway.")
        print("[P]oke around and look for your keys.")
    def diningroom2():
        print("The boy looks up this time when you walk in.  He kind of squints at you for a second before lighting up. \n")
        print(f'"Hey!  You\'re {player_name}, right?  Hey, uh, do you like Steven Universe?" \n')
        print('[Y]es or [N]o')
        take_quiz = input(">  ")
        take_quiz = take_quiz.upper()
        if take_quiz == "Y":
            personality_quiz()
        else:
            print('"Ah, okay, nevermind." \n The boy starts looking at his phone again.')
# use variable times_in_diningroom to call personality quiz on second visit to dining room.  copy quiz into functions section.
    def downstairsbath():
        print("You're in the downstairs bathroom. \n What do you want to do?")
        print("[J]ust take a quick look around.")
        print('[N]ope! Back to the hallway.')
    def downstairsbed():
        print("You're in a bedroom.  What do you want to do?")
        print("[Y]ou know I'm looking for the keys.")
        print("[W]alk back into the hallway.")
    def kitchen():
        print("You're in the kitchen.  What would you like to do?")
        print("[I] better look for my keys.")
        print("[O]ut to the hallway again.")
    def upstairslanding():
        print("You're upstairs.  What would you like to do?")
        print("[Z]oo.  It's a zoo.  I gotta search it, though.")
        print("[Q]uestion your life choices.  Cry.")
        print("[F]uck it, I'm going back downstairs.")
    
    print("THE LOST KEYS")
    print("___________________\n\n What is your name?")
    player_name = input(">  ")
    if len(player_name) < 5:
        print("Short and sassy!  I fucking love it!  You have the best name!")
    elif len(player_name) < 10:
        print("What a great name! Classic, beautiful, elegant, perfection!")
    else:
        print("That whole thing is your name?!  Yes, betch!!!!  Fucking phenomenal!")

    print()
    print(f"Alright, {player_name}, here's the situation.")
    print("You are a hungover college girl who left her keys at a frat house.")
    print("Your drunk ass walked home, pounded on your apartment door, got let in by your rightfully disgruntled roommates, and proceeded to pass out on the couch.")
    print("Apparently you puked in the toilet before passing out.  You might not remember that, though.  You were pretty drunk.")
    print("Oh, also, if at any time you want to quit searching and, like, go get some tacos or something, just hit [X] the next time I ask you what you want to do.")
    print("Anyway, it's now the next morning.  You've schlepped back to the frat house and you're standing there, right in front of the front door.  This is actually a novel experience for you.  You've never been to a frat house in broad daylight before.")
    print("You hear a voice through the door.")
    print('\n"What are you doing," it asks.\n')

    print("How would you like to respond?")
    print("[A]nswer the question \n [L]eave")

    while True:
        answer = input(">  ")
        answer = answer.upper()

        if current_room == "hall" and spoke_to_burly_boy == True:
            print("A few moments later, you hear a distant thundering.  It's coming from upstairs and it's getting louder and louder.  One assumes that how you feel in this moment is how Simba felt seeing the wildebeest stampede through the ravine as a horde of large young men all thunder down the stairs, making a beeline for you.")
            print('\n"Someone tell the girl!" One of them shouts, faceless in the mob.  "Girl!  Hey, GIRL!!!  We found your keys, girl!!!"')
            print("\nThey circle around you.  You haven't felt that small since you were maybe eleven years old.  One of them splits himself off from the crowd.")
            print('\n"Are these-" he pulls out a ring of keys from his pocket, "your keys?"')
            print("And lo, there is the distictive bright millennial pink cat keychain dangling off the ring.\n")
            print('"Yes," you whisper.  "Oh my god, yes."\n')
            print('"EYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY!!!"\n The cheer went up.\n')
            print('Turns out he found them in the bathroom upstairs.  You thank them again profusely.  There\'s a scattered round of "no problems" and then, just as suddenly as they descended, they all dispersed, like ships in the night.')
            print(f"\n Congratulations, {player_name}!  You've found your keys!  You win!")
            break            
        if answer == "A" and current_room == "start":
            print('"I lost my keys in here last night," you call back.  "I was seeing if I could go in and look for them?"\n')
            print("He opens the door and gestures for you to go in.\n \"Go wherever you want.\"\n")
            print("You've never seen a frat house post-party before.  There are hungover and still-drunk frat boys stumbling around in their socks and sandals and gym shorts, seeking out food and showers like moths to a porch light.  A few of them throw puzzled glances your way.  You're sure they think you're some post-bacchanalia hallucination.")
            current_room = "living"
            livingroom()
        elif answer == "B" and current_room == "hall":
            print("You decide to head back to the living room.\n")
            current_room = "living"
            livingroom()
        elif answer == "C" and current_room == "hall":
            print("The hallway has so many randomly dropped items in it: discarded accessories, empty cans and bottles, a tuba, several pairs of shoes.  Perhaps your keys are among them?  You carefully scan the ground, nudging the various piles with your shoe.  No dice.  You don't see your keys.")
            print()
            hallway()
        elif (answer == "D" and current_room == "living") or (answer == "G" and current_room == "hall"):
            print("This is where the band was set up, so maybe your keys are here?  You enter the dining room.\n")
            current_room = "dining"
            times_in_diningroom += 1
            if times_in_diningroom == 2:
                diningroom2()
            diningroom()
        elif answer == "E" and current_room == "living":
            print("You head for the front door.\n")
            entryway()
        elif answer == "F" and current_room == "up":
            print("The stairs seem even more treacherous going down.\n")
            current_room = "hall"
            hallway()
        elif answer == "H" and current_room == "living":
            print("You head towards the hallway.\n")
            current_room = "hall"
            hallway()
        elif answer == "I" and current_room == "kitch":
            print("The kitchen is a mess.  Aside from the wildly overflowing trashcan in the corner, there are dishes piled high in the sink.  Every surface is covered in empty food containers of some kind.  From pizza boxes to empty chip bags to a small cluster of abandoned fortune cookies and take-out boxes.  Beer bottles and red solo cups balance precariously on every windowsill.  You begin to rummage, hope flagging as your keys fail to appear.")
            print()
            kitchen()
        elif answer == "J" and current_room == "bath":
            print("The floor is so sticky, and you know it's not all spilled beer.  You find an empty toilet paper roll on top of the toilet that's dry, and use it to prod the moist detritus on the floor.  You're kind of praying your keys aren't in here, absorbing the mixture of booze and effluvia.  Luck's with you, you don't see your keys in the slop.")
            print()
            downstairsbath()
        elif answer == "K" and current_room == "hall":
            print("You walk into the kitchen.\n")
            current_room = "kitch"
            kitchen()            
        elif answer == "L" and current_room == "start":
            print ("You decide to give up and just leave.")
            break
        elif answer == "M" and current_room == "hall":
            print("The fumes wafting out almost make you change your mind, but you enter the bathroom.\n")
            current_room = "bath"
            downstairsbath()
        elif (answer == "N" and current_room == "bath") or (answer == "O" and current_room == "kitch"):
            print("You go back to the hallway.\n")
            current_room = "hall"
            hallway()
        elif answer == "P" and current_room == "dining":
            print("There's a boy in socks and sandals standing in the middle of the room, looking at his phone.  He doesn't look up from it as you pick through the room, checking the cavities of amps and slivers of space behind the pushed-aside furniture.  No luck, you don't see your keys anywhere.")
            print()
            diningroom()
        elif answer == "Q" and current_room == "up":
            print("Twenty minutes have passed.  You've searched just about every bedroom and nuclear-waste-dump-site of a bathroom in the house.  You've given up on ever finding your keys and are preparing yourself to beg your roommates' forgiveness and get a new set copied.")
            print("As you stand there in the upstairs hallway, silently bewailing your predicament, a particularly-burly frat boy approaches you.")
            print('\n"You need help with something?"\n')
            print("(Well, do you?  [Y]es or [N]o?)")

            help = input(">  ")
            help = help.upper()

            if help == "Y":
                print('"I lost my keys here last night and I can\'t find them, I\'ve looked everywhere."\n')
                print('"What do they look like?  I\'ll put it into the group chat," he said, already pulling out his phone.')
                print('No one ever checks a group chat, you think, but what the hell.  It\'s worth a shot.  "Um, it\'s just a ring of keys.  The keychain is a pink plastic cat, though, like yea big.  Like, bright pink, you can\'t miss it."')
                print("He nods, presumably typing this description faithfully into the group chat.")
                print('"Alright, I sent the message out.  Good luck."  And with that, he turns and leaves.')
                spoke_to_burly_boy = True
                upstairslanding()
            elif help == "N":
                print('"No," you tell him.\n You turn away from him and try to think of what to do next. \n')
                upstairslanding()
            else:
                print("He gives you a quizzical look.")
                upstairslanding()

        elif answer == "R" and current_room == "dining":
            print("You go back to the living room. \n")
            current_room = "living"
            livingroom()
        elif answer == "S" and current_room == "living":
            print("The room is a swamp of empty pizza boxes and beer cans.  There's a trashcan in the corner overflowing with garbage.  People clearly kept stacking their garbage long after the can filled up, and it's now a precarious tower of refuse.  The couch cushions are damp when you search the couch, and you hope it's only spilled beer.  You go through the room as carefully as you can, but don't see your keys anywhere.")
            print()
            livingroom()
        elif answer == "T" and current_room == "hall":
            print("The door is open, so you walk into what looks like a bedroom. \n")
            current_room = "bed"
            downstairsbed()
        elif answer == "U" and current_room == "hall":
            print("You head towards the stairs at the end of the hallway and begin to climb, avoiding slippery pieces of discarded clothing as you go. \n")
            current_room = "up"
            upstairslanding()
        elif (answer == "V" and current_room == "dining") or (answer == "W" and current_room == "bed"):
            print("You turn back to the hallway. \n")
            current_room = "hall"
            hallway()
        elif answer == "X":
            print("Okay, go get some tacos.  You can try again another time.")
            break
        elif answer == "Y" and current_room == "bed":
            print("You enter a room where a boy is drunkenly watching some Old Yeller-esque movie on a tiny TV in the corner of the room from his bed.")
            print('"Do you like dog movies?" he asks, voice all mumbly from grogginess and also from the fact that his face is squished against his pillow and half-buried by his blanket.')
            print("\n You tell him you do. \n")
            print("He mumbles again, pleased, and asks what you're doing.  You tell him you're looking for your keys.")
            print('"Sorry, I haven\'t seen any keys around here." \n You don\'t doubt him. \n')
            downstairsbed()
        elif answer == "Z" and current_room == "up":
            print("You've heard this area colloquially referred to as 'Fight Club' and you can see why.  Plywood has been haphazardly hammered into a series of dividers, carving out several \"bedrooms.\"  There are stickers and lewd doodles on every inch of the space, and the \"doors\" are no more than bedsheets and shower curtains nailed into place.  You begin a half-assed search of the area, fairly certain you didn't come up here last night, but still desperate to find your keys.  There's another noxious ruin of a bathroom up here, which you search as well.  Still no keys!")
            print()
            upstairslanding()

        else:
            if wrong_input < 1:
                print("Are you still drunk?  That's not an option.")    
            elif wrong_input < 2:
                print("That's not an option.  You're still drunk, aren't you?  That's okay, I'll repeat myself.")   
            elif wrong_input < 3:
                print("How many drinks did you have last night?  No worries, I'll say it again.") 
            elif wrong_input < 4:
                print("Just, okay, sweetie.  That's not actually an answer.")
            elif wrong_input < 5:
                print("Once more, from the top.")
            elif wrong_input < 6:
                print("Uh... you can't actually do that.")
            else:
                print("Pay attention.  Ugh.  Maybe we should just start over.")
                game()
            wrong_input = wrong_input + 1

game()
