from tkinter import Tk, LEFT, ttk, CENTER, TOP, RIGHT, W, VERTICAL, Canvas, BOTTOM
from tkinter.ttk import Button, Entry, Frame, Label, Scrollbar
from setting.main_values import *
from setting import main_values
from setting.colors import *


class MainView:
    def __init__(self):
        self.window = Tk()
        self.init_window()
        calculate_header_widths(self.window)
        create_styles()
        self.init_widget()
        self.add_widget()

    def init_window(self):
        self.window.title(window_title)
        #width, height = get_screen_size(self.window)
        #self.window.geometry(f"{width}x{height}+{window_x}+{window_y}")
        self.window.config(background=WHITE, borderwidth=0, padx=window_pad_x, pady=window_pad_y)
        self.window.iconbitmap(get_icon_path())

    def init_widget(self):
        self.top_frame = get_top_frame(self.window)
        self.url_frame, self.past_button, self.url_entry = get_url_frame(self.top_frame)
        self.search_frame, self.search_entry = get_search_frame(self.top_frame)
        # message frame
        self.message_frame,\
        self.message_label,\
        self.message_button\
            = get_message_frame(self.window)
        # the frame which contains headers and videos frame.
        self.main_frame = get_main_frame(self.window)
        # headers (id, title, data, view, like, comment, duration).
        self.header_frame,\
        self.id_label,\
        self.title_label,\
        self.date_label,\
        self.views_label,\
        self.likes_label,\
        self.comments_label,\
        self.duration_label\
            = get_header_frame(self.main_frame)
        # frame contains videos items.
        self.videos_list_container_frame,\
        self.videos_list_frame\
            = get_video_items_frames(self.main_frame)
        # statistics frame
        self.statistics_frame,\
        self.count_label,\
        self.total_views_label,\
        self.total_likes_label,\
        self.total_comments_label,\
        self.total_duration_label\
            = get_statistics_frame(self.window)

    def add_widget(self):
        self.top_frame.pack(fill="x", anchor=CENTER, side=TOP)
        # URL layout.
        # left side.
        self.url_frame.pack(side=LEFT)
        self.past_button.pack(side=LEFT, padx=10)
        self.url_entry.pack(side=LEFT)
        # right side.
        self.search_frame.pack(side=RIGHT, padx=10, pady=default_pad_y)
        self.search_entry.pack(side=RIGHT)
        # message section.
        self.message_button.pack(side=RIGHT)
        self.message_label.pack(fill="x")
        # list view frame.
        self.main_frame.pack(fill="both", anchor="center", expand=1, pady=main_frame_pad_y)
        # headers.
        self.header_frame.pack(fill="x") # , pady=default_pad_y
        self.id_label.pack(side=LEFT)
        self.title_label.pack(side=LEFT)
        self.duration_label.pack(side=RIGHT)
        self.comments_label.pack(side=RIGHT)
        self.likes_label.pack(side=RIGHT)
        self.views_label.pack(side=RIGHT)
        self.date_label.pack(side=RIGHT)
        # videos views frame.
        self.videos_list_container_frame.pack(fill="both", expand=1, pady=default_pad_y)
        # statistics frame
        self.statistics_frame.pack(fill="x", anchor=CENTER, side=BOTTOM)
        self.count_label.pack(side=LEFT)
        self.total_duration_label.pack(side=RIGHT)
        self.total_comments_label.pack(side=RIGHT)
        self.total_likes_label.pack(side=RIGHT)
        self.total_views_label.pack(side=RIGHT)

    def add_video_view(self, video_view):
        video_view.pack(fill="x", pady=list_y_gap)

    def set_statistics_labels(self, analyzer):
        self.count_label.config(text="total: " + str(analyzer.count))
        self.total_views_label.config(text="views: " + str(analyzer.total_views))
        self.total_likes_label.config(text="likes: " + str(analyzer.total_likes))
        self.total_comments_label.config(text="comments: " + str(analyzer.total_comment))
        self.total_duration_label.config(text="durations: " + analyzer.get_total_duration())

    def disable_all_action_views(self):
        self.search_entry.config(state="disable")
        self.url_entry.config(state="disable")
        self.past_button.config(state="disable")

    def enable_all_action_views(self):
        self.search_entry.config(state="enable")
        self.url_entry.config(state="enable")
        self.past_button.config(state="enable")

    def show(self):
        self.window.mainloop()

    def add_message_frame(self, message="", color=RED):
        self.message_label.configure(text=message, foreground=color)
        self.message_frame.pack(after=self.top_frame, fill="x", pady=5)

    def remove_message_frame(self):
        self.message_frame.pack_forget()

    def close(self):
        self.window.destroy()


