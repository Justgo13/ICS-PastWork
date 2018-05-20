% These are SUB-PROGRAMS to allow for shorter code and re-usability of code segments
% that occur more than once in the program, for example, I have the 'goodnight' procedure
% run everytime a user gets to the end of a path of choices
%
% Scroll down to find the beggining of the MAIN program, where execution starts!

var ans, again : string
setscreen("graphics:700;500")

procedure goodnight
    % This is the graphics part of my program that includes an annimation
    var any:string(1)
    put "Hit any key to continue"
    getch (any)
    cls
    drawfill (1, 1, 20, 20)

    var xMoon := 250
    var yMoon := 50
    % This loop simulates the moon rising in the sky
    loop
	drawarc (xMoon - 50, yMoon + 50, 100, 100, 285, 345, white)
	drawarc (xMoon, yMoon, 50, 50, 245, 30, white)
	drawfill (xMoon, yMoon - 45, white, white)
	exit when xMoon > maxx - 60
	delay (50)
	drawarc (xMoon - 50, yMoon + 50, 100, 100, 285, 345, 20)
	drawarc (xMoon, yMoon, 50, 50, 245, 30, 20)
	drawfill (xMoon, yMoon - 45, 20, 20)
	xMoon += 5
	yMoon += 5
    end loop

    var xStar, yStar : int
    % This loop has random stars appearing in the sky
    for i : 1 .. 25
	randint (xStar, 10, maxx - 50)
	randint (yStar, 150, maxy - 50)
	drawfillstar (xStar, yStar, xStar + 30, yStar + 30, yellow)
	delay (100)
    end for

    var font := Font.New ("Palatino:30:bold,italic")
    Font.Draw ("Good night!", 230, 30, font, 10)
    delay(3000)
end goodnight

function valid (choice : string) : boolean
    % This function will check if the user's choice is valid 
    if choice = "A" or choice = "a" or choice = "B" or choice = "b" or choice = "C" or choice = "c" then
	result true
    else
	put "Not a valid choice, try again"
	result false
    end if
end valid

procedure secondPeriod
    % This procedure just has the question and choices for second period classes
    % It is used to avoid typing all the put statements multiple times, as I use it a few times
    put "You are on time for period 2 in which there is a new lesson, followed by lunch."
    put "For lunch, do you:"
    put "A. Eat what your Mom packed for you"
    put "B. Buy a lunch in the cafeteria"
    put "C. Go outside the school for lunch"
end secondPeriod

