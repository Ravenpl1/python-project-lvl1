from brain_games.cli import welcome_user

def main():
    print("Hello, %s!" % name)

name = welcome_user()

if __name__ == '__main__':
    main()