from tkinter.ttk import Frame, Label
from tkinter import LEFT, RIGHT, W
from setting import main_values
from setting.main_values import default_font, list_view_pad_x


class VideoView(Frame):
    def __init__(self, parent_layout, information):
        super().__init__(parent_layout, padding=list_view_pad_x, borderwidth=0)
        self.index = -1
        video_id, title, date, views, likes, comments, duration = information
        self.widths = main_values.header_widths  # widths in letters.
        self.widths_in_px = main_values.header_width_pxs
        # add_items_view:
        # the video id.
        self.get_item_view(self, video_id).pack(side=LEFT)
        # the video title.
        self.get_item_view(self, title).pack(side=LEFT)
        # the video duration count.
        self.get_item_view(self, duration).pack(side=RIGHT)
        # the video comment count.
        self.get_item_view(self, comments).pack(side=RIGHT)
        # the video likes count.
        self.get_item_view(self, likes).pack(side=RIGHT)
        # the video views count.
        self.get_item_view(self, views).pack(side=RIGHT)
        # the video date.
        self.get_item_view(self, date).pack(side=RIGHT)

    def get_item_view(self, parent_layout, text):
        self.index += 1
        return Label(
            parent_layout,
            text=text,
            anchor=W,
            font=default_font,
            width=self.widths[self.index],
            wraplength=self.widths_in_px[self.index]
        )
