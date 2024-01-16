# cli.py
import argparse
from LeanDesk.LeanDesk import LeanDesk

def main():
    parser = argparse.ArgumentParser(description='Clean a directory.')
    parser.add_argument('directory_path', help='Path to the directory to be cleaned')
    
    args = parser.parse_args()
    
    cleaning = LeanDesk()
    cleaning.cleaning_dir(path=args.directory_path)
    print(f'Directory {args.directory_path} cleaned successfully.')

if __name__ == '__main__':
    main()
