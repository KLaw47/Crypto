def dynamo():
    # create keys
    keys = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 !@#$%^&*()_+-=[]{}|;:",./<>?\\'
# autogenerate values string
    values = keys[-1] + keys[0:-1]
    print(keys)
    # print(values)

# create dictionaries
    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys))

# or create 1 dict and flip
    dict_e = dict(zip(keys,values))
    dict_d = {value:key for key, value in dict_e.items()}
# user input 'message' and mode
    msg = input('Enter your secret message quietly: ')
    mode = input('Crypto mode: encode (e) OR decode (d): ')
# run encode or decode
    if mode.lower() == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg])
    elif mode.lower() == 'd':
        new_msg = ''.join([dict_d[letter] for letter in msg])
    return new_msg


# return res
print(dynamo())
