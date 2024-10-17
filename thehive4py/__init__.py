import warnings

warnings.warn(
    message=(
        "thehive4py v1.x is not maintained anymore as TheHive v3 and v4 "
        "are end of life. If you are using TheHive v5 please consider "
        "switching to thehive4py v2.x "
        "(https://github.com/TheHive-Project/TheHive4py)!"
    ),
    category=DeprecationWarning,
    stacklevel=2,
)
