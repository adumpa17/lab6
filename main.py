def encode(tempPassword):  # This is Abhiram Dumpa's code
    encryptedPassword = ""
    for i in range(0, len(tempPassword)):
        tempNum = int(tempPassword[i])
        tempNum += 3
        if tempNum > 9:
            tempNum -= 10
        encryptedPassword += str(tempNum)
    return encryptedPassword


def decode(password):
    new_password = ""
    for char in password:
        num = int(char)
        new_num = num - 3
        if new_num < 0:
            new_num = new_num + 10
        new_password += str(new_num)
    return new_password


if __name__ == "__main__":
    notDone = True
    while notDone:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = int(input("Please enter an option: "))

        if choice == 1:
            temp = input("Please enter your password to encode: ")
            newPass = encode(temp)
            print("Your password has been encoded and stored!")

        if choice == 2:
            tempDecode = decode(newPass)
            print(f"The encoded password is {newPass}, and the original password is {tempDecode}.")

        if choice == 3:
            break
