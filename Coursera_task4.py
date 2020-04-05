def penguin(num):
    head = "   _~_    "      
    eyes = "  (o o)   "    
    nose = " /  V  \\  "
    stomach = "/(  _  )\\ "
    foot = "  ^^ ^^   "
    for i in range(num):
        print(head, end='')
    print()
    for i in range(num):
        print(eyes, end='')
    print()
    for i in range(num):
        print(nose, end='')
    print()
    for i in range(num):
        print(stomach, end='')
    print()
    for i in range(num):
        print(foot, end='')
    print()

def main():
    num = int(input())
    penguin(num)

if __name__ == "__main__":
    main()
   