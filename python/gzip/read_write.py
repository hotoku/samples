import gzip
from io import BytesIO
import pickle

obj = dict(x="1", y=1)
bio = BytesIO()
pickle.dump(obj, bio)
gzipfile = gzip.compress(bio.getvalue())

bio2 = BytesIO(gzip.decompress(gzipfile))
ret = pickle.load(bio2)
print(ret)
