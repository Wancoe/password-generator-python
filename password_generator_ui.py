import inquirer
from rich.console import Console
from rich.prompt import Prompt

class PasswordGeneratorUI:
    def __init__(self):
        self.console = Console()

    def display_welcome(self):
        self.console.print("[bold green]Welcome to the Password Generator![/bold green]")

    def get_password_length(self):
        questions = [
            inquirer.List('length', message="Choose password length:", choices=[8, 12, 16, 20],),
        ]
        answers = inquirer.prompt(questions)
        return answers['length']

    def display_password(self, password):
        self.console.print(f"[bold blue]Generated Password: {password}[/bold blue]")

    def run(self):
        self.display_welcome()
        length = self.get_password_length()
        password = "a1b2c3d4"  # Replace with actual password generation logic
        self.display_password(password)

if __name__ == '__main__':
    ui = PasswordGeneratorUI()
    ui.run()