import json
import random
from pathlib import Path


def print_hangman(remaining_count):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |    |
           |   / \\
          ---
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    |
           |   / 
          ---
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    |
           |    
          ---
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |    
          ---
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |    
          ---
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |    
          ---
        """,
        """
           ------
           |    |
           |    O
           |    
           |    
           |    
          ---
        """,
    ]
    print(stages[remaining_count])


def select_problem() -> str:
    # problems = json.loads(Path("elementary_school_words.json").read_text())
    problems = json.loads(Path("resources/middle_school_words.json").read_text())
    selected_problem = random.choice(problems)
    return selected_problem


class Word:
    def __init__(self, word: str):
        self.remaining_count = 6  # 시도 횟수
        self.word_ref = word.lower()  # 정답 단어
        self.word_current = ["_"] * len(word)  # 화면에 보이는 word
        self.tried_letters = []  # 시도한 알파벳들 저장
        self.print_welcome()
        self.print_status()

    def print_welcome(self):
        print("=" * 50)
        print(f"This word consists of {len(self.word_ref)} letters.")

    def print_status(self):
        print_hangman(self.remaining_count)
        print(f" - remaining count: {self.remaining_count}")
        print(f" - current word: {' '.join(self.word_current)}")
        print(f" - tried letters: {self.tried_letters}")

    def print_not_found(self):
        print(f"You got a wrong letter (ㅠㅠ).")

    def print_gameover(self):
        print(f"Game over (ㅠㅠ). The answer is '{self.word_ref}'")

    def print_congrat(self):
        print("Congraturations!!!!!!! You got the correct answer.")

    def is_valid_letter(self, letter: str):
        if not isinstance(letter, str) or len(letter) != 1:
            print("Please enter a single letter.")
            return False

        if letter.lower() in self.tried_letters:
            print(f"The letter '{letter.lower()}' has already been entered.")
            return False
            
        if letter.lower() not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a latin alphabet")
            return False
        
        return True

    def guess(self, letter: str):
        letter = letter.lower()
        found = False
        for i, c in enumerate(self.word_ref):
            if letter == c:
                self.word_current[i] = letter
                found = True

        if not found:
            self.remaining_count -= 1
            self.tried_letters.append(letter)

    def is_cleared(self):
        if "_" not in self.word_current:
            return True
        else:
            return False

    def run(self):
        while self.remaining_count > 0:
            print("=" * 50)
            user_input = input("Please enter a letter: ")
            letter = user_input
            print(f"You entered '{letter}'")
            if not self.is_valid_letter(letter):
                continue

            self.guess(letter)
            self.print_status()
            if self.is_cleared():
                self.print_congrat()
                break

        if self.remaining_count == 0:
            self.print_gameover()


if __name__ == "__main__":
    problem = select_problem()
    word = Word(problem)
    word.run()
