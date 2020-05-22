while(1):

    file = input("Enter correct filename: ")
    
    try:
    
        filecontent = open(file, 'r')
        content = filecontent.read()

    except IOError:						
    							
        print("\nFileNotFoundError: File is not found. Please check what you have entered. Try Again!\n")

    else:								
    									
        print("Succesfully read the file, '{}'\n".format(file))
        print("File content: {}\n".format(content))
        break
