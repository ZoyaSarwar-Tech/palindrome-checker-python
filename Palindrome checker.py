print("WELCOME TO PALINDROME CHECKER")

def simple_palindrome(text):
    text = text.lower().strip()
    return text == text[::-1]

def advanced_palindrome(text):
    text = text.lower().strip()
    cleaned_text=""
    for char in text:
        if char.isalpha():
         cleaned_text+=char
    return text==cleaned_text[::-1]


def find_palindrome_in_sentence(sentence):
    words = sentence.split()

    palindrome=[]
    for word in words:
        cleaned_word="".join(c.lower() for c in word if c.isalpha())
        if cleaned_word==cleaned_word[ ::-1]:
            palindrome.append(word)
    return palindrome



def palindrome_checker_menu():



    while True:
        print("\nMenu")
        print("1. Simple Palindrome")
        print("2. Advanced Palindrome")
        print("3. Find Palindrome in sentence")
        print("4. Exit")
        choice=int(input("Enter your choice(1-4):"))
        if choice==1:
            text=input("Enter text to check:")
            if simple_palindrome(text):
                print(f"{text} is a palindrome")
            else:
                print(f"{text} is not a palindrome")

        elif choice==2:
            text=input("Enter text to check:")
            if advanced_palindrome(text):
                print(f"{text} is a palindrome")
            else:
                print(f"{text} is not a palindrome")

        elif choice==3:
            sentence=input("Enter sentence to check:")
            palindrome=find_palindrome_in_sentence(sentence)
            if palindrome:
                print(f"palindrome found in sentence: {palindrome}")
            else:
                print(f"no palindrome found in sentence: {palindrome}")


        elif choice==4:
            print("Thank you for using Palindrome Checker")
            break
        else:
            print("Invalid choice")
palindrome_checker_menu()












