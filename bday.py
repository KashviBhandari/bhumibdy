import streamlit as st
from PIL import Image
import os
import time
import base64
#import streamlit as st

st.set_page_config(
    page_title="Happy Birthday ❤️",
    page_icon="🎂",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background: linear-gradient(-45deg,#ff9a9e,#fad0c4,#fad0c4,#a18cd1);
background-size:400% 400%;
animation:gradient 10s ease infinite;
}

@keyframes gradient{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.main-card{
background:rgba(255,255,255,0.2);
backdrop-filter:blur(15px);
padding:40px;
border-radius:25px;
text-align:center;
box-shadow:0 8px 32px rgba(0,0,0,.2);
margin-top:40px;
}

.title{
font-size:60px;
font-weight:bold;
color:white;
text-shadow:3px 3px 10px rgba(0,0,0,.3);
}

.subtitle{
font-size:28px;
color:white;
margin-top:20px;
}

.stButton>button{
background:linear-gradient(45deg,#ff4b91,#ff8fab);
color:white;
border:none;
padding:15px 40px;
border-radius:50px;
font-size:22px;
font-weight:bold;
transition:.3s;
}

.stButton>button:hover{
transform:scale(1.08);
box-shadow:0 0 20px #ff4b91;
}

img{
border-radius:20px;
box-shadow:0 10px 30px rgba(0,0,0,.3);
}

.footer{
text-align:center;
font-size:24px;
color:white;
margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-card">
<div class="title">🎂 Happy Birthday Bhumi 🎂</div>
<div class="subtitle">
Wishing you endless happiness, laughter, and beautiful memories! ❤️✨
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.hearts{
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    pointer-events:none;
    overflow:hidden;
    z-index:999;
}

.heart{
    position:absolute;
    bottom:-50px;
    font-size:35px;
    animation: float 8s linear infinite;
}

.heart:nth-child(1){left:5%;animation-delay:0s;}
.heart:nth-child(2){left:20%;animation-delay:2s;}
.heart:nth-child(3){left:35%;animation-delay:4s;}
.heart:nth-child(4){left:50%;animation-delay:1s;}
.heart:nth-child(5){left:65%;animation-delay:3s;}
.heart:nth-child(6){left:80%;animation-delay:5s;}
.heart:nth-child(7){left:95%;animation-delay:2s;}

@keyframes float{
    0%{
        transform:translateY(0) rotate(0deg);
        opacity:1;
    }
    100%{
        transform:translateY(-120vh) rotate(360deg);
        opacity:0;
    }
}
</style>

<div class="hearts">
<div class="heart">❤️</div>
<div class="heart">💖</div>
<div class="heart">💕</div>
<div class="heart">💗</div>
<div class="heart">💞</div>
<div class="heart">💓</div>
<div class="heart">❤️</div>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.butterflies{
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    pointer-events:none;
    overflow:hidden;
    z-index:999;
}

.butterfly{
    position:absolute;
    font-size:35px;
    animation: fly 12s linear infinite;
}

.butterfly:nth-child(1){top:10%; left:-10%; animation-delay:0s;}
.butterfly:nth-child(2){top:25%; left:-15%; animation-delay:2s;}
.butterfly:nth-child(3){top:45%; left:-20%; animation-delay:4s;}
.butterfly:nth-child(4){top:65%; left:-10%; animation-delay:6s;}
.butterfly:nth-child(5){top:80%; left:-15%; animation-delay:8s;}

@keyframes fly{
    0%{
        transform:translateX(0) translateY(0) rotate(0deg);
        opacity:0;
    }

    10%{
        opacity:1;
    }

    50%{
        transform:translateX(60vw) translateY(-50px) rotate(20deg);
    }

    100%{
        transform:translateX(120vw) translateY(50px) rotate(-20deg);
        opacity:0;
    }
}
</style>

<div class="butterflies">
    <div class="butterfly">🦋</div>
    <div class="butterfly">🦋</div>
    <div class="butterfly">🦋</div>
    <div class="butterfly">🦋</div>
    <div class="butterfly">🦋</div>
</div>
""", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image(
        "photos/image1.jpeg",
        use_container_width=True
    )

st.balloons()
st.success("May all your dreams come true! ❤️")

st.markdown("""
<div class="footer">
🌸 Made with Love 🌸
</div>
""", unsafe_allow_html=True)
# ------------------
# SURPRISE BUTTON
# ------------------

st.title("🎁 Birthday Surprise")

if st.button("✨ Open Your Surprise ✨"): 

    st.markdown(
        '<p class="title">🎉 HAPPY BIRTHDAY 🎉</p>',
        unsafe_allow_html=True
    )

    friend_name = "mere adopet maa"

    st.markdown(
        f'<p class="subtitle"> {friend_name} ❤️</p>',
        unsafe_allow_html=True
    )

    st.write("")

    # ------------------
    # PHOTO GALLERY
    # ------------------

    st.header("📸 KUCH YAAD ")

    photo_folder = "photos"

    photos = []

    if os.path.exists(photo_folder):
        photos = sorted([
            f for f in os.listdir(photo_folder)
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
        ])

    if photos:
        placeholder = st.empty()

        for photo in photos:
            placeholder.image(
                os.path.join(photo_folder, photo),
                width=350  # Image size
            )
            time.sleep(3)  # 3 seconds per image
    st.write("---")

    # ------------------
    # CAKE
    # ------------------

    st.header("Babyyyy cakeee 👄")

    img_path = "imag2.png"

    if os.path.exists(img_path):
        st.image(img_path, width=300)
    else:
        st.warning("Cake image not found")

    st.write("---")
    # ------------------
    # MESSAGE
    # ------------------

if st.button("💌 Read My Letter"):

    message = """
        🎂 Happy Birthday meri pyaari kuttiya! ❤️🐶

        Aaj tera special din hai, isliye aaj tujhe kam pareshan karunga. 😂

        Chhoti si hai tu,
        Par dimaag tera kabhi baccho jaisa, kabhi buddho jaisa chalta hai. 🤦‍♂️

        Tere nakhre alag hi level ke hain.
        Teri bakbak ka koi competition nahi hai.
        Kabhi itna hasa deti hai ki pet dukhne lagta hai.
        Kabhi itna gussa dilati hai.

        Fir bhi tu bahut special hai.
        Aur hamesha rahegi.

        Kitna bhi lad lein hum,
        Kitni bhi nok-jhok ho jaye,
        Lekin saath kabhi nahi chhodenge.

        Tu meri favourite pagal insaan hai.
        Aur meri permanent tension bhi.

        Teri har smile bahut pyari lagti hai.
        Tera gussa bhi cute lagta hai.

        Teri har wish poori ho.
        Har sapna sach ho.
        Har din khushiyon se bhara ho.

        Zindagi mein bahut success mile.
        Achhe dost mile.
        Achhi kismat mile.

        Kabhi udaas mat hona.
        Kabhi himmat mat harna.

        Cake ache se khana.
        Gifts jamkar lena.
        Photos bahut saari khinchwana.

        Kisi ki tension mat lena.
        Sirf enjoy karna.

        Bade sapne dekhna.
        Aur unhe poora bhi karna.

        Kabhi khud par doubt mat karna.
        Tu bahut kuch kar sakti hai.

        Bas mehnat karte rehna.
        Aur muskuraate rehna.

        Meri taraf se tujhe dher saara pyaar.
        Dher saari duayein.
        Dher saari khushiyan.

        Chahe kitni bhi badi ho jana,
        Mere liye tu wahi chhoti si pagal kuttiya rahegi. ❤️😂

        Bhagwan tujhe hamesha khush rakhe.

        🎂🎉 Happy Birthday meri pyaari kuttiya,
        meri bhai,
        meri favourite pagal insaan!

        ❤️✨ JANAMDIN KI DHER SAARI BADHAIYAAN! ✨❤️
        """


    box = st.empty()
    text = ""

    for ch in message:
        text += ch
        box.markdown(
            f"""
            <div style="
            font-size:28px;
            color:white;
            text-align:center;
            background:rgba(255,255,255,0.15);
            padding:20px;
            border-radius:20px;">
            {text}
            </div>
            """,
            unsafe_allow_html=True,
        )
        time.sleep(0.01)

    st.success("🥳 Enjoy Your Special Day! 🥳")
    st.balloons()
    # ------------------
    # QUOTE
    # ------------------

    st.success(
        "✨ Count your life by smiles, not tears. Count your age by friends, not years. ✨"
    )

    # ------------------
    # MUSIC
    # ------------------

    st.header("🎵 Birthday Song")

    st.video(
        "https://www.youtube.com/watch?v=90w2RegGf9w"
    )

    st.write("---")

    # ------------------
    # FINAL SURPRISE
    # ------------------

    st.header("🎁 One Last Surprise")

    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)

    st.balloons()

    st.markdown(
        """
        # ❤️🥳🎂🎉

        ## May your day be as wonderful as you are!

        ### Have an amazing birthday!

        💕 Stay happy.
        💕 Stay blessed.
        💕 Keep smiling.

        🎉 HAPPY BIRTHDAY 🎉

        """
    )
    
