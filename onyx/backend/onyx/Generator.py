import base64
from io import BytesIO

import qrcode


def generate_code(payload):
    buffered = BytesIO()
    qr = qrcode.make(payload)
    qr.save(buffered, format='JPEG')

    img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return {
        'image': f"data:image/jpeg;base64,{img_base64}",
        'type': "image/jpeg;base64",
        'content': payload
    }


if __name__ == "__main__":
    print(generate_code("Hello there"))
