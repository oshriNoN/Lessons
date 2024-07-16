import cmd

import typer
from sys import exit
from click.exceptions import UsageError

a = 2

class MyCLI(cmd.Cmd):
    prompt = '>>> '  # Change the prompt text
    intro = 'Welcome to MyCLI. Type "help" for available commands.'  # intro message

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)
        self.a = 2
    
    def do_hello(self, line):
        """Print a greeting."""
        print("Hello, World!")

    def do_quit(self, line):
        """Exit the CLI."""
        return True
    
    def do_something(self, line):
        """something command """
        self.a = 3

    def do_print(self, line):
        """print command """
        print(self.a)

    def do_error(self, line):
        """error command """
        raise Exception("error")

##====================================================================##
# typer is a library that allows you to build CLI applications in Python. 
# It is based on the cmd module and provides a simpler interface for building command-line applications.
app = typer.Typer()

@app.command()
def hello(name):
    print(f"hello {name}")

@app.command()
def goodbye():
    print("sdsd")


if __name__ == '__main__':
        
    try:
        app()
        # MyCLI().cmdloop()
    except KeyboardInterrupt:
        exit("\nInterrupted by user, exiting...")

