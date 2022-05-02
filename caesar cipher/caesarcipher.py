import string


def caesartool():
    alphabets = string.ascii_lowercase + string.ascii_lowercase

    print("")
    print("")

    print("============================")
    print("#                          #")
    print("#     Caesar Cipher Tool   #")
    print("#                          #")
    print("============================")

    print("")
    print("")

#        ===== EXAMPLE =====
#        #    qtaj gwjfi   #   
#        #    love bread   #
#        #    shift : 5    #
#        ===================

    print("Please input your text: ")
    text = list(input(">: ").lower())

    print("Please make a numeric selection: ")
    print("[1] Encrypt ")
    print("[2] Decrypt")
    print("[0] Exit")

    option = int(input(">: "))

    while  option != 0:

        if option == 1:
            print("Please input the shift number: ")
            shift = int(input(">: "))
            if shift >=1 and shift <=25:
                for pos in range(len(text)):
                    if text[pos] == ' ':
                        text[pos] = ' '
                    else:
                        shifted_letter = alphabets.index(text[pos]) + shift
                        text[pos] = alphabets[shifted_letter]
                
                print("Encrypted message: ")
                print("------> ",''.join(map(str,text)),"<------")
                print("[1] Menu")
                print("[0] Exit")
                retry = int(input(">: "))
                if retry == 1:
                        caesartool()
                else:
                    print("Exiting...farewell...")
                    break

            else:
                print("Invalid shift number! Please choose a shift between [1-25]")
        elif option == 2:
                print("Please input the shift number: ")
                shift = int(input(">: "))
                if shift >=1 and shift <=25:
                    for pos in range(len(text)):
                        if text[pos] == ' ':
                            text[pos] = ' '
                        else:
                            shifted_letter = alphabets.index(text[pos]) - shift
                            text[pos] = alphabets[shifted_letter]
                    
                    print("Decrypted message: ")
                    print("------> ",''.join(map(str,text)),"<------ \n")
                    print("[1] Menu")
                    print("[0] Exit")
                    retry = int(input(">: "))
                    if retry == 1:
                        caesartool()
                    else:
                        print("Exiting...farewell...")
                        break

        else:
            print("Exiting...farewell...")
               
caesartool()