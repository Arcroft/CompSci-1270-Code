# Ashlyn Croft
# Idk, sometime last week. I am seriously drowning. I worked 2 weeks ahead to finsh another class so I can focus on math/coding this coming week. Week of July28 2025
# Assignment... 6?
# Candy Land style game, I did wreck it ralph, because... No one can stop me? Idk. Its cute.
#  "this is the assignment that many cheat-cheaty-cheaters get caught on."
# I feel like there's a pun to be made about this with candy land, but my brain is fried.
# Regardless I can't do ascii art, so idk if that counts as cheating, but I googled the hell out of it.
# I also copied the emojis.


import random
import os
import time
from colorama import init, Fore, Back, Style

# pretty colors
init(autoreset=True)



class WreckItRalphGame:
    def __init__(self):
        self.board_size = 50
        self.players = []
        self.current_player = 0
        self.special_spaces = self.create_special_spaces()
        


    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    



    def print_logo(self):
        print(Fore.RED + Style.BRIGHT + """
    ╦ ╦╦═╗╔═╗╔═╗╦╔═  ╦╔╦╗  ╦  ╔═╗╔╗╔╔╦╗
    ║║║╠╦╝║╣ ║  ╠╩╗  ║ ║   ║  ╠═╣║║║ ║║
    ╚╩╝╩╚═╚═╝╚═╝╩ ╩  ╩ ╩   ╩═╝╩ ╩╝╚╝═╩╝
    """ + Style.RESET_ALL)
        print(Fore.CYAN + "    🕹️  ARCADE BOARD GAME  🕹️\n" + Style.RESET_ALL)
    




    def print_main_menu(self):
        self.clear_screen()
        self.print_logo()
        
        print(Fore.YELLOW + """
        ╔═══════════════════════════════╗
        ║         MAIN MENU             ║
        ╚═══════════════════════════════╝
        """ + Style.RESET_ALL)
        
        print(Fore.GREEN + """
        [1] START GAME
        [2] INSTRUCTIONS  
        [3] QUIT
        """ + Style.RESET_ALL)
        
        print(Fore.MAGENTA + """
        ┌─────────────────────────┐
        │ "I'M BAD, AND THAT'S   │
        │  GOOD. I WILL NEVER BE │
        │  GOOD, AND THAT'S NOT  │
        │  BAD!"                 │
        └─────────────────────────┘
        """ + Style.RESET_ALL)
    




    def print_instructions(self):
        self.clear_screen()
        self.print_logo()
        
        print(Fore.YELLOW + """
        ╔═══════════════════════════════╗
        ║        INSTRUCTIONS           ║
        ╚═══════════════════════════════╝
        """ + Style.RESET_ALL)
        
        print(Fore.WHITE + """
        OBJECTIVE:
        Be the first to reach Niceland (the finish)!
        
        HOW TO PLAY:
        • Roll the dice to move forward by pressing enter
        • Land on special spaces for power-ups or penalties
        • Choose your favorite character from the movie
        
        SPECIAL SPACES:
        """ + Style.RESET_ALL)
        
        print(Fore.CYAN + "◊ GLITCH" + Style.RESET_ALL + " - Teleport 1-6 spaces forward")
        print(Fore.RED + "◊ WRECK IT" + Style.RESET_ALL + " - Move back 3 spaces")
        print(Fore.YELLOW + "◊ TURBO" + Style.RESET_ALL + " - Double your next roll")
        print(Fore.BLUE + "◊ FIX IT" + Style.RESET_ALL + " - Protection from next penalty")
        print(Fore.MAGENTA + "◊ CHERRY BOMB" + Style.RESET_ALL + " - Others move back 2")
        print(Fore.GREEN + "◊ SUGAR RUSH" + Style.RESET_ALL + " - Zoom forward 5 spaces")
        print(Fore.RED + Back.BLACK + "◊ CY-BUG" + Style.RESET_ALL + " - Skip your next turn")
        print(Fore.YELLOW + Style.BRIGHT + "◊ MEDAL" + Style.RESET_ALL + " - Immunity to penalties")
        
        print(Fore.WHITE + """
        CHARACTERS:
        • Ralph - He wrecks stuff
        • Vanellope - She's a candy princess
        • Felix - His father is Fix it Felix Sr.
        • Calhoun - Married, widowed before honeymoon. Cybugs, what re you gunna do right?
        """ + Style.RESET_ALL)
        
        input("\nPress Enter to return to menu...")
    




    def create_special_spaces(self):
        specials = {}
        # Add special spaces throughout the board
        specials[5] = ("glitch", Fore.CYAN)
        specials[10] = ("wreck_it", Fore.RED)
        specials[15] = ("turbo", Fore.YELLOW)
        specials[20] = ("fix_it", Fore.BLUE)
        specials[25] = ("cherry_bomb", Fore.MAGENTA)
        specials[30] = ("sugar_rush", Fore.GREEN)
        specials[35] = ("cy_bug", Fore.BLACK + Back.RED)
        specials[40] = ("medal", Fore.YELLOW + Style.BRIGHT)
        specials[45] = ("glitch", Fore.CYAN)
        return specials
    


    def get_player_ascii(self, character):
        if character == "Ralph":
            return Fore.RED + "█" + Style.RESET_ALL
        elif character == "Vanellope":
            return Fore.CYAN + "▼" + Style.RESET_ALL
        elif character == "Felix":
            return Fore.BLUE + "▪" + Style.RESET_ALL
        elif character == "Calhoun":
            return Fore.GREEN + "◆" + Style.RESET_ALL
        return "●"
    

    # These suck. Lol. Whatever I guess.

    def print_character_select(self):
        print(Fore.YELLOW + "\n╔═══════════════════════════════╗")
        print("║     CHARACTER SELECT          ║")
        print("╚═══════════════════════════════╝" + Style.RESET_ALL)
        print()
        print(Fore.RED + "1. RALPH" + Style.RESET_ALL + " (Wreck-It Ralph)")
        print("   " + Fore.RED + "  ▄██▄")
        print("   " + "  ████")
        print("   " + "  ▀██▀" + Style.RESET_ALL)
        print()
        print(Fore.CYAN + "2. VANELLOPE" + Style.RESET_ALL + " (The Glitch)")
        print("   " + Fore.CYAN + "  ▲▼▲")
        print("   " + " ◄▼▼▼►")
        print("   " + "  ▼▼▼" + Style.RESET_ALL)
        print()
        print(Fore.BLUE + "3. FELIX" + Style.RESET_ALL + " (Fix-It Felix Jr.)")
        print("   " + Fore.BLUE + "  ┌─┐")
        print("   " + "  │■│")
        print("   " + "  └─┘" + Style.RESET_ALL)
        print()
        print(Fore.GREEN + "4. CALHOUN" + Style.RESET_ALL + " (Sergeant)")
        print("   " + Fore.GREEN + "  ╔═╗")
        print("   " + "  ╬═╣")
        print("   " + "  ╚═╝" + Style.RESET_ALL)
    






    def print_board(self):
        print("\n" + Fore.WHITE + Back.BLUE + " GAME BOARD " + Style.RESET_ALL + "\n")
        


        # board display
        board_display = []
        for i in range(self.board_size):
            if i == 0:
                board_display.append(Back.GREEN + " S " + Style.RESET_ALL)
            elif i == self.board_size - 1:
                board_display.append(Back.YELLOW + " F " + Style.RESET_ALL)
            elif i in self.special_spaces:
                special_type, color = self.special_spaces[i]
                board_display.append(color + " ◊ " + Style.RESET_ALL)
            else:
                board_display.append(" · ")
        


        # player positions
        for player in self.players:
            if 0 <= player['position'] < self.board_size:
                board_display[player['position']] = " " + self.get_player_ascii(player['character']) + " "
        




        # board
        for row in range(5):
            start = row * 10
            end = min(start + 10, self.board_size)
            print("".join(board_display[start:end]))
        


        # Legend
        print("\n" + Fore.YELLOW + "Legend: " + Style.RESET_ALL + 
              "S=Start, F=Finish, ◊=Special Space")
        



        # Player status
        print("\n" + Fore.WHITE + "Players:" + Style.RESET_ALL)
        for i, player in enumerate(self.players):
            status = f"{self.get_player_ascii(player['character'])} {player['name']}"
            if player['is_computer']:
                status += Fore.YELLOW + " [CPU]" + Style.RESET_ALL
            status += f" - Position: {player['position']}"
            if i == self.current_player:
                status = Fore.GREEN + "→ " + Style.RESET_ALL + status
            else:
                status = "  " + status
            print(status)
    



    def print_special_effect(self, effect_type):
        effects = {
            "glitch": (Fore.CYAN, """
            ╔════════════════╗
            ║ G░L░I░T░C░H░! ║
            ╚════════════════╝
            """),
            "wreck_it": (Fore.RED, """
            ╔═══════════════════╗
            ║ I'M GONNA WRECK IT║
            ╚═══════════════════╝
            """),
            "turbo": (Fore.YELLOW, """
            ╔═══════════════╗
            ║ TURBO-TASTIC! ║
            ╚═══════════════╝
            """),
            "fix_it": (Fore.BLUE, """
            ╔═══════════════╗
            ║ I CAN FIX IT! ║
            ╚═══════════════╝
            """),
            "cherry_bomb": (Fore.MAGENTA, """
            ╔═══════════════╗
            ║ CHERRY BOMB!  ║
            ╚═══════════════╝
            """),
            "sugar_rush": (Fore.GREEN, """
            ╔═══════════════╗
            ║  SUGAR RUSH!  ║
            ╚═══════════════╝
            """),
            "cy_bug": (Fore.RED + Back.BLACK, """
            ╔═══════════════╗
            ║ CY-BUG ATTACK ║
            ╚═══════════════╝
            """),
            "medal": (Fore.YELLOW + Style.BRIGHT, """
            ╔═══════════════╗
            ║ HERO'S MEDAL! ║
            ╚═══════════════╝
            """)
        }
        
        if effect_type in effects:
            color, ascii_art = effects[effect_type]
            print(color + ascii_art + Style.RESET_ALL)
    





    def execute_special_space(self, player, space_type):
        print(f"\n{player['name']} landed on a special space!")
        time.sleep(1)
        self.print_special_effect(space_type)
        time.sleep(1)
        
        if space_type == "glitch":
            jump = random.randint(1, 6)
            player['position'] += jump
            print(f"Vanellope's glitch power! Jump forward {jump} spaces!")
        
        elif space_type == "wreck_it":
            player['position'] = max(0, player['position'] - 3)
            print("Ralph wrecked it! Move back 3 spaces!")
        
        elif space_type == "turbo":
            player['turbo_next'] = True
            print("Turbo power activated! Double your next roll!")
        
        elif space_type == "fix_it":
            player['skip_penalty'] = True
            print("Felix's hammer protects you from the next penalty!")
        
        elif space_type == "cherry_bomb":
            for other in self.players:
                if other != player:
                    other['position'] = max(0, other['position'] - 2)
            print("Cherry bomb! Everyone else moves back 2 spaces!")
        
        elif space_type == "sugar_rush":
            player['position'] += 5
            print("Sugar Rush! Zoom forward 5 spaces!")
        
        elif space_type == "cy_bug":
            player['skip_turn'] = True
            print("Cy-Bug attack! Skip your next turn!")
        
        elif space_type == "medal":
            player['has_medal'] = True
            print("You earned a Hero's Medal! Immune to next penalty!")
        
        time.sleep(2)
    







    def roll_dice(self, show_animation=True):
        dice_art = [
            ["┌─────┐", "│     │", "│  ●  │", "│     │", "└─────┘"],  # 1
            ["┌─────┐", "│ ●   │", "│     │", "│   ● │", "└─────┘"],  # 2
            ["┌─────┐", "│ ●   │", "│  ●  │", "│   ● │", "└─────┘"],  # 3
            ["┌─────┐", "│ ● ● │", "│     │", "│ ● ● │", "└─────┘"],  # 4
            ["┌─────┐", "│ ● ● │", "│  ●  │", "│ ● ● │", "└─────┘"],  # 5
            ["┌─────┐", "│ ● ● │", "│ ● ● │", "│ ● ● │", "└─────┘"]   # 6
        ]
        
        if show_animation:
            # Cool animation effect
            for _ in range(5):
                self.clear_screen()
                self.print_logo()
                roll = random.randint(1, 6)
                print(Fore.YELLOW + "\nRolling..." + Style.RESET_ALL)
                for line in dice_art[roll-1]:
                    print("  " + line)
                time.sleep(0.2)
        else:
            roll = random.randint(1, 6)
        
        return roll
    





    def play_turn(self):
        player = self.players[self.current_player]
        
        print(f"\n{Fore.YELLOW}═══════════════════════════════")
        print(f"{player['name']}'s turn ({player['character']})")
        if player['is_computer']:
            print(Fore.YELLOW + "[COMPUTER PLAYER]" + Style.RESET_ALL)
        print(f"Current position: {player['position']}")
        print(f"═══════════════════════════════{Style.RESET_ALL}")
        
        # Check for skip turn
        if player.get('skip_turn', False):
            print(Fore.RED + "You're stunned by the Cy-Bug! Turn skipped!" + Style.RESET_ALL)
            player['skip_turn'] = False
            time.sleep(2)
            return
        
        if player['is_computer']:
            print("\nComputer is thinking...")
            time.sleep(1.5)
            roll = self.roll_dice(show_animation=False)
            print(f"Computer rolled: {roll}")
        else:
            input("\nPress Enter to roll the dice...")
            roll = self.roll_dice(show_animation=True)
        




        # Apply turbo if
        if player.get('turbo_next', False):
            roll *= 2
            print(Fore.YELLOW + f"TURBO POWER! Roll doubled to {roll}!" + Style.RESET_ALL)
            player['turbo_next'] = False
        
        player['position'] += roll
        


        # Check if player won
        if player['position'] >= self.board_size - 1:
            player['position'] = self.board_size - 1
            return True  # Player won!
        




        # special space
        if player['position'] in self.special_spaces:
            space_type, _ = self.special_spaces[player['position']]
            
            # Check immunity
            if player.get('has_medal', False) and space_type in ['wreck_it', 'cy_bug']:
                print(Fore.YELLOW + "Your Hero's Medal protects you!" + Style.RESET_ALL)
                player['has_medal'] = False
            elif player.get('skip_penalty', False) and space_type in ['wreck_it', 'cy_bug']:
                print(Fore.BLUE + "Felix's hammer protects you!" + Style.RESET_ALL)
                player['skip_penalty'] = False
            else:
                self.execute_special_space(player, space_type)
        
        return False
    
    def print_winner(self, player):
        self.clear_screen()
        print(Fore.YELLOW + Style.BRIGHT + """
        ╔═══════════════════════════════════╗
        ║                                   ║
        ║         🏆 WINNER! 🏆             ║
        ║                                   ║
        ╚═══════════════════════════════════╝
        """ + Style.RESET_ALL)
        
        winner_text = f"{player['name']} ({player['character']})"
        if player['is_computer']:
            winner_text += " [COMPUTER]"
        print(f"\n{Fore.GREEN}{winner_text} WINS!{Style.RESET_ALL}\n")
        
        if player['character'] == "Ralph":
            print(Fore.RED + """
            ╔═══════════════════════╗
            ║   "I'M BAD, AND       ║
            ║    THAT'S GOOD!"      ║
            ╚═══════════════════════╝
            """ + Style.RESET_ALL)
        elif player['character'] == "Vanellope":
            print(Fore.CYAN + """
            ╔═══════════════════════╗
            ║   "I'M A PRINCESS     ║
            ║     TOO, YA KNOW!"    ║
            ╚═══════════════════════╝
            """ + Style.RESET_ALL)
        elif player['character'] == "Felix":
            print(Fore.BLUE + """
            ╔═══════════════════════╗
            ║    "I CAN FIX IT!"    ║
            ╚═══════════════════════╝
            """ + Style.RESET_ALL)
        else:
            print(Fore.GREEN + """
            ╔═══════════════════════╗
            ║  "FEAR IS A FOUR-     ║
            ║   LETTER WORD!"       ║
            ╚═══════════════════════╝
            """ + Style.RESET_ALL)
        
        input("\nPress Enter to return to main menu...")
    
    def setup_game(self):
        self.clear_screen()
        self.print_logo()
        
        # Reset
        self.players = []
        self.current_player = 0
        
        # number of human players
        while True:
            try:
                num_humans = int(input("How many human players? (0-4): "))
                if 0 <= num_humans <= 4:
                    break
                print("Please enter a number between 0 and 4.")
            except ValueError:
                print("Please enter a valid number.")
        
        if num_humans == 0:
            print("\nStarting CPU-only game!")
            num_computers = 4
        else:
            # computer players
            max_computers = 4 - num_humans
            if max_computers > 0:
                while True:
                    try:
                        num_computers = int(input(f"How many computer players? (0-{max_computers}): "))
                        if 0 <= num_computers <= max_computers:
                            break
                        print(f"Please enter a number between 0 and {max_computers}.")
                    except ValueError:
                        print("Please enter a valid number.")
            else:
                num_computers = 0
        
        total_players = num_humans + num_computers
        if total_players < 2:
            print("\nNeed at least 2 players! Adding computer players...")
            num_computers = 2 - num_humans
            time.sleep(2)
        



        # Character selection
        characters = ["Ralph", "Vanellope", "Felix", "Calhoun"]
        available = characters.copy()
        


        #players choose characters
        for i in range(num_humans):
            self.clear_screen()
            self.print_logo()
            self.print_character_select()
            
            name = input(f"\nPlayer {i+1}, enter your name: ")
            
            while True:
                try:
                    choice = int(input("Choose your character (1-4): "))
                    if 1 <= choice <= 4 and characters[choice-1] in available:
                        character = characters[choice-1]
                        available.remove(character)
                        break
                    print("Invalid choice or character already taken.")
                except ValueError:
                    print("Please enter a valid number.")
            
            self.players.append({
                'name': name,
                'character': character,
                'position': 0,
                'is_computer': False
            })
        

        # Computer get random remaining characters
        cpu_names = ["CPU Ralph", "CPU Vanellope", "CPU Felix", "CPU Calhoun"]
        for i in range(num_computers):

            character = random.choice(available)
            available.remove(character)
            
            # characterCPU name
            for cpu_name in cpu_names:
                if character in cpu_name:
                    name = cpu_name
                    break
            
            self.players.append({
                'name': name,
                'character': character,
                'position': 0,
                'is_computer': True
            })
        
        # Random player order
        random.shuffle(self.players)
        
        print(f"\n{Fore.GREEN}Game starting with {len(self.players)} players!{Style.RESET_ALL}")
        time.sleep(2)
    
    def play(self):
        while True:
            self.print_main_menu()
            
            choice = input("\nEnter your choice (1-3): ")
            
            if choice == "1":

                self.setup_game()
                

                game_won = False
                while not game_won:
                    self.clear_screen()
                    self.print_logo()
                    self.print_board()
                    
                    game_won = self.play_turn()
                    
                    if game_won:
                        self.print_winner(self.players[self.current_player])
                        break
                    
                    self.current_player = (self.current_player + 1) % len(self.players)
                    
                    if not self.players[self.current_player]['is_computer']:
                        input("\nPress Enter to continue...")
                    else:
                        time.sleep(1)  # Brief pause
            


            elif choice == "2":
                self.print_instructions()
            

            elif choice == "3":
                self.clear_screen()
                print(Fore.YELLOW + """
                ╔═══════════════════════════════╗
                ║  THANKS FOR PLAYING!          ║
                ║  "THERE'S NO ONE I'D RATHER   ║
                ║   BE THAN ME!"                ║
                ╚═══════════════════════════════╝
                """ + Style.RESET_ALL)
                break
            
            else:
                print(Fore.RED + "Invalid choice! Please try again." + Style.RESET_ALL)
                time.sleep(1)



if __name__ == "__main__":
    game = WreckItRalphGame()
    game.play()




# OMG! I FIND MY CODING MOTTO! AAAAHHHHHHHHHHH! It's perfect!

# My name's Ralph, and I'm a bad guy. 
# Uh, let's see... I'm nine feet tall, 
# I weigh six hundred and forty-three pounds. 
# Got a bit of a temper on me.
# My passion bubbles very near the surface, 
# I guess, 
# not gonna lie. 
# Anyhoo, 
# what else? 
# Uh... I'm a wrecker. I wreck things, professionally. I mean, I'm very good at what I do. 
# Probably the best I know. 





# ...please don't sue me hasbro or disney