"""Print the alphabet in lowercase, not followed by a new line."""
#!/usr/bin/python3
for letter in range (97, 123):
    print("{}".format(chr(letter)), end="")
