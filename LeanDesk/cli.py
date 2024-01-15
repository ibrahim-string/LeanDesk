# cli.py
import argparse
from LeanDesk.LeanDesk import leandesk

def main():
    parser = argparse.ArgumentParser(description='Clean a directory.')
    parser.add_argument('directory_path', help='Path to the directory to be cleaned')
    
    args = parser.parse_args()
    

    leandesk.cleaning_dir(args.directory_path)
    print(f'Directory {args.directory_path} cleaned successfully.')

if __name__ == '__main__':
    main()
