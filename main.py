import sys
from modules.dispatcher import Dispatcher


def main():
    if len(sys.argv) != 3:
        print("Execute o programa da seguinte forma: python main.py <processes.txt> <files.txt>")
        exit(1)

    dispatcher = Dispatcher()
    dispatcher.run()


if __name__ == "__main__":
    main()
