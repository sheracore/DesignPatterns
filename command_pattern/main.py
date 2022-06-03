from invoker import Invoker
from simple_command import SimpleCommand
from complex_command import ComplexCommand


if __name__ == '__main__':
    """
    The client code can parameterize an invoker with any commands.
    """
    simple_command = SimpleCommand()
    complex_command = ComplexCommand()

    invoker = Invoker()
    invoker.set_on_start(simple_command)
    invoker.set_on_finish(complex_command)
