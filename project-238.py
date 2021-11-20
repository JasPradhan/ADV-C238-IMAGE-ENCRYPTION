import hashlib

filename="image_for_project_238.jpg"

with open(filename,'rb') as f:
	file_data=f.read()

image_hash=hashlib.sha256(file_data).hexdigest()

print(image_hash)