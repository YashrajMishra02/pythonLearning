# How does the for loop are suppose to work
nums = [1,2,3]

# when we create a for loop this is how the for loop work
# it create an iterator
i_nums = iter(nums)

while True:
    # run the code until it hits the StopIteration error i.e. until no value is left 
    try:
        # where next item get's you the next item of iterator
        item = next(i_nums)
        print(item)
    except StopIteration:
        break
