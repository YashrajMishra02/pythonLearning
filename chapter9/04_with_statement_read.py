# Using Context Manager to open a file and read to it i.e using with statement in python

   
with open("test.txt","r") as f:
    
    f_content = f.read() # Read the entire file but can cause the memory error if the file is too large

    f_content = f.readlines() # This method reads the entire file and returns a list of lines in the file

    f_content = f.readline() # This method reads a single line from the file and returns it as a string and if used multiple time it will read the next line from the file
    print(f_content) 

    # ITERATION IN FILE
    # iteration help 
    for line in f:
        print(line, end='')
    print(type(line)) # <class 'str'> is created because the file is read line by line and each line is a string

    # READING CHUNKS AND SEEK
    f_content = f.read(100) # by defining the size as argument in the read() method
    print(f_content)

    # READING CHUNKS AND SEEK USING ITERATION 
    size_to_read = 10
    f_content = f.read(size_to_read)
    while len(f_content) > 0:
        print(f_content, end='*')
        f_content = f.read(size_to_read)


    # FILE POSITION MANIPULATION 
    # NOTE : If use a varable to declare the size then it show the correct stream position 
    size_to_read = 10
    f_content = f.read(size_to_read)
    print(f.tell())

    # NOTE: But if use directly the value then the position differ by 3 i.e. if 100 then 103 will be the output
    f_content = f.read(10)
    print(f.tell())

    size_to_read = 10
    f_content = f.read(size_to_read)
    print(f_content,end='')

    f.seek(0) # seek() method is used to manipulate the current postion in file & use to change at any position you

    f_content = f.read(size_to_read)
    print(f_content)


    