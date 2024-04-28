import firebase_admin
from firebase_admin import credentials, storage
import datetime

cred = credentials.Certificate("./service.json")
firebase_admin.initialize_app(cred, { 'storageBucket' : 'ndvi-rpi.appspot.com' })

image = "color_mapped_image.png"
bucket = storage.bucket()
blob = bucket.blob("color_mapped_image.png")
blob.upload_from_filename(image)

blob.make_public()

print(blob.public_url)
