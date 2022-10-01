class Guess_Draw:
    """Displays the word to guess and the parachute. 
    
    The responsibility of Display is to check the guess against the word and update the display to reflect the changes. 
    
    Attributes:
        _word (List[char]): The word to be guessed.
        _length (int): Length of the word to be guessed.
        _guess (Boolean): Boolean if the guessed letter is in the give_word.
        _spaces (List[char]): The characters to be displayed.
        _string (string): The string to return to the director.
        _parachute (List[string]): Contains the parachute to be displayed.
        _index (List[int]): A list of all the indexes of characters to remove on the parachute.
    """

    def __init__(self):
        """Constructs a new Display.

        Args:
            self (Display): An instance of Display.
        """
        self._word = []
        self._length = 0
        self._guess = True
        self._spaces = []
        self._string = ""
        self._parachute = ["  ", "___", "\n", " ", "/", "___", "\\", "\n", " ", "\\", "   ", "/", "\n", "  ", "\\", " ", "/", "\n", "   ", "o", "\n  /|\\\n  / \\\n\n^^^^^^^"]
        self._index = [1, 4, 6, 5, 9, 11, 14, 16]
        self._parachute_string = ""
    
    def print_current_word(self, word, letter = ""):
        """ This method will build the word to guess

        The responsibility of display_word is to build the word using "_" where a letter has not been guessed
        It will then replace the "_" with the letter correctly guessed

        Parameters:
            self (Display):
            word (string): The word being guessed.
            letter (char): The letter being guessed.

        Returns:
            _string (string): the string built to display the word.
        """
        self._string = ""
        # This will only run once when the game starts
        if letter == "":
            self._length = len(word)
            for item in word:
                self._word.append(item)
            
            for x in range(self._length):
                self._spaces.append("_")
        # This will run every round after the first
        else:
            self._guess = False
            for item in self._word:
                if item == letter:
                    self._spaces[self._word.index(item)] = letter
                    self._guess = True

        # Prints the _ where no letters are guessed correct and then prints the letter when guess is correct
        for item in self._spaces:
            self._string += (item + " ")
        self._string += "\n"
        return self._string

    def draw_parachute(self):
        """ This method will build the parachute

        The responsibility of display_parachute is to build the parachute
        It will then replace the parts of the parachute with empty spaces " " when a guess is incorrect.
        Once the user runs out of guesses, it will return a false to change the state of the game.

        Parameters:
            self (Display):
        Returns:
            _parachute_string (string): the string built to display the parachute.
        """
        self._parachute_string = ""
        # If the guess from the user is correct we should not cut the parachute
        # But rather print the parachute as it was in the previous round
        if self._guess:
            for item in self._parachute:
                print(item, end="")
            return self._parachute_string
        # If the guess from the user is incorrect we should cut the parachute
        # and the print the new parachute after the cut
        else:
            if self._index[0] <= 16:
                self._parachute.pop(self._index[0])
                self._parachute.insert(self._index[0], " ")
                
            # If the parachute is cut all the way, the user has lost the game and the head of the man 
            # Will turn to an x
            if (self._index[0] == 16):
                self._parachute.pop(19)
                self._parachute.insert(19, "x")
            self._index.pop(0)

            for item in self._parachute:
                self._parachute_string += item
            self._parachute_string += "\n"            

            return self._parachute_string
        
    def _died(self):
        
        return (self._parachute[19] == "x")

    def _landed(self):

        return (self._word == self._spaces)