def create_styles():
    style = ttk.Style()
    # white style (ws)
    style.configure(
        "ws.TFrame",
        background=WHITE
    )
    style.configure(
        "grays.TFrame",
        background=LIGHT_GRAY
    )
    style.configure(
        "grays.TButton",
        background=LIGHT_GRAY
    )
    # black background style.
    # style.configure(
    #     "bs.TFrame",
    #     background=BLACK
    # )
    # red background style.
    # style.configure(
    #     "rs.TFrame",
    #     background=RED
    # )


def get_top_frame(parent_layout):
    return Frame(parent_layout)


def get_url_frame(parent_layout):
    frame = Frame(parent_layout)
    past_button = Button(frame, text="past", width=8)
    url_entry = Entry(
        frame,
        justify=LEFT,
        font=("", button_font_size),
        width=100
    )
    return frame, past_button, url_entry


def get_search_frame(parent_layout):
    frame = Frame(parent_layout)
    search_entry = Entry(
        frame,
        justify=LEFT,
        font=("", button_font_size),
        width=20
    )
    return frame, search_entry


def get_message_frame(parent_layout):
    frame = Frame(parent_layout, padding=0, borderwidth=0)
    label = Label(frame, padding=4, foreground=RED, anchor=CENTER)
    button = Button(frame, text="X", width=3)
    return frame, label, button


def get_main_frame(parent_layout):
    return Frame(
        parent_layout,
        padding=0,
        borderwidth=0,
        style="ws.TFrame"
    )


def get_header_label(frame, text, width=0):
    return Label(
        frame,
        text=text,
        font=header_font,
        width=width,
        anchor=W,
        # underline=0
    )


def get_header_frame(parent_layout):
    frame = Frame(parent_layout, padding=list_view_pad_x, borderwidth=0)
    widths = main_values.header_widths
    return(
        frame,
        get_header_label(frame, "Id", widths[0]),  # video title label
        get_header_label(frame, "Title", widths[1]),  # video url label
        get_header_label(frame, "Date", widths[2]),  # video date label
        get_header_label(frame, "Views", widths[3]),  # video views label
        get_header_label(frame, "Likes", widths[4]),  # video likes label
        get_header_label(frame, "Comments", widths[5]),  # video comments label
        get_header_label(frame, "Duration", widths[6])  # video duration label
    )


def get_video_items_frames(parent_layout):
    container_frame = Frame(parent_layout, padding=0, borderwidth=0, style="ws.TFrame")
    canvas = Canvas(container_frame, background=WHITE)  # , background="#555555"
    scrollbar = Scrollbar(container_frame, command=canvas.yview, orient=VERTICAL)
    video_list_frame = Frame(canvas, padding=0, borderwidth=0, style="ws.TFrame")
    # set canvas.
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=video_list_frame, anchor="s")
    # add to view.
    canvas.pack(side=LEFT, fill="both", expand=1)
    scrollbar.pack(side=RIGHT, fill="y")
    return container_frame, video_list_frame


def get_statistics_frame(parent_layout):
    frame = Frame(parent_layout, padding=list_view_pad_x, borderwidth=0)
    widths = main_values.header_widths
    return (
        frame,
        get_header_label(frame, "count: 0", widths[0]),  # count
        get_header_label(frame, "views: 0", widths[0]),  # total views
        get_header_label(frame, "likes: 0", widths[0]),  # total likes
        get_header_label(frame, "comments: 0", widths[0]),  # total comments
        get_header_label(frame, "duration: 0:0:0", widths[0]),  # total duration
    )
