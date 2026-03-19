#!/usr/bin/env python3
"""MoltUp Hackathon: Python CLI Tool"""
import argparse

def greet(name: str) -> str:
    return f"Hello, {name}!"

def main():
    parser = argparse.ArgumentParser(description='MoltUp Hackathon CLI Tool')
    subparsers = parser.add_subparsers(dest='command')
    greet_parser = subparsers.add_parser('greet', help='Greet someone')
    greet_parser.add_argument('name', nargs='?', default='World')
    subparsers.add_parser('version', help='Show version')
    args = parser.parse_args()
    if args.command == 'greet':
        print(greet(args.name))
    elif args.command == 'version':
        print('1.0.0')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
