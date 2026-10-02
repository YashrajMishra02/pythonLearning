# Generate multiplication tables for numbers 2 to 20 along with creating a file for each table

for i in range(2,21):
    with open(f"table{i}.txt",'w') as f:
        for j in range(1,11):
            f.write(f"{i} x {j} = {i * j}\n")

