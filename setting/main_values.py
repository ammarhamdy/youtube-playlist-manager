from os import getcwd
from os.path import join
from tkinter.font import Font

# app title
window_title = "playlist manager"


# window icon
def get_icon_path():
    return join(
        getcwd(),
        join("view", join("icon", "black_youtube.ico"))
    )


def get_past_img_path():
    return join(
        getcwd(),
        join("view", join("image", "clipboard.png"))
    )


# window size
def get_screen_size(tk_obj):
    # return 750, 500
    return tk_obj.winfo_screenwidth(), tk_obj.winfo_screenheight()


# window position.
window_x = 0
window_y = 0

# button
button_width = 24
button_height = 24
button_font_size = 15

# padding
window_pad_x = 15
window_pad_y = 10
main_frame_pad_y = 5
default_pad_y = 10
# list view spacing.
list_view_pad_x = 10
list_y_gap = 5

# font.
header_font = ("Arial", 16, "bold")
default_font = ("Arial", 16)


def get_dfault_font(window):
    return Font(window, family=header_font[0], size=header_font[1], weight=header_font[2])


# header size.
header_widths = None
header_width_pxs = None


def calculate_header_widths(window):
    global header_widths, header_width_pxs
    """
    headers size must be in this percentage:
    15% ,35%, 10%, 10%, 10%, 10%, 10%  from the total frame width
    """
    frame_width = window.winfo_screenwidth() - window_pad_x * 2
    # average of letter width in px: largest letter width + the smallest letter width / 2
    font = get_dfault_font(window)
    factor = (font.measure("i") + font.measure("m")) / 2
    # header width in pixels.
    header_width_pxs = (
        frame_width * 15 / 100,  # id
        frame_width * 35 / 100,  # title
        frame_width * 10 / 100,  # date
        frame_width * 10 / 100,  # view
        frame_width * 10 / 100,  # like
        frame_width * 10 / 100,  # comment
        frame_width * 10 / 100,  # duration
    )
    # header width in chars (how many chars it takes)
    header_widths = (
        int(header_width_pxs[0] / factor),  # id
        int(header_width_pxs[1] / factor),  # title
        int(header_width_pxs[2] / factor),  # date
        int(header_width_pxs[3] / factor),  # view
        int(header_width_pxs[4] / factor),  # like
        int(header_width_pxs[5] / factor),  # comment
        int(header_width_pxs[6] / factor)  # duration
    )
