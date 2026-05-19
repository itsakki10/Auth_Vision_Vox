import streamlit as st

from src.ui.base_layout import (
    style_base_layout,
    style_background_home
)


def home_screen():

    style_background_home()
    style_base_layout()

    # ================= LOGO =================

    _, center, _ = st.columns([2,1,2])
    
    with center:
        st.markdown(
    "<div style='margin-top:-35px'></div>",
    unsafe_allow_html=True
    )
        
        st.image(
            "assets/logo.png",
            width=140
        )


    # ================= TITLE =================

    st.markdown(
        """
        <h1 style='
        text-align:center;
        font-size:72px;
        font-weight:800;
        line-height:.85;
        margin-top:0px;
        margin-bottom:10px;
        '>
        AUTH VISION <br> VOX
        </h1>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <p style='
        text-align:center;
        color:#6B7280;
        font-size:22px;
        margin-top:0px;
        margin-bottom:10px;
        '>

        Smart Attendance. Secure Identity.

        </p>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <hr style='
        width:150px;
        margin:auto;
        border:.5px solid #C084FC;
        margin-bottom:35px;
        '>
        """,
        unsafe_allow_html=True
    )


    # ================= CARDS WRAPPER =================

    col1, col2 = st.columns(
        2,
        gap="large"
    )


    # ================= STUDENT =================

    with col1:

        with st.container():

            _,img,_ = st.columns([1,2,1])

            with img:

                st.image(
                    "assets/student.png",
                    width=180
                )


            st.markdown(
                """
                <h2 style='text-align:center'>
                I'm a STUDENT
                </h2>
                """,
                unsafe_allow_html=True
            )


            st.markdown(
                """
                <p style='text-align:center'>
                Mark attendance, view history and
                manage your profile.
                </p>
                """,
                unsafe_allow_html=True
            )


            if st.button(
                "Student Portal →",
                type="primary",
                use_container_width=True,
                key="student"
            ):
                st.session_state["login_type"] = "student"
                st.rerun()


    # ================= TEACHER =================

    with col2:

        with st.container():

            _,img,_ = st.columns([1,2,1])

            with img:

                st.image(
                    "assets/teacher.png",
                    width=180
                )


            st.markdown(
                """
                <h2 style='text-align:center'>
                I'm a TEACHER
                </h2>
                """,
                unsafe_allow_html=True
            )


            st.markdown(
                """
                <p style='text-align:center'>
                Manage classes, view reports and
                monitor attendance.
                </p>
                """,
                unsafe_allow_html=True
            )


            if st.button(
                "Teacher Portal →",
                type="secondary",
                use_container_width=True,
                key="teacher"
            ):
                st.session_state["login_type"] = "teacher"
                st.rerun()