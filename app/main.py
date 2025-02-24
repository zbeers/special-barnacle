import sys

def main():
    #writes $ to prompt user input
    sys.stdout.write('$ ')
    
    command = input()
    print(f"{command}: command not found\n")
    main() #makes main recursive

if __name__ == '__main__':
    main()