procedure afterLunch
    % This procedure includes a branch of the program that occurs more than once
    % depending on choices, 
    case ans of
	label "A", "a" :
	    put "You enjoy a relatively nutricious lunch sitting in the hall with a few friends"
	    put "You make it on time to your period 3 class where you are able to finish and"
	    put "hand in an important assignment. Now on to the last period of the day."
	    put "You attend your last class for an important lesson, then go home at the end of the day"
	    put "You enjoy your evening wathcin TV and playing games"
	    put "Good night!"
	label "B", "b" :
	    put "You have some junk food from the cafeteria, but eat the fruit your Mom packed"
	    put "You go to your 3rd period class where there is an assignment to finish"
	    put "Your stomach doesn't feel well and you need to run out to be sick. Do you"
	    put "A. Hand in what you've done, call home to pick you up"
	    put "B. Keep going, finish the assignment, then go to the office and call home."
	    put "C. Keep going, and not call home. Try to finish off the day in school."
	    loop
		get ans
		exit when valid (ans)
	    end loop
	    if ans = "A" or ans = "a" then
		put "You get home and are able to sleep off the sick feeling."
		put "You receive a low grade on your assignment, which is dissappointing."
		put "You did miss an important lesson in the last period, but are able to ask"
		put "a friend for the notes and catch up. Good night!"
	    elsif ans = "B" or ans = "b" then
		put "You are able to finish the assignment and receive a pretty decent grade."
		put "You are pretty happy, and are able to go home and sleep it off."
		put "You do miss an important lesson in the last period, but are able to ask"
		put "a friend for the notes and catch up. Good night!"
	    else
		put "You push through your sick feeling, and get the assignment done."
		put "You are satisfied with your mark, and go to your last class."
		put "Halfway through the last class, you need to be sick again."
		put "You almost faint in class and the teacher calls the office."
		put "The office has you rest then calls an ambulance and parents."
		put "You wind up waiting in the hospital for hours that ruins your"
		put "parent's and your night, but wind up alright, go home and sleep."
		put "Good night."
	    end if
	label "C", "c" :
	    put "You walk down the street with some friends for lunch"
	    put "You enjoy your lunch and chatting with your friends, but wind up being late back to school."
	    put "You stay a little late to try and finish the assignment, but still receive a low grade."
	    put "It's dissappointing, and you wind up late for the last period as well."
	    put "Your last period teacher keeps you after class for a few minutes, which makes you miss the bus."
	    put "Do you:"
	    put "A. Call your parents for a ride"
	    put "B. Wait for the next city bus"
	    put "C. Walk home (a 30 min walk is good exercise!)"
	    loop
		get ans
		exit when valid (ans)
	    end loop
	    if ans = "A" or ans = "a" then
		put "A parent come to pick you up. They are angry about your lates and low grades."
		put "They ground you for a few days and have you do make-up school work."
		put "Good night!"
	    elsif ans = "B" or ans = "b" then
		put "It takes you a while to get home, but once there your parents have received"
		put "notice of your lates and low grades. You will not be getting your allowance"
		put "this week. Good night!"
	    else
		put "It starts raining on the way home, and you have no coat or umbrella."
		put "You arrive home wet and cold. Your parents feel sorry for you even"
		put "though they found out about a few lates and low grades."
		put "You are able to relax a bit that evening. Good night!"
	    end if
    end case
end afterLunch

procedure skipping
    % Again, another short proceudure to avoid typing the put statements multiple times
    put "You miss a pop quiz, are now late on an assignment that was due and "
    put "the school called your parents, so now you are grounded for a week!"
    put "Goodbye!"
end skipping


% ******************************************************************************************************
% START of MAIN program
% ******************************************************************************************************

loop
    cls
    put "It's a pretty normal, pleasant spring and school day."
    put "Do you:"
    put "A. Wake up on time to get to school"
    put "B. Sleep in and take you time, being late for school."
    put "C. Skip school, message your friends and go hang out with them"
    loop
	get ans
	exit when valid (ans)
    end loop

    case ans of
	label "A", "a" :
	    put "You arrive at school and meet up with your friends. They want to skip school"
	    put "on this lovely day. You're not sure what to do, but finally arrive at a decision:"
	    put "A. Excuse yourself and go straight to class"
	    put "B. Start out with them, but think better of it and return to class a little late"
	    put "C. Go with them and have fun shopping"
	    loop
		get ans
		exit when valid (ans)
	    end loop
	    if ans = "A" or ans = "a" then
		put "The teacher has assigned a pop quiz, which is pretty easy and you pass!"
		secondPeriod
		loop
		    get ans
		    exit when valid (ans)
		end loop
		afterLunch
	    elsif ans = "B" or ans = "b" then
		put "The teacher has assigned a pos quiz, which you are late for."
		put "You do what you can, but do not pass the quiz"
		secondPeriod
		loop
		    get ans
		    exit when valid (ans)
		end loop
		afterLunch
	    else
		skipping
	    end if
	label "B", "b" :
	    put "You arrive late to school, sign in and go straight to class"
	    put "The teacher just gave a pop quiz, and lets you have 5 minutes to write it."
	    put "You are not able to finish so receive a failing grade."
	    secondPeriod
	    loop
		get ans
		exit when valid (ans)
	    end loop
	    afterLunch
	label "C", "c" :
	    skipping
    end case
    goodnight
    cls
    put "Do you want to play again? Y/N "
    get again
    exit when again = "N" or again = "n"
end loop
