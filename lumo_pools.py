
from lumo_filehandler import outlist, is_Sunday
from lumo_pools_shimmering import get_existing_stars

outlist_pool = [line.strip().upper() for line in open(outlist).readlines()]
sunday_pool  = (["PREP SUNDAY CHECKLIST"] if is_Sunday else [])

bernard_pool = [
    "BODIES",
    "PERALS",
    "MY EXPERIMENT IS TO DO [x] MINS OF MEDS DAILY",
    "PREPARE SOME KIND OF LUNCH",
    "MAKEUP",
    ]  + (outlist_pool
       + sunday_pool)

glitter_kindness = [
    ]

thomasoflight_pool = [
    "ELM!",
    "TYPING",
    "CODE READING - ELM"
    ]

marie_pool = [
    "HOW CAN I GET 15 MINUTES OF PAINTING IN?"
    # "UI",
    # "AFFINITY WORKBOOK"
    ]

aprill_pool = [
    "APRL-SONGS"
    ]

julian_pool = [
    "ECONOMICS"
    ]

ada_pool = [
    "LEGGERE ITALIANO"
    ]

utfh_pool = [
    # "SEND SUPER RESUME TO PEOPLE (3-5)"
    ]

windwalk_pool = [
    "BANKING",
    "SCHEDULE SOCIAL",
    "SCHEDULE SUPPORT"
    ]

soul_pool = [
    "NATURE",
    "FRIENDS",
    "SUPPORT/HEALING"
    ]

shimmering_stars = get_existing_stars()

