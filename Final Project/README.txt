# =============================================================================
#   Noam Benkler
#   March 14, 2018
#   README.txt
#   This README file describes the features of the program, instructions on
#     how to run the program, neccesary add-ons to properly
#     run the code, and citation for the images, sounds, and source code
#     used for inspiration and information in the coding of this program.																				      		  		
#        																																
#         																																
# =============================================================================

Ordered list:
    1. DESCRIPTION
    2. INSTRUCTIONS
    3. DATA
    4. OTHER FILES AND LIBRARIES
    5. BUGS        
    6. NOTES
    7. BIBLIOGRAPHY

==== 1. DESCRIPTION ====

The Monty python memory game is a card game where 18 cards are arranged face down
the player tries to find identical pairs of two cars. 
If the two cards match, they are removed from the gameplay.
If they do not match, the cards are turned back over. The object 
of the game is to find pairs of matching cards in the fewest number of turns 
possible.

==== 2. INSTRUCTIONS ====

This game uses the "pygame" module (http://pygame.org). 
To play this game, you must have python3 and pygame and installed 
on your computer. If you need to download either follow
the links below.

Python: 
(1) http://python.org/getit/

Pygame: 
(1) http://pygame.org/install.html
(2) http://pygame.org/download.shtml

After you have python and pygame downloaded, to start the game, unzip the 
"Monty Python Memory Game Source Code" file, copy the folder into the directory of
your choice, and run the "memory.py" file through whatever windows editor
you use. Once the "memory.py" file is run, the game should automatically start.
To end the game hit the "esc" key on your keyboard. 
 
==== 3. DATA ====

This game uses a number of images and sounds. There are 18 playing cards 
located in the "img" folder, and 8 sound files located in the "snd" folder.

==== 4. OTHER FILES & LIBRARIES ====

Other than the memory.py there are two other files this program
needs to run, named "gameBoard.py" and "gameMusic.py." 

"gameBoard.py" sets up and displays the game board and playing cards. It also 
reads the images and fonts files from the "img" & "fnt "directories.

"gameMusic.py" sets up the game music. It also reads the .ogg and .wav files 
from the "snd" directory.

For the program to run smoothly these files must be located in the same directory as
"memory.py"

memory.py imports the libraries "sys", "os", and "pygame" as well as "gameBoard" and "gameMusic"

gameBoard.py imports the libraries "sys", "os", "random", and "pygame"

gameMusic.py imports the libraries "pygame", and "os"


==== 5. BUGS ====

Though code runs perfectly, terminal always returns two errors which I have not yet discovered how to fix.
1. libpng warning: iCCP: known incorrect sRGB profile
2. libpng warning: iCCP: cHRM chunk does not match sRGB

==== 6. NOTES ====

• I used 3 games found at:
 (http://www.pygame.org/project-Memory-1263-.html, 
 https://codereview.stackexchange.com/questions/127836/memory-game-using-python-and-pygame,
 and http://www.programmingnotes.org/?p=3997) 
 as the base for my work, and to learn how to use Pygame.

• The images and music used for this game are credited below 
  
• The fonts were found online (http://1001freefonts.com)

==== 7. BIBLIOGRAPY ====

Source Code Inspiration:
	http://www.pygame.org/project-Memory-1263-.html
	https://codereview.stackexchange.com/questions/127836/memory-game-using-python-and-pygame
	http://www.programmingnotes.org/?p=3997

Images:
	Card backs:
		 https://theredlist.com/wiki-2-17-1483-1492-1494-view-comedy-romance-10-profile-monty-python-s-flying-circus.html

	Soft Cushion:
		https://www.pinterest.com/pin/350506783491478838/

	Comfy Chair:
		https://www.allmovie.com/movie/monty-pythons-flying-circus-a-book-at-bedtime-v210940

	The Rack:
		http://www.ebay.co.uk/bhp/dish-drainer-tray

	Fear:
		Origional:https://www.dohardmoney.com/run-away-get-bad-rei-deal-quickly/
		Alternative: http://hero.wikia.com/wiki/Sir_Robin

	Surprise:
		http://putlockers.tf/watch/mx5z02GR-monty-python-and-the-holy-grail.html

	Ruthless efficiency:
		Origional: http://wonkville.net/2016/02/05/french-cheese-eaters-upset-at-removal-of-word-berets/
		Alternate: https://thecrookedpen.com/tag/netflix/

	An almost phanatical devotion to the pope:
		https://www.youtube.com/watch?v=7rmD7FEw3AM

	Nice Red Uniforms
		http://www.freerepublic.com/focus/f-chat/3531290/posts

	Our Weaponry
		https://i.ytimg.com/vi/rWq1lLi55Sc/hqdefault.jpg

	Heresy by Deed
		https://solascendans.com/2012/02/14/live-at-the-witch-trials/
	
	Heresy by Word
		https://www.youtube.com/watch?v=FQ5YU_spBw0

	Heresy by Thought
		http://www.dailymail.co.uk/news/article-1038833/How-fly-cleaned-bathroom-Cameron-Obama-united-just-nudge-nudge.html

	Heresy by Action
		http://1.bp.blogspot.com/_RfxxdzJ7g-I/TTsReghq05I/AAAAAAAAD1o/FNp1JdcWrAk/s1600/BrianLeben.jpg

	Diabolical Laughter:
		http://s2.dmcdn.net/JGD86.jpg

	Diabolical Acting:
		http://d1gjpyq0w94yrb.cloudfront.net/wp-content/uploads/2016/09/12152443/monty-python-25.jpg

	Interroigation:
		http://putlockers.tf/watch/mx5z02GR-monty-python-and-the-holy-grail.html

	Confession:
		http://putlockers.tf/watch/mx5z02GR-monty-python-and-the-holy-grail.html
	
	A piece of wood:
		https://img0.etsystatic.com/035/1/8226732/il_340x270.611925060_qshx.jpg

	The Black Knight:
		http://images.fanpop.com/images/image_uploads/The-Black-Night-monty-python-and-the-holy-grail-591468_800_441.jpg 

	Old woman:
		https://people.csail.mit.edu/paulfitz/spanish/t10.html

	Archimedies:
		https://bikesandphilosophydotcom.files.wordpress.com/2017/04/monty-python-football.jpg?w=1200

	Kamikaze Scottsman:
		http://www.dailymotion.com/video/x2qdr1a

Music:
	All music used in the program was downloaded from (http://www.montypython.net/fullsongs.php) and edited using Audacity



----------















																																				self.SCREEN.blit(joke,(titleHeight-100,titleWidth-125))
																																				self.SCREEN.blit(joke2,(titleHeight-100,titleWidth-100))
																																				self.SCREEN.blit(joke3,(titleHeight-100,titleWidth-50))

