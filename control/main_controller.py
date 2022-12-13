from view.main_view import MainView
from model.data_handler import get_playlist_id, get_service
from model.playlist_client import PlaylistClient
from model.data_handler import STANDER_PLAYLIST_URL, extract_target_info
from model.video_view import VideoView
from model.video_analyzer import VideoAnalyser
from setting.colors import LIGHT_GRAY, BLACK

MAIN_VIEW: MainView = None


def init_controller(main_view: MainView):
    global MAIN_VIEW
    MAIN_VIEW = main_view
    view_placeholder(None)
    MAIN_VIEW.url_entry.bind("<Return>", get_url)
    MAIN_VIEW.url_entry.bind("<FocusIn>", remove_placeholder)
    MAIN_VIEW.url_entry.bind("<FocusOut>", view_placeholder)
    MAIN_VIEW.message_button.config(command=MAIN_VIEW.remove_message_frame)
    MAIN_VIEW.past_button.config(command=paste_url)


def get_url(_):
    """
    get text from entry, validate that text, extract playlist id from it
    then start request the target and sow result.
    """
    status, playlist_id = get_playlist_id(MAIN_VIEW.url_entry.get())
    if status:
        status, result = get_service()
        if status:
            status, result = PlaylistClient(result, playlist_id).request()
            if status:
                show_videos(result)
            else:
                MAIN_VIEW.add_message_frame(result)
            if not status:
                MAIN_VIEW.add_message_frame(result)
        else:
            MAIN_VIEW.add_message_frame(result)
    else:
        MAIN_VIEW.add_message_frame(playlist_id)


def paste_url():
    """ paste url from clipboard to entry"""
    MAIN_VIEW.url_entry.configure(foreground=BLACK)
    MAIN_VIEW.url_entry.delete(0, "end")
    try:
        MAIN_VIEW.url_entry.insert(
            0, MAIN_VIEW.window.selection_get(selection="CLIPBOARD")
        )
    except:
        MAIN_VIEW.add_message_frame("nothing to past !")


def view_placeholder(_):
    """  prepare entry to show placeholder """
    MAIN_VIEW.url_entry.configure(foreground=LIGHT_GRAY)
    MAIN_VIEW.url_entry.delete(0, "end")
    MAIN_VIEW.url_entry.insert(0, STANDER_PLAYLIST_URL)


def remove_placeholder(_):
    MAIN_VIEW.url_entry.configure(foreground=BLACK)
    MAIN_VIEW.url_entry.delete(0, "end")


def show_videos(videos_data):
    MAIN_VIEW.disable_all_action_views()
    analyzer = VideoAnalyser()
    for data in videos_data:
        info = extract_target_info(data)
        video_view = VideoView(MAIN_VIEW.videos_list_frame, info)
        MAIN_VIEW.add_video_view(video_view)
        analyzer.calculate_total(info)
    MAIN_VIEW.set_statistics_labels(analyzer)
    MAIN_VIEW.enable_all_action_views()



