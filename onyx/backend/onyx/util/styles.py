from qrcode.image.styles.colormasks import SolidFillColorMask
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer, SquareModuleDrawer, CircleModuleDrawer, \
    RoundedModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer

qr_styles = dict(
    square=SquareModuleDrawer(),
    gaped=GappedSquareModuleDrawer(),
    circle=CircleModuleDrawer(),
    round=RoundedModuleDrawer(),
    vertical=VerticalBarsDrawer(),
    horizontal=HorizontalBarsDrawer()
)

qr_color_styles = dict(
    solid=SolidFillColorMask
)

qr_default_style = dict(
    qr_code_style='square',
    qr_color_style='solid',
    qr_border_size=4,
    qr_size=1,
    qr_code_color=dict(
        red=255,
        green=255,
        blue=255
    ),
    qr_background_color=dict(
        red=0,
        green=0,
        blue=0
    )
)