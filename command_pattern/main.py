from invoker import Invoker
from simple_command import SimpleCommand
from complex_command import ComplexCommand
from receiver import Receiver


if __name__ == '__main__':
    """
    The client code can parameterize an invoker with any commands.
    """
    simple_command = SimpleCommand('payload for simple_command')
    complex_command = ComplexCommand(Receiver(), 'a string', 'b string')

    invoker = Invoker()
    invoker.set_on_start(simple_command)
    invoker.set_on_finish(complex_command)
    invoker.do_something_important()
