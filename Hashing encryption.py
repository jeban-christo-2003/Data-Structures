import hashlib

def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()

def main():
    while True:
        choice = input("Choose an option:\n1. Hash text\n2. Exit\nYour choice: ")

        if choice == '1':
            text = input("Enter the text to hash: ")
            hashed_text = hash_text(text)
            print(f"Hashed text: {hashed_text}\n")
        elif choice == '2':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    main()
