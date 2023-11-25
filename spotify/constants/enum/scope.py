from enum import Enum


class Scope(Enum):
    # Images
    UGC_IMAGE_UPLOAD = "ugc-image-upload"
    USER_READ_PLAYBACK_STATE = "user-read-playback-state"
    USER_MODIFY_PLAYBACK_STATE = "user-modify-playback-state"
    USER_READ_CURRENTLY_PLAYING = "user-read-currently-playing"

    # Playback
    APP_REMOTE_CONTROL = "app-remote-control"
    STREAMING = "streaming"

    # Playlists
    PLAYLIST_READ_PRIVATE = "playlist-read-private"
    PLAYLIST_READ_COLLABORATIVE = "playlist-read-collaborative"
    PLAYLIST_MODIFY_PRIVATE = "playlist-modify-private"
    PLAYLIST_MODIFY_PUBLIC = "playlist-modify-public"

    # Follow
    USER_FOLLOW_MODIFY = "user-follow-modify"
    USER_FOLLOW_READ = "user-follow-read"

    # Listening History
    USER_READ_PLAYBACK_POSITION = "user-read-playback-position"
    USER_TOP_READ = "user-top-read"
    USER_READ_RECENTLY_PLAYED = "user-read-recently-played"

    # Library
    USER_LIBRARY_MODIFY = "user-library-modify"
    USER_LIBRARY_READ = "user-library-read"

    # Users
    USER_READ_EMAIL = "user-read-email"
    USER_READ_PRIVATE = "user-read-private"

    # Open Access
    USER_SOA_LINK = "user-soa-link"
    USER_SOA_UNLINK = "user-soa-unlink"
    USER_MANAGE_ENTITLEMENTS = "user-manage-entitlements"
    USER_MANAGE_PARTNER = "user-manage-partner"
    USER_CREATE_PARTNER = "user-create-partner"
