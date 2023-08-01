import io
import pickle
from datetime import datetime

from google.cloud import storage


bucket_name = "ptx-hotoku-work"
obj_name = "temp/storage-object-name" + datetime.now().strftime("%Y%m%d%H%M%S")


value = {
    "int": 123,
    "str": "abc"
}


client = storage.Client()
bucket = client.get_bucket(bucket_name)
blob = bucket.blob(obj_name)

bio = io.BytesIO()
pickle.dump(value, bio)
blob.upload_from_string(bio.getvalue())


bucket.copy_blob(blob, bucket, obj_name + "-2")
blob2 = bucket.blob(obj_name + "-2")
bs = blob2.download_as_bytes()
bio2 = io.BytesIO(bs)
value2 = pickle.load(bio2)
print(value2)
