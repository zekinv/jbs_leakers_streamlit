"""contact: zekinv@gmail.com
"""
import streamlit as st
import cv2
import time
import datetime
import requests
import traceback
from PIL import Image
import json
import math

from logger import logging
from home import (FAVICON, 
                  HIDE_STREAMLIT_STYLE, 
                  URL_PAST_EVENTS, 
                  URL_RECENT_EVENTS, 
                  CAM1_ID, 
                  CAM1_URL, 
                  CAM1_EVENTS_DEFUALT)

st.set_page_config(
                    page_title="Leakers Audit",
                    page_icon=FAVICON,
                    layout="wide",
                    )

st.markdown("""<h1 style='color: gray;'>Camera-1</h1>""",
            unsafe_allow_html=True)

st.markdown(HIDE_STREAMLIT_STYLE, unsafe_allow_html=True)

s_date = str(datetime.datetime.today().date())
e_date = str(datetime.datetime.today().date())
s_time = "00:00:00"
e_time = "23:59:59"
ascending = "true"
pageNo = 1
pageLimit = 50
pageLmt = 1

cam1_t1, cam1_t2 = st.tabs(["Live", "PastEvents"])

with cam1_t2:
    cam1_t2_con1 = st.container()
    cam1_t2_con2 = st.container()
    cam1_t2_con3 = st.container()
    cam1_t2_con4 = st.container()
    cam1_t2_con5 = st.container()
    cam1_t2_con6 = st.container()
    cam1_t2_con7 = st.container()
    cam1_t2_con8 = st.container()
    cam1_t2_con9 = st.container()
    cam1_t2_con10 = st.container()
    cam1_t2_con11 = st.container()
    cam1_t2_con12 = st.container()
    cam1_t2_con13 = st.container()
    cam1_t2_con14 = st.container()
    cam1_t2_con15 = st.container()
    cam1_t2_con16 = st.container()
    cam1_t2_con17 = st.container()
    cam1_t2_con18 = st.container()
    cam1_t2_con19 = st.container()
    cam1_t2_con20 = st.container()
    cam1_t2_con21 = st.container()
    cam1_t2_con22 = st.container()
    cam1_t2_con23 = st.container()
    cam1_t2_con24 = st.container()
    cam1_t2_con25 = st.container()
    cam1_t2_con26 = st.container()
    cam1_t2_con27 = st.container()

    with cam1_t2_con1:
        cam1_t2_con1_col1,cam1_t2_con1_col2, cam1_t2_con1_col3= st.columns([1.1,5.5,3.4])
        CAM1_SUBMIT_ST = cam1_t2_con1_col1.button(
                                    label="Submit",
                                    type = "primary",
                                    use_container_width = True)
        CAM1_EVENTS_ST = cam1_t2_con1_col2.multiselect(label = '',
                                                    options = CAM1_EVENTS_DEFUALT,
                                                    label_visibility="collapsed",
                                                    placeholder = "Please Select the Events: All Events Selected ")
        CAM1_DATE_ST = cam1_t2_con1_col3.date_input(label = "date",
                                          value= (datetime.datetime.now(), datetime.datetime.now()),
                                          max_value=datetime.datetime.now(),
                                          min_value=datetime.date(2023, 1, 1),
                                          label_visibility="collapsed",)
        if len(CAM1_DATE_ST)==2:
            s_date, e_date = CAM1_DATE_ST
            print("TWO_DATES: {} to {}".format(s_date, e_date))
        else: 
            s_date, *_ = CAM1_DATE_ST
            e_date = s_date
            print("ONE_DATES: {} to {}".format(s_date, e_date))

    with cam1_t2_con3:
        cam1_t2_con3_col1, cam1_t2_con3_col2 = st.columns([5,5])

    with cam1_t2_con4:
        cam1_t2_con4_col1, cam1_t2_con4_col2 = st.columns([5,5])

    with cam1_t2_con5:
        cam1_t2_con5_col1, cam1_t2_con5_col2 = st.columns([5,5])

    with cam1_t2_con6:
        cam1_t2_con6_col1, cam1_t2_con6_col2 = st.columns([5,5])

    with cam1_t2_con7:
        cam1_t2_con7_col1, cam1_t2_con7_col2 = st.columns([5,5])

    with cam1_t2_con8:
        cam1_t2_con8_col1, cam1_t2_con8_col2 = st.columns([5,5])

    with cam1_t2_con9:
        cam1_t2_con9_col1, cam1_t2_con9_col2 = st.columns([5,5])

    with cam1_t2_con10:
        cam1_t2_con10_col1, cam1_t2_con10_col2 = st.columns([5,5])

    with cam1_t2_con11:
        cam1_t2_con11_col1, cam1_t2_con11_col2 = st.columns([5,5])

    with cam1_t2_con12:
        cam1_t2_con12_col1, cam1_t2_con2_col12 = st.columns([5,5])

    with cam1_t2_con13:
        cam1_t2_con13_col1, cam1_t2_con13_col2 = st.columns([5,5])

    with cam1_t2_con14:
        cam1_t2_con14_col1, cam1_t2_con14_col2 = st.columns([5,5])

    with cam1_t2_con15:
        cam1_t2_con15_col1, cam1_t2_con15_col2 = st.columns([5,5])

    with cam1_t2_con16:
        cam1_t2_con16_col1, cam1_t2_con16_col2 = st.columns([5,5])

    with cam1_t2_con17:
        cam1_t2_con17_col1, cam1_t2_con17_col2 = st.columns([5,5])

    with cam1_t2_con18:
        cam1_t2_con18_col1, cam1_t2_con18_col2 = st.columns([5,5])

    with cam1_t2_con19:
        cam1_t2_con19_col1, cam1_t2_con19_col2 = st.columns([5,5])

    with cam1_t2_con20:
        cam1_t2_con20_col1, cam1_t2_con20_col2 = st.columns([5,5])
    
    with cam1_t2_con21:
        cam1_t2_con21_col1, cam1_t2_con21_col2 = st.columns([5,5])

    with cam1_t2_con22:
        cam1_t2_con22_col1, cam1_t2_con22_col2 = st.columns([5,5])

    with cam1_t2_con23:
        cam1_t2_con23_col1, cam1_t2_con23_col2 = st.columns([5,5])

    with cam1_t2_con24:
        cam1_t2_con24_col1, cam1_t2_con24_col2 = st.columns([5,5])

    with cam1_t2_con25:
        cam1_t2_con25_col1, cam1_t2_con25_col2 = st.columns([5,5])

    with cam1_t2_con26:
        cam1_t2_con26_col1, cam1_t2_con26_col2 = st.columns([5,5])
    
    with cam1_t2_con27:
        cam1_t2_con27_col1, cam1_t2_con27_col2 = st.columns([5,5])

    CAM1_PLACEHOLDER = [
                        cam1_t2_con3_col1, cam1_t2_con3_col2,
                        cam1_t2_con4_col1, cam1_t2_con4_col2,
                        cam1_t2_con5_col1, cam1_t2_con5_col2,
                        cam1_t2_con6_col1, cam1_t2_con6_col2,
                        cam1_t2_con7_col1, cam1_t2_con7_col2,
                        cam1_t2_con8_col1, cam1_t2_con8_col2,
                        cam1_t2_con9_col1, cam1_t2_con9_col2,
                        cam1_t2_con10_col1, cam1_t2_con10_col2,
                        cam1_t2_con11_col1, cam1_t2_con11_col2,
                        cam1_t2_con12_col1, cam1_t2_con2_col12,
                        cam1_t2_con13_col1, cam1_t2_con13_col2,
                        cam1_t2_con14_col1, cam1_t2_con14_col2,
                        cam1_t2_con15_col1, cam1_t2_con15_col2,
                        cam1_t2_con16_col1, cam1_t2_con16_col2,
                        cam1_t2_con17_col1, cam1_t2_con17_col2,
                        cam1_t2_con18_col1, cam1_t2_con18_col2,
                        cam1_t2_con19_col1, cam1_t2_con19_col2,
                        cam1_t2_con20_col1, cam1_t2_con20_col2,
                        cam1_t2_con21_col1, cam1_t2_con21_col2,
                        cam1_t2_con22_col1, cam1_t2_con22_col2,
                        cam1_t2_con23_col1, cam1_t2_con23_col2,
                        cam1_t2_con24_col1, cam1_t2_con24_col2,
                        cam1_t2_con25_col1, cam1_t2_con25_col2,
                        cam1_t2_con26_col1, cam1_t2_con26_col2,
                        cam1_t2_con27_col1, cam1_t2_con27_col2,
                       ]

    if CAM1_SUBMIT_ST:
        HEADERS = {'Content-type': 'application/json'}
        if not CAM1_EVENTS_ST:
            CAM1_EVENTS_ST = CAM1_EVENTS_DEFUALT

        CAM1_PAYLOAD_NO_DATA = {
                    "cam_id" : [CAM1_ID],
                    "s_date" : str(s_date),
                    "e_date" : str(e_date),
                    "s_time" : s_time,
                    "e_time" : e_time,
                    "events" : CAM1_EVENTS_ST,
                    "ascending": ascending,
                    "pageNumber" : pageNo,
                    "pageLimit" : pageLmt,
                    }
        print("EVENTS: {}".format(CAM1_PAYLOAD_NO_DATA["events"]))
        print("PAGE_NUMBER: {}".format(pageNo))
        CAM1_NO_OF_DATA_RESPONCE = {}
        try:
            _CAM1_NO_OF_DATA_RESPONCE = requests.request(method="POST", 
                                                         url = URL_PAST_EVENTS, 
                                                         headers=HEADERS, 
                                                         data=json.dumps(CAM1_PAYLOAD_NO_DATA, indent=1), 
                                                         verify=False)
            CAM1_NO_OF_DATA_RESPONCE = _CAM1_NO_OF_DATA_RESPONCE.json()
        except:
            logging.warning(traceback.format_exc())
        if CAM1_NO_OF_DATA_RESPONCE.get('data'):
            cam1_t2_con2.empty()
            print("CAM1_NO_OF_DATA_RESPONCE: {}".format(CAM1_NO_OF_DATA_RESPONCE))
            print("CAM1_NO_OF_DATA_RESPONCE | noData: {}".format(CAM1_NO_OF_DATA_RESPONCE.get('noData')))
            CAM1_NO_OF_PAGES = int(CAM1_NO_OF_DATA_RESPONCE.get('noData'))/50
            print("CAM1_NO_OF_PAGESE: {}".format(CAM1_NO_OF_PAGES))
            if CAM1_NO_OF_PAGES < 1:
                CAM1_NO_OF_PAGES = 1
            with cam1_t2_con2:
                _CAM1_PAGE_NUMBER = st.radio(label="""Total Events: {}\
                                    \nPage No.""".format(CAM1_NO_OF_DATA_RESPONCE.get('noData')), 
                                    options=list(range(1,math.ceil(CAM1_NO_OF_PAGES)+1)),
                                    horizontal=True,
                                    label_visibility="visible")
                try:
                    CAM1_PAGE_NUMBER = int(_CAM1_PAGE_NUMBER)
                except Exception as ERR:
                    print(f"noDATA: {CAM1_NO_OF_DATA_RESPONCE.get('noData')}, no_pages:{CAM1_NO_OF_PAGES}, _pageNumber:{_CAM1_PAGE_NUMBER}")
                    print(ERR)
                    print(traceback.format_exc())
            CAM1_PAYLOAD = {
                        "cam_id" : [CAM1_ID],
                        "s_date" : str(s_date),
                        "e_date" : str(e_date),
                        "s_time" : s_time,
                        "e_time" : e_time,
                        "events" : CAM1_EVENTS_ST,
                        "ascending": ascending,
                        "pageNumber" : CAM1_PAGE_NUMBER,
                        "pageLimit" : pageLimit,
                        }
            print("EVENTS: {}".format(CAM1_PAYLOAD["events"]))
            print("PAGE_NUMBER: {}".format(CAM1_PAYLOAD["pageNumber"]))
            print("PAYLOAD : {}".format(CAM1_PAYLOAD))
            CAM1_DATA = {}
            logging.debug("Camera_1_URL : {}".format(URL_PAST_EVENTS))
            logging.debug("s_date: {}".format(CAM1_PAYLOAD["s_date"]))
            try:
                CAM1_DATA_RESPONCE = requests.request(method="POST", 
                                                      url = URL_PAST_EVENTS, 
                                                      headers=HEADERS, 
                                                      data=json.dumps(CAM1_PAYLOAD, indent=1), 
                                                      verify=False)
                CAM1_DATA = CAM1_DATA_RESPONCE.json()
            except:
                logging.warning(traceback.format_exc())
            print(CAM1_DATA)
            for CAM1_J, CAM1_ITEM in enumerate(CAM1_DATA['data']):
                with CAM1_PLACEHOLDER[CAM1_J]:
                    CAM1_P1 = st.empty()
                    CAM1_P2 = st.empty()
                    CAM1_P3 = st.empty()
                    CAM1_P4 = st.empty()
                    CAM1_P1 .divider()
                    CAM1_P2 .image(CAM1_ITEM['image_url'], use_column_width=True)
                    CAM1_P3 .text(CAM1_ITEM['created_time_stamp'])
                    CAM1_P4 .text(CAM1_ITEM['labels'][0]['label'])

                    
        else:
            for CAM1_COLS in CAM1_PLACEHOLDER:
                with CAM1_COLS:
                    CAM1_P1 = st.empty()
                    CAM1_P2 = st.empty()
                    CAM1_P3 = st.empty()
                    CAM1_P4 = st.empty()
            cam1_t2_con2.empty()
            cam1_t2_con2.text("No Data Avalable")

