"""displays the users input with the correct aritcle"""
import argparse

def get_args()-> str:
    """using argparse to get the users word"""
    parser = argparse.ArgumentParser(description="Crow's Nest -- choose the correct article")
    parser.add_argument('name', help='enter a word')
    args = parser.parse_args()
    return args.name

def main() -> None:
    word = get_args()
    article = 'an' if word[0].lower() in ['a', 'e', 'i', 'o', 'u'] else 'a'
    print(f"Ahoy, Captain, {article} {word} off the larboard bow!")


if __name__ == '__main__':
    main()
