import uuid
import random
import string

value = uuid.uuid4()
print(str(value))

charset = string.ascii_uppercase + string.digits
print(charset * 4)
print(''.join(random.sample(charset, 4)))
