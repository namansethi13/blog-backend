import uuid
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile

def compress_and_rename_image(image, new_name=None,partial_name=None, quality=85, max_width=1280, max_height=720):
    img = Image.open(image)
    img = img.convert("RGB") 

    img.thumbnail((min(img.width, max_width) , min( image.height , max_height)), Image.LANCZOS)

    base_name = new_name or partial_name + str(uuid.uuid4())
    final_name = f"{base_name}.jpg"

    buffer = BytesIO()
    img.save(buffer, format="JPEG", optimize=True, quality=quality)
    buffer.seek(0)

    return ContentFile(buffer.read(), name=final_name)
