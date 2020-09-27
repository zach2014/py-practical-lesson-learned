"""Print greeting message with the invoker
Usage:
    entry_point_with_args_cmd [--to=invoker-name]

"""
import docopt


def format_greeting(name):
    """greets to the provided person name"""
    greeting_msg_prefix = "Glad to exec me"
    print(greeting_msg_prefix,  ',' + name)


def main():
    args = docopt.docopt(__doc__)
    invoker = args['--to']
    if invoker:
        format_greeting(invoker)
    else:
        format_greeting('Anonymous')


if __name__ == '__main__':
    main()
