% Game start
% Column is x
% Row is y
import GUI
var font1 : int
var font2 : int
var font3 : int
var font4 : int
font1 := Font.New ("Times.New.Roman:12")
font2 := Font.New ("Times.New.Roman:75:bold")
font3 := Font.New ("Comicsans:65:bold")
font4 := Font.New ("Comicsans:65:bold")
setscreen ("graphics:500;500")
drawfill (1, 1, black, black)
Font.Draw ("CONNECT", 50, 250, font3, white)
Font.Draw ("CONNECT", 54, 250, font4, blue)
Font.Draw ("FOUR", 125, 165, font3, white)
Font.Draw ("FOUR", 129, 165, font4, blue)
var count, count1, count2 : int := 0
var tie_count : int := 0
var turns : int := 1
var player : array 1 .. 6, 1 .. 7 of int
var x0 : int := 100
var y0 : int := 115
var xpos : int
var ypos : int
var diagonalpos : int
var x, y, button : int

proc win_red
    % P1 win
    cls
    loop
	Font.Draw ("P1", maxx div 2 - 125, maxy div 2, font2, red)
	Font.Draw ("Wins", maxx div 2 - 100, maxy div 2 - 100, font2, red)
	delay (250)
	cls
	delay (250)
	count := count + 1
	exit when count >= 5
    end loop
    quit
end win_red

proc win_yellow

    % P2 win
    cls
    loop
	Font.Draw ("P2", maxx div 2 - 125, maxy div 2, font2, yellow)
	Font.Draw ("Wins", maxx div 2 - 100, maxy div 2 - 100, font2, yellow)
	delay (250)
	cls
	delay (250)
	count := count + 1
	exit when count >= 5
    end loop
    quit
end win_yellow

proc tie
    delay (4000)
    cls
    loop
	Font.Draw ("TIE", 150, 250, font3, red)
	Font.Draw ("TIE", 154, 250, font4, black)
	Font.Draw ("GAME", 100, 175, font3, red)
	Font.Draw ("GAME", 104, 175, font4, black)
	delay (250)
	cls
	delay (250)
	Font.Draw ("TIE", 150, 250, font3, red)
	Font.Draw ("TIE", 154, 250, font4, black)
	Font.Draw ("GAME", 100, 175, font3, red)
	Font.Draw ("GAME", 104, 175, font4, black)
	count := count + 1
	exit when count >= 5
    end loop
    quit
end tie

