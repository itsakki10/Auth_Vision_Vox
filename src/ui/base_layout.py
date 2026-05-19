import streamlit as st


# ================= HOME BACKGROUND =================

import streamlit as st

def style_background_home():

    st.markdown("""
    <style>

    .stApp{
        background:
        linear-gradient(
        135deg,
        #DCE5FF 0%,
        #EEF2FF 45%,
        #EEE4FF 100%
        ) !important;

        overflow-x:hidden;
    }


    /* LEFT BLUE GLOW */

    .stApp::before{

        content:"";
        position:fixed;

        top:-12vw;
        left:-12vw;

        width:40vw;
        height:40vw;

        min-width:300px;
        min-height:300px;

        background:
        radial-gradient(
        circle,
        rgba(99,102,241,.14),
        transparent 70%
        );

        border-radius:50%;
        filter:blur(90px);

        z-index:0;
        pointer-events:none;
    }


    /* RIGHT PINK GLOW */

    .stApp::after{

        content:"";
        position:fixed;

        bottom:-15vw;
        right:-15vw;

        width:45vw;
        height:45vw;

        min-width:350px;
        min-height:350px;

        background:
        radial-gradient(
        circle,
        rgba(236,72,153,.16),
        transparent 70%
        );

        border-radius:50%;
        filter:blur(100px);

        z-index:0;
        pointer-events:none;
    }



    /* TOP LEFT CURVE */

    .curve-lines{

        position:fixed;

        top:-3vw;
        left:-3vw;

        width:clamp(150px,22vw,280px);
        height:clamp(150px,22vw,280px);

        opacity:.45;

        background:
        repeating-radial-gradient(
        circle at top left,

        transparent 0px,
        transparent 11px,

        rgba(167,139,250,.45) 12px,
        rgba(167,139,250,.45) 14px
        );

        z-index:1;
        pointer-events:none;
    }



    /* TOP RIGHT DOTS */

    .dot-pattern{

        position:fixed;

        top:8vh;
        right:4vw;

        width:clamp(60px,10vw,120px);
        height:clamp(60px,10vw,120px);

        background-image:
        radial-gradient(
        #B794F6 1.8px,
        transparent 1.8px
        );

        background-size:20px 20px;

        opacity:.6;

        z-index:1;
        pointer-events:none;
    }

    </style>

    <div class="curve-lines"></div>
    <div class="dot-pattern"></div>

    """, unsafe_allow_html=True)


# ================= DASHBOARD =================

def style_background_dashboard():

    st.markdown("""
    <style>

    .stApp{

        background:
        linear-gradient(
        135deg,
        #DCE5FF 0%,
        #EEF2FF 45%,
        #EEE4FF 100%
        ) !important;

        overflow:hidden;
    }


    .stApp::before{

        content:"";

        position:fixed;

        top:-180px;
        left:-180px;

        width:500px;
        height:500px;

        background:
        radial-gradient(
        circle,
        rgba(99,102,241,.14),
        transparent 70%
        );

        border-radius:50%;

        filter:blur(90px);

        z-index:-1;

        pointer-events:none;
    }


    .stApp::after{

        content:"";

        position:fixed;

        bottom:-220px;
        right:-220px;

        width:650px;
        height:650px;

        background:
        radial-gradient(
        circle,
        rgba(236,72,153,.18),
        transparent 70%
        );

        border-radius:50%;

        filter:blur(100px);

        z-index:-1;

        pointer-events:none;
    }

    </style>
    """, unsafe_allow_html=True)




# ================= MAIN CSS =================

def style_base_layout():

    st.markdown("""

<style>

@import url(
'https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap'
);



#MainMenu,
footer,
header{

visibility:hidden;

}



/* page */

.block-container{

padding-top:.5rem!important;

padding-left:2rem!important;

padding-right:2rem!important;

max-width:1150px!important;

}



/* fonts */

html,
body,
[class*="css"]{

font-family:'Poppins',sans-serif;

}



/* title */

h1{

font-size:4rem!important;

font-weight:800!important;

line-height:.85!important;

background:
linear-gradient(
90deg,
#4F46E5,
#A855F7
);

-webkit-background-clip:text;

-webkit-text-fill-color:transparent;

}



/* heading */

h2{

font-size:2rem!important;

font-weight:700!important;

color:#374151!important;

text-align:center;

}



/* text */

p{

color:#374151!important;

font-size:18px;

text-align:center;

line-height:1.6;

}



/* CARDS */

div[data-testid="stVerticalBlock"] > div:has(button){

background:
rgba(255,255,255,.26);

border:
1px solid rgba(
255,
255,
255,
.4
);

border-radius:35px;

padding:30px;

backdrop-filter:blur(18px);

box-shadow:
0 10px 35px rgba(
0,
0,
0,
.04
);

transition:.3s;

}



/* card hover */

div[data-testid="stVerticalBlock"] > div:has(button):hover{

transform:translateY(-6px);

}



/* button common */

.stButton > button{

height:58px;

border-radius:18px;

border:none;

font-size:18px;

font-weight:600;

color:white!important;

transition:.3s;

}



/* STUDENT */

button[kind="primary"]{

background:
linear-gradient(
90deg,
#3563FF,
#6D4DFF
)!important;

}



/* TEACHER */

button[kind="secondary"]{

background:
linear-gradient(
90deg,
#EC4899,
#A855F7
)!important;

}



/* hover */

.stButton button:hover{

transform:scale(1.02);

box-shadow:
0 12px 25px rgba(
79,
70,
229,
.25
);

}



/* mobile */

@media(max-width:768px){

.block-container{

padding-left:1rem!important;

padding-right:1rem!important;

}

h1{

font-size:3rem!important;

}

}


</style>

""",unsafe_allow_html=True)