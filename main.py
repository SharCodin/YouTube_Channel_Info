"""Get Channel info from YouTube video"""

import sys

from utils import get_channel_id_from_video, get_info_from_subscriptions


if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        get_channel_id_from_video(url)
    else:
        get_info_from_subscriptions()