procedure Start_game
    % Making the game board
    cls
    drawfill (1, 1, black, black)
    drawfillbox (65, 80, 435, 400, blue)
    for i : 1 .. 7
	for j : 1 .. 6
	    player (j, i) := 0
	    drawfilloval (x0 + (i - 1) * 50, y0 + (j - 1) * 50, 15, 15, 0)
	end for
    end for

    % Checking the mouse click

    loop
	exit when count1 = 4 or count2 = 4 or tie_count = 42
	if turns = 1 then
	    Font.Draw ("PLAYER", 75, 415, font3, red)
	elsif turns = 2 then
	    Font.Draw ("PLAYER", 75, 415, font3, yellow)
	end if

	Mouse.Where (x, y, button)
	if button = 1 then
	    if x < 65 or x > 435 then        %making sure they can't click in out of the box
		put "Invalid choice"
		delay (500)
	    else
		if turns = 1 then % turn = 1

		    for i : 1 .. 7             % checking xpos
			xpos := i
			delay (75)
			exit when x <= (x0 + (xpos - 1) * 50 + 35) and x >= (x0 + (xpos - 1) * 50 - 35)             %exits when the player click in one column
		    end for

		    for j : 1 .. 6             % checking ypos
			ypos := j
			delay (75)
			exit when player (ypos, xpos) = 0 % exit when the piece hits the bottom
		    end for

		    if ypos = 6 and player (ypos, xpos) not= 0 then    % column is full error message
			put "Column is full, please try another column"

		    else
			for decreasing j : 6 .. ypos             % drawing the falling piece

			    drawfilloval (x0 + (xpos - 1) * 50, 365 - (6 - j) * 50, 15, 15, red)
			    delay (75)
			    drawfilloval (x0 + (xpos - 1) * 50, 365 - (6 - j) * 50, 15, 15, white)
			end for
			drawfilloval (x0 + (xpos - 1) * 50, 365 - (6 - ypos) * 50, 15, 15, red)         % draw piece at spot
			player (ypos, xpos) := 1  %set spot to player 1 or 2
			tie_count := tie_count + 1   % count adds 1 each time a player places a piece
			count1 := 1 % counter for the win

			% Red
			% adjacent to the right & left

			if xpos < 7 and xpos > 1 then
			    count1 := 1
			    for i : xpos + 1 .. 7
				if player (ypos, i) = 1 then
				    count1 := count1 + 1
				end if
				exit when player (ypos, i) not= 1
			    end for

			    for decreasing i : xpos - 1 .. 1
				if player (ypos, i) = 1 then
				    count1 := count1 + 1
				end if
				exit when player (ypos, i) not= 1
			    end for
			end if

			if count1 = 4 then
			    put "P1 Wins"
			    delay (3000)
			    win_red

			end if
			% going up & down
			if ypos < 6 and ypos > 1 then
			    count1 := 1
			    for j : ypos + 1 .. 6
				if player (j, xpos) = 1 then
				    count1 := count1 + 1
				end if
				exit when player (j, xpos) not= 1
			    end for
			    for decreasing j : ypos - 1 .. 1
				if player (j, xpos) = 1 then
				    count1 := count1 + 1
				end if
				exit when player (j, xpos) not= 1
			    end for
			end if

			if count1 = 4 then
			    put "P1 Wins"
			    delay (3000)
			    win_red

			end if
			%going diagonal / (down (left)
			count1 := 1
			if (xpos - 1) >= (ypos - 1) then
			    diagonalpos := ypos
			else
			    diagonalpos := xpos
			end if

			for j : 1 .. diagonalpos - 1
			    if player (ypos - j, xpos - j) = 1 then
				count1 := count1 + 1
			    end if
			    exit when player (ypos - j, xpos - j) not= 1
			end for

			%going diagonal / (up (right)
			if (7 - xpos) >= (6 - ypos) then
			    diagonalpos := 6 - ypos
			else
			    diagonalpos := 7 - xpos
			end if

			for j : 1 .. diagonalpos - 1
			    if player (ypos + j, xpos + j) = 1 then
				count1 := count1 + 1
			    end if
			    exit when player (ypos + j, xpos + j) not= 1
			end for

			if count1 = 4 then
			    put "P1 Wins"
			    delay (3000)
			    win_red

			end if
			% going diagonal / (up (left)
			count1 := 1
			if (6 - ypos) >= (xpos - 1) then
			    diagonalpos := xpos - 1
			else
			    diagonalpos := 6 - ypos
			end if

			for j : 1 .. diagonalpos - 1
			    if player (ypos + j, xpos - j) = 1 then
				count1 := count1 + 1
			    end if
			    exit when player (ypos + j, xpos - j) not= 1
			end for

			% going diagonal / (down (right)
			if (7 - xpos) >= (ypos - 1) then
			    diagonalpos := ypos - 1
			else
			    diagonalpos := 7 - xpos
			end if
			for j : 1 .. diagonalpos
			    if player (ypos - j, xpos + j) = 1 then
				count1 := count1 + 1
			    end if
			    exit when player (ypos - j, xpos + j) not= 1
			end for

			if count1 = 4 then
			    put "P1 Wins"
			    delay (3000)
			    win_red

			end if

		    end if
		    turns := 2

		elsif turns = 2 then

		    for i : 1 .. 7
			xpos := i
			delay (75)
			exit when x <= (x0 + (xpos - 1) * 50 + 35) and x >= (x0 + (xpos - 1) * 50 - 35)
		    end for
		    for j : 1 .. 6
			ypos := j
			delay (75)
			exit when player (ypos, xpos) = 0
		    end for

		    if ypos = 6 and player (ypos, xpos) not= 0 then
			put "Column is full, please try another column"

		    else
			for decreasing j : 6 .. ypos
			    drawfilloval (x0 + (xpos - 1) * 50, 365 - (6 - j) * 50, 15, 15, yellow)
			    delay (75)
			    drawfilloval (x0 + (xpos - 1) * 50, 365 - (6 - j) * 50, 15, 15, white)
			end for
			drawfilloval (x0 + (xpos - 1) * 50, 365 - (6 - ypos) * 50, 15, 15, yellow)
			player (ypos, xpos) := 2
			tie_count := tie_count + 1
			count2 := 1

			% Blue
			% adjacent to the right & left

			if xpos < 7 and xpos > 1 then
			    count2 := 1
			    for i : xpos + 1 .. 7
				if player (ypos, i) = 2 then
				    count2 := count2 + 1
				end if
				exit when player (ypos, i) not= 2
			    end for
			    for decreasing i : xpos - 1 .. 1
				if player (ypos, i) = 2 then
				    count2 := count2 + 1
				end if
				exit when player (ypos, i) not= 2
			    end for
			end if

			if count2 = 4 then
			    put "P2 Wins"
			    delay (3000)
			    win_yellow

			end if

			% going up & down
			if ypos < 6 and ypos > 1 then
			    count2 := 1
			    for j : ypos + 1 .. 6
				if player (j, xpos) = 2 then
				    count2 := count2 + 1
				end if
				exit when player (j, xpos) not= 2
			    end for
			    for decreasing j : ypos - 1 .. 1
				if player (j, xpos) = 2 then
				    count2 := count2 + 1
				end if
				exit when player (j, xpos) not= 2
			    end for
			end if

			if count2 = 4 then
			    put "P2 Wins"
			    delay (3000)
			    win_yellow

			end if

			%going diagonal / (down (left)
			count2 := 1
			if (xpos - 1) >= (ypos - 1) then
			    diagonalpos := ypos
			else
			    diagonalpos := xpos
			end if

			for j : 1 .. diagonalpos - 1
			    if player (ypos - j, xpos - j) = 2 then
				count2 := count2 + 1
			    end if
			    exit when player (ypos - j, xpos - j) not= 2
			end for

			%going diagonal / (up (right)
			if (7 - xpos) >= (6 - ypos) then
			    diagonalpos := 6 - ypos
			else
			    diagonalpos := 7 - xpos
			end if

			for j : 1 .. diagonalpos - 1
			    if player (ypos + j, xpos + j) = 2 then
				count2 := count2 + 1
			    end if
			    exit when player (ypos + j, xpos + j) not= 2
			end for

			if count2 = 4 then
			    put "P2 Wins"
			    delay (3000)
			    win_yellow

			end if

			% going diagonal / (up (left)
			count2 := 1
			if (6 - ypos) >= (xpos - 1) then
			    diagonalpos := xpos - 1
			else
			    diagonalpos := 6 - ypos
			end if

			for j : 1 .. diagonalpos - 1
			    if player (ypos + j, xpos - j) = 2 then
				count2 := count2 + 1
			    end if
			    exit when player (ypos + j, xpos - j) not= 2
			end for

			% going diagonal / (down (right)
			if (7 - xpos) >= (ypos - 1) then
			    diagonalpos := ypos - 1
			else
			    diagonalpos := 7 - xpos
			end if
			for j : 1 .. diagonalpos
			    if player (ypos - j, xpos + j) = 2 then
				count2 := count2 + 1
			    end if
			    exit when player (ypos - j, xpos + j) not= 2
			end for

			if count2 = 4 then
			    put "P2 Wins"
			    delay (3000)
			    win_yellow

			end if

		    end if
		    turns := 1
		end if
	    end if
	end if
    end loop

    if tie_count = 42 then
	tie
    end if
end Start_game

procedure Go_back
    cls
    drawfill (1, 1, red, red)
    var button1 : int := GUI.CreateButton (10, 450, 0, "Start Game", Start_game)
    drawfill (1, 1, black, black)
    Font.Draw ("CONNECT", 50, 250, font3, white)
    Font.Draw ("CONNECT", 54, 250, font4, blue)
    Font.Draw ("FOUR", 125, 165, font3, white)
    Font.Draw ("FOUR", 129, 165, font4, blue)
end Go_back

procedure How_to_play
    cls
    drawfill (1, 1, black, black)
    Font.Draw ("1. Decide who plays first. Alternate turns after playing one piece.", 50, 400, font1, white)
    Font.Draw ("2. Red is P1, Yellow is P2 ", 50, 350, font1, white)
    Font.Draw ("3. Click on the open hole where you want to place your piece.", 50, 300, font1, white)
    Font.Draw ("4. When the word player is red then it is P1 vice versa", 50, 250, font1, white)
    Font.Draw ("5. When one person gets four pieces in a row, they win.", 50, 200, font1, white)
    Font.Draw ("6. If all the slots are filled and nobody won then it is a tie. ", 50, 150, font1, white)
    var button3 : int := GUI.CreateButton (50, 50, 0, "Go Back", Go_back)

end How_to_play

var button1 : int := GUI.CreateButton (10, 450, 0, "Start Game", Start_game)
var button2 : int := GUI.CreateButton (10, 425, 0, "How to play", How_to_play)


loop
    exit when GUI.ProcessEvent
end loop















