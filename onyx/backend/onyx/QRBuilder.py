import base64
import logging
import os
from io import BytesIO

import qrcode
from qrcode.image.styledpil import StyledPilImage

from onyx.util.styles import qr_default_style, qr_styles, qr_color_styles
from onyx.util.StructMessage import StructMessage
from onyx.util.StorageEntity import StorageEntity


def build_response(payload, persistent=False, mime='plain/text', style=None):
    if style is None:
        logging.debug(StructMessage(message='Missing style information, using default style.'))
        style = qr_default_style

    if style is not None:

        # check for missing qr_code_style
        if style.get('qr_code_style') is None:
            logging.debug(StructMessage(message='Missing "qr_code_style", using default.',
                                        default=qr_default_style['qr_code_style']))

            style['qr_code_style'] = qr_default_style['qr_code_style']

        # check for missing qr_border_size
        if style.get('qr_border_size') is None:
            logging.debug(StructMessage(message='Missing "qr_border_size", using default.',
                                        default=qr_default_style['qr_border_size']))

            style['qr_border_size'] = qr_default_style['qr_border_size']

        # check for missing qr_code_color
        if style.get('qr_code_color') is None:
            logging.debug(StructMessage(message='Missing "qr_back_color", using default.',
                                        default=qr_default_style['qr_code_color']))

            style['qr_code_color'] = qr_default_style['qr_code_color']

        # check for missing qr_background_color
        if style.get('qr_background_color') is None:
            logging.debug(StructMessage(message='Missing "qr_background_color", using default.',
                                        default=qr_default_style['qr_background_color']))

            style['qr_background_color'] = qr_default_style['qr_background_color']

        # check for missing qr_size
        if style.get('qr_size') is None:
            logging.debug(StructMessage(message='Missing "qr_size", using default.',
                                        default=qr_default_style['qr_size']))

            style['qr_size'] = qr_default_style['qr_size']

    # when enabled and flag is set persist payload
    if persistent and bool(os.getenv('ONYX_ENABLE_REDIS', False)):
        hashed = hash(payload).__str__()
        logging.debug(StructMessage(message='Hashed payload', payload=payload, hash=hashed))
        if not StorageEntity.save(hashed, {'data': payload, 'mime_type': mime}):
            return {
                'status': 'failure',
                'payload': 'Unable to persist payload'
            }

        payload = f"{os.getenv('ONYX_HOSTNAME', 'http://localhost')}/api/persistence/{hashed}"

    buffered = BytesIO()
    qr = qrcode.QRCode(version=style['qr_size'], border=style['qr_border_size'])
    qr.add_data(payload)

    fill_color = (style['qr_code_color']['red'], style['qr_code_color']['green'], style['qr_code_color']['blue'])
    back_color = (style['qr_background_color']['red'], style['qr_background_color']['green'],
                  style['qr_background_color']['blue'])

    logging.debug(StructMessage(message='Building qr code.', style=style))
    image = qr.make_image(format='PNG', image_factory=StyledPilImage,
                          module_drawer=qr_styles.get(style['qr_code_style']),
                          color_mask=qr_color_styles.get('solid')(front_color=fill_color, back_color=back_color))

    image.save(buffered, format='PNG')

    img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return {
        'status': 'success',
        'image': f"data:image/png;base64,{img_base64}",
        'payload': payload
    }


if __name__ == "__main__":
    print(build_response("Hello there", qr_default_style))
