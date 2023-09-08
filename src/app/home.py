"""contact: zekinv@gmail.com
"""

import streamlit as st
from PIL import Image
import os
from st_pages import Page, show_pages, add_page_title, Section

LEVEL = os.getenv("LOGGER")

FAVICON = Image.open("./static/favicon.ico")
JBS_HOME_IMG = Image.open("./static/jbsfoods_home_img.png")


# URL_PAST_EVENTS = "http://10.161.227.67:5001/analytics_event_summary"
# URL_RECENT_EVENTS = "http://10.161.227.67:5001/video_dashboard_recent_events"

# CAM1_URL = "http://10.161.243.210/cgi-bin/video.cgi?User=CustomAuth&type=http&cameraID=1&Auth=amJzQFNOTF9DR0kgVG8gMTZCMDBEQDA4MTk3ZjNkYTZkYjIwODY2NjZiMTk3MGU2YzEwZjgzQC9jZ2ktYmluL3ZpZGVvLmNnaT9Vc2VyPUN1c3RvbUF1dGgmdHlwZT1odHRwJmNhbWVyYUlEPTEmbWpwZWdwbGF5PTFAYjBmZWIxNzRlOTQxYWU4MGRiMzgwODBiOWZhY2YwNjg=&mjpegplay=1"
# CAM2_URL = "rtsp://admin:password@10.161.243.209:554/snl/live/1/1"

URL_PAST_EVENTS = os.getenv("URL_PAST_EVENTS")
URL_RECENT_EVENTS = os.getenv("URL_RECENT_EVENTS")

CAM1_URL = os.getenv("CAM1_URL")
CAM2_URL = os.getenv("CAM2_URL")

# CAM1_ID = "645b4849abc45c23e25a6efb"
# CAM2_ID = "646b30872f68a9d3cc89cac5"

CAM1_ID = os.getenv("CAM1_ID")
CAM2_ID = os.getenv("CAM2_ID")

CAM1_EVENTS_DEFUALT = [
                        "BACK_RIB",
                        "BRISKET_1",
                        "CHUCK_FLAP_2",
                        "CHUCK_SHORT_RIB_2",
                        "CHUCK_TENDER_2",
                        "CHUCK_TENDER_5",
                        "CHUCK_1",
                        "CLOD/HEART_1",
                        "CLOD_TOP_BLADE_1",
                        "FLANK",
                        "HANGING_TENDER_2",
                        "INSIDE_SKIRT_2",
                        "INSIDE_SKIRT_6",
                        "LIFTER_MEAT/PECTORAL",
                        "NAVEL_FINGER_MEAT_5lb",
                        "NAVEL_1",
                        "OUTSIDE_SKIRT_2",
                        "OUTSIDE_SKIRT_4",
                        "RIB_BI_1",
                        "RIB_BNLS_1",
                        "RIB_FINGER_MEAT_12",
                        "RIB_SHORT_RIB_2",
                        "SHORT_RIB_CAP_2",
                        "TERES_MAJOR_6",
                        "RIB_SHORT_RIB_2_c1",
                        "RIB_SHORT_RIB_2_c2",
                        "BRISKET_OYSTER_6",
                        "RIB_BNLS_0.5",
                        "RIB_FINGER_MEAT_40",
                        "BRISKET_POINT_2",
                        "CHUCK_FLAP_8",
                        "TERES_MAJOR_15",
                        ]

CAM2_EVENTS_DEFUALT = [
                        "LOIN_BNLS_1",
                        "LOIN_BI_1",
                        "TENDERLOIN_1",
                        "BOTTOM_ROUND_EYE_1",
                        "INSIDE_ROUND_1",
                        "KNUCKLE_1",
                        "LOIN_BNLS_05",
                        "BALL_TIP_7_9",
                        "FLAP_MEAT_4",
                        "D_SHANK_2",
                        "LOIN_TAIL_1",
                        "BOTTOM_ROUND_FLAT_1",
                        "TOP_BUTT_CAP_1",
                        "TOP_BUTT_CAP_2",
                        "TOP_BUTT_1",
                        "TOP_BUTT_2",
                        "TENDERLOIN_PEELED_1",
                        "LOIN TAIL_6_8",
                        "TRI_TIP_4",
                        "TRI-TIP_6_7_8",
                        "LOIN TAIL_4",
                        "BOTTOM_ROUND_1",
                        "LOIN TAIL_2",
                        "TOP BUTT 1 small",
                        ]

#: Hide an Remove Streamlit referencess
HIDE_STREAMLIT_STYLE = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
            </style>
            """

HIDE_STREAMLIT_STYLE_HOME = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

def main():
    st.set_page_config(
                        page_title="Leakers Audit",
                        page_icon=FAVICON,
                        )
    st.markdown(HIDE_STREAMLIT_STYLE_HOME, unsafe_allow_html=True)
    st.image(JBS_HOME_IMG)
    add_page_title()
    show_pages([
            Page("home.py", "Leakers Audit", ""),
            Page("./pages/camera_1.py", "Camera 1", ":cinema:"),
            Page("./pages/camera_2.py", "Camera 2", ":cinema:"),
            ])

if __name__ == '__main__':
    main()
