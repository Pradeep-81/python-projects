email = input("Enter email id:")  # g@g.in
space, capital_letter, special_character = 0, 0, 0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                if (email[-4] == "." and email[-5] == "@") ^ (email[-3] == "." and email[-4] == "@"):
                    print("Expected Domain name.")
                else:
                    for i in email:
                        if i.isspace():
                            space = 1
                        elif i.isalpha():
                            if i == i.isupper():
                                capital_letter = 1
                        elif i.isdigit():
                            continue
                        elif i == "." or i == "_" or i == '@':
                            continue
                        else:
                            special_character = 1
                    if space == 1:
                        print("Email cannot contain spaces.")
                    elif capital_letter == 1:
                        print("Email cannot contain capital letters.")
                    elif special_character == 1:
                        print("Email cannot contain special characters.")
                    else:
                        print("Valid email Id.")
            else:
                print("Invalid Extension in email.")
        else:
            print("Email cannot contain more than one @ symbol.")
    else:
        print("Email cannot start with a Digit or any special characters.")
else:
    print("Invalid Email.length of Email cannot be less than 6.")
