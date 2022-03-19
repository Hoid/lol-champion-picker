import argparse

__author__ = "Tyler Cheek"
__license__ = "MINE"


class Champion:

    name = ""
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Champion named {self.name}"
        

def main(args):
    """ Main entry point of the app """
    champions_selected_raw = args.champions_selected_str.split(',')
    champions_selected = [champion_name_str.lower() for champion_name_str in champions_selected_raw]
    for champion_name in champions_selected:
        champion = Champion(champion_name)
        print(champion)
    



if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Champions argument
    parser.add_argument("-c", "--champions-selected", dest="champions_selected_str", help="a comma-separated list of champion names; case insensitive, but spaces matter")

    args = parser.parse_args()
    main(args)