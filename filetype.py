# Python program to print the extension of the given file

#Entering the file name
file= input("Enter the filename: ")

# Splitting the file into two parts
split_file=file.split('.')

file_extension= split_file[1]

# Checking for file extension matches
if (file_extension== 'py'):
    print("Python")
    
if (file_extension== 'txt'):
    print("Text file")
    
if (file_extension== 'mp4'):
    print("MP4 File")
    
if (file_extension== 'jpg' or 'jpeg' or 'png'):
    print("Image File")
    
if(file_extension== 'pdf'):
    print("PDF File")