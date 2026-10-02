# Using Context Manager to open a file and write to it i.e using with statement in python

with open("test2.txt","w") as f:
    pass
    print(type(f)) # <_io.TextIOWrapper>
    f.write("Test")

    # same as seek 
    f.seek(0)
    f.write("R")


# COPYING TEXT FILE

# My Version
with open('test.txt','r') as rf:
    f_content = rf.readline()
    while len(f_content) > 0:
        with open('test_copy.txt','a') as wf:
            wf.writelines(f_content)
        f_content = rf.readline()

# Sir Version
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


# COPYING IMAGE FILES
with open('filename.jpg', 'rb') as rf:
    with open('filename_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)

# ADVANCED FILE OPERATION

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        chunk_size = 400
        rf_chunk =  rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)