# Pickling, Unpickling 

import pickle

# dump(): Used for serialization/pickling
# pickle.dump(object, fileobject)


# load(): Used for deserialization/unpickling
# pickle.load(object, fileobject)

lst = ['a', 'b', 'c', 'd', 'e']
fh = open('dummy.txt', 'wb')
pickle.dump(lst, fh)

fh.close()

fh = open('dummy.txt', 'rb')
data = pickle.load(fh)
print(data)