def bar(x):
    print(x + 2)

# Only run this when run from the command line,
# but not when imported

if __name__ == "__main__":
    print("I am running from the command line.")

elif __name__ == "foo":
    print("I am being imported!")