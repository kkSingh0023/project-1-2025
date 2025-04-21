def main():
    print("Welcome! Type something and press Enter (Ctrl+C to exit):")
    while True:
        try:
            user_input = input(">>> ")
            print(f"You typed: {user_input}")
        except KeyboardInterrupt:
            print("\nExiting... Goodbye!")
            break

if __name__ == "__main__":
    main()