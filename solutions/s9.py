def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize//block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize%block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    
#     if condition:
#     return something
# else:
#     return something_else
    
    if partial_block_remainder > 0:
        return (full_blocks +1)*block_size
    
    # In Python, once the if condition runs and hits a return, the function immediately exits — it never reaches the next line.
    # means we can directly continue , instead of writing else 
    # note that it is a alternate for else , not for elif 
    return full_blocks*block_size
                                   
print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192