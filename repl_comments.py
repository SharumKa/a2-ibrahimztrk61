from hashlib import sha256

comments = []

#Code below borrowed from https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py
def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()


password_hash = "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"

comment = input("Enter your comment: ")

while comment:
    pw1 = create_hash(input("Enter your password: "))
    pw2 = create_hash(input("Enter your password again: "))
    if pw1 == pw2:
        print('Those were the same passwords')
        comments.append(comment)
        print("Previously entered comments: ")
        for i, comment in enumerate(comments, 1):
            print(str(i) + '. ' + comment)
    else:
        print('Those were different passwords')
    comment = input("Enter your comment: ")
