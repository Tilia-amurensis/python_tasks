import cmd
import logging 
import turtle

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

class MyShell(cmd.Cmd):
    intro = 'Welcome to the my! shell.   Type help or ? to list commands.\n'
    prompt = '$'

    def __init__(self):
        super().__init__()
        self.__t=turtle.Pen()

    def do_forward(self, arg):
        arg_list = arg.split()
        if len(arg_list) > 0:
            step = int(arg_list[0])
            self.__t.forward(step)

    def do_backward(self, arg):
        arg_list = arg.split()
        if len(arg_list) > 0:
            step = int(arg_list[0])
            self.__t.backward(step)

    def do_left(self, arg):
        arg_list = arg.split()
        if len(arg_list) > 0:
            step = int(arg_list[0])
            self.__t.left(step)

    def do_right(self, arg):
        arg_list = arg.split()
        if len(arg_list) > 0:
            step = int(arg_list[0])
            self.__t.right(step)
            
    def do_reset(self, arg):
        self.__t.reset()

    def do_up(self, arg):
        self.__t.up()

    def do_down(self, arg):
        self.__t.down()

    def do_exit(self, arg):
        'exit: stop doing and exit...'
        log.debug("Thank you for using my! shell")
        return True

if __name__ == '__main__':
    try:
        MyShell().cmdloop()
    except KeyboardInterrupt:
        log.error("Key")
    except Exception as e:
        log.error("Error occurred: {}".format(e))