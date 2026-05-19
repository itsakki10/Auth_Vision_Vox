import streamlit as st


def footer_home():

    c1, c2, c3 = st.columns([3,2,3])

    with c2:

        st.markdown(
        """
        <p style='
        text-align:center;
        color:#6B7280;
        font-size:16px;
        font-weight:500;
        '>

        Created with ❤️ by
        <span style='
        color:#7C3AED;
        font-weight:700;
        '>

        Akash Mehra

        </span>

        </p>
        """,
        unsafe_allow_html=True
        )



def footer_dashboard():

    c1, c2, c3 = st.columns([3,2,3])

    with c2:

        st.markdown(
        """
        <p style='
        text-align:center;
        color:#374151;
        font-size:16px;
        font-weight:500;
        '>

        Created with ❤️ by
        <span style='
        color:#7C3AED;
        font-weight:700;
        '>

        Akash Mehra

        </span>

        </p>
        """,
        unsafe_allow_html=True
        )