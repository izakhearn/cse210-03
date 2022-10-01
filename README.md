# cse210-03

## Jumper Game

The purpose of this repository is to keep the code for the Jumper game.

The code has the following object and classes

## Terminal Service Class

```python
Class       : terminal_service
File Name   : terminal_service.py

**Attributes**
promt : string
text : string
**Methods**
write_text()   : Prints text on screen
read_number()  : Return input as float
read_test()    : Return Input as string
```

-------

## Words Class

```python
Class       : WordList
File Name   : word.py

**Attributes**
    None

**Methods**
random_word() : Returns a random word from the list 
```

```python
Object      : self._list

**Responsibility**
To hold the card that is currently in play

**Behaviors**       **State**
 random_word        Gets a new random word from the list
```

-------

## Director Class

```python
Class            : Director
File Name        : director.py

**Attributes**
    None

**Methods**
start_game()     : None 
_get_inputs()     : None
_do_outputs()  : None
```

```python
Object      : Director

**Responsibility**
To hold an instance of the game running and print out the parachute and guessed words

**Behaviors**       **State**
 start_game         Starts running the game
```

-------

## Guess Draw Class

```python
Class            : Guess_Draw
File Name        : guess_draw.py

**Attributes**
    None

**Methods**
print_current_word() : Returns the words with correct letter guesses
draw_parachute()     : Prints the parachute 
_died()              : Check if the soldier died and returns a 
                        x if he died
_landed()            :  Check if all guesses are correct and 
                        returns the whole word
```

```python
Object      : _Guess_Draw

**Responsibility**
To hold an instance of Guess_Draw class

**Behaviors**        **State**
 print_current_word     Prints the current word with correctly 
                        guessed letters

 draw_parachute         Prints the soldier and parachute lines 
                        remaining
```

-------

## Author : Izak Hearn

## Email : izak@gmail.com
