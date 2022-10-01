from game.terminal_service import TerminalService
from game.word import WordList
from game.guess_draw import Guess_Draw

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        Guess_Draw (Guess_Draw): The Guess_Draw of the jumper.
        is_playing (boolean): Whether or not to keep playing.
        word (List): the word from a list of words.
        terminal_service: For getting and Guess_Drawing information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._Guess_Draw = Guess_Draw()
        self._is_playing = True
        self._terminal_service = TerminalService()
        self.letter_guess = ""
        self._list = WordList()
        self.random_word = self._list.random_word()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

        self._terminal_service.write_text(self._Guess_Draw.print_current_word(str(self.random_word)))
        
        self._terminal_service.write_text(self._Guess_Draw.draw_parachute())

        while self._is_playing:
            self._get_inputs()
            self._do_outputs()

    def _get_inputs(self):
        """Moves the seeker to a new location.
        Args:
            self (Director): An instance of Director.
        """
        self.letter_guess = self._terminal_service.read_text("\nGuess a letter: ")
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.
        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.write_text(self._Guess_Draw.print_current_word(self.random_word, self.letter_guess))
        self._terminal_service.write_text(self._Guess_Draw.draw_parachute())
        if self._Guess_Draw._died():
            self._is_playing = False
            self._terminal_service.write_text("Your soldier has fallen!")
        if self._Guess_Draw._landed():
            self._terminal_service.write_text("You brought your soldier down safely!")
            self._is_playing = False