with cam1_t1:
    #: Count for sleep function if NoData from Live Events
    C = 0
    cam1_t1_col1, cam1_t1_col2 = st.columns([2,5])
    with cam1_t1_col2:

        # CAM1_CAP = cv2.VideoCapture(CAM1_URL)

        # CAM1_TOGGLE_ST = st.toggle("Camera-1 Live",value = False,)
        # CAM1_PLACEHOLDER_ST = st.empty()
        # if CAM1_TOGGLE_ST:
            
        #     CAM1_REC, _CAM1_FRAME = CAM1_CAP.read()
        #     if CAM1_REC:
        #         CAM1_FRAME = cv2.cvtColor(_CAM1_FRAME, cv2.COLOR_BGR2RGB)
        #     else: 
        #         time.sleep(0.009)

        #     CAM1_PLACEHOLDER_ST.image(
        #             use_column_width=True, 
        #             image = CAM1_FRAME
        #             )
        #     with st.spinner("Loading..."):
        #             time.sleep(2)
        CAM1_TOGGLE_ST = st.toggle("Camera-2 Live",value = False,)
        CAM1_PLACEHOLDER_ST = st.empty()
        if CAM1_TOGGLE_ST:
            CAM1_PLACEHOLDER_ST.image(
                    use_column_width=True, 
                    image = CAM1_URL
                    )
            with st.spinner("Loading..."):
                    time.sleep(2)
        else:
            CAM1_PLACEHOLDER_ST.empty()
    with cam1_t1_col1:
        st.text("Recent Detection")
        cam1_t1_col1_con1 = st.container()
        with cam1_t1_col1_con1:
            cam1_t1_col1_con1_p1 = st.empty()
            cam1_t1_col2_con1_p2 = st.empty()
            cam1_t1_col3_con1_p3 = st.empty()
            cam1_t1_col4_con1_p4 = st.empty()

    logging.info("Video_DashBoard_Events_Stream_Func, cam_id: Camera-1")
    print("Video_DashBoard_Events_Stream_Func, cam_id: Camera-1")
    CAM1_TIMESTAMP = None

    #: While loop will Break after 20 minuts // in streamlit case will not Break 
    CAM1_NOW = datetime.datetime.now()+datetime.timedelta(minutes = 20)
    while True:
        if CAM1_NOW < datetime.datetime.now():
            break
        CAM1_RES = dict()
        try:
            CAM1_LIVE_URL = "{}?cam_id={}&timestamp={}".format(URL_RECENT_EVENTS,
                                                                CAM1_ID,
                                                                CAM1_TIMESTAMP)
            logging.debug("URL", CAM1_LIVE_URL)
            _CAM1_RES = requests.get(url = CAM1_LIVE_URL)
            if _CAM1_RES.status_code >= 200 and _CAM1_RES.status_code < 300:
                logging.debug("status_code: ", _CAM1_RES.status_code)
                CAM1_RES = _CAM1_RES.json()
            else:
                logging.warning("WARNINR | status_code: {}".format(_CAM1_RES.status_code))
                CAM1_RES = {
                    'data': []
                }
            print("CAM1_RES", CAM1_RES)
        except Exception as ERR:
            logging.critical(ERR)
            logging.critical(traceback.format_exc())

        _CAM1_DATA_LIVE = CAM1_RES.get('data')
        if _CAM1_DATA_LIVE:
            C = 0
            CAM1_TIMESTAMP = CAM1_RES.get('timestamp')
            for CAM1_DATA_LIVE in _CAM1_DATA_LIVE:
                CAM1_IMG = CAM1_DATA_LIVE["image"]
                cam1_t1_col1_con1_p1.image(CAM1_IMG,use_column_width=True)
                cam1_t1_col2_con1_p2.text(f"{CAM1_DATA_LIVE['labels'][0]}")
                # cam1_t1_col3_con1_p3.text(f"Score : {CAM1_DATA_LIVE['score']}")
                cam1_t1_col4_con1_p4.text(f"{CAM1_DATA_LIVE['timestamp']}")

        else:
            print(C)
            C += 1
            if C > 10:
                time.sleep(10)
            else:
                time.sleep(3)
            print("NO_DATA")
            # logging.warning("NO DATA")
            CAM1_TIMESTAMP = CAM1_RES.get('timestamp')
