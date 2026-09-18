import streamlit as st

st.set_page_config(
    page_title="My Profile",
    page_icon="👤",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #eef2ff, #fdf2f8);
    }

    .profile-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin-top: 20px;
    }

    .profile-title {
        color: #6366f1;
        text-align: center;
    }

    .profile-text {
        font-size: 18px;
        line-height: 1.8;
    }
</style>
""", unsafe_allow_html=True)

st.title("👤 My Profile")
st.write("Tell me a little about yourself!")

st.divider()

# Input form
name = st.text_input("👋 Name")
age = st.number_input("🎂 Age", min_value=1, max_value=120, step=1)
school = st.text_input("🏫 School")
subject = st.text_input("📚 Favorite subject")
hobby = st.text_input("🎨 Favorite hobby")

if st.button("✨ Create My Profile", use_container_width=True):
    if name and school and subject and hobby:
        st.markdown(f"""
        <div class="profile-card">
            <h2 class="profile-title">🌟 Hello, {name}!</h2>
            <div class="profile-text">
                👋 My name is <b>{name}</b>.<br>
                🎂 I am <b>{age}</b> years old.<br>
                🏫 I go to <b>{school}</b>.<br>
                📚 My favorite subject is <b>{subject}</b>.<br>
                🎨 I enjoy <b>{hobby}</b>.
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Please fill in all the fields first! 😊")
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Neon Calculator",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# PAGE BACKGROUND
# ---------------------------------------------------------

st.markdown("""
<style>

    /* Remove Streamlit default spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 900px;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* Background */
    .stApp {
        background:
            radial-gradient(circle at 20% 20%, #14213d 0%, transparent 35%),
            radial-gradient(circle at 80% 80%, #24103d 0%, transparent 35%),
            linear-gradient(135deg, #050509, #0a0a12 50%, #050509);
    }

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.markdown("""
<div style="
    text-align:center;
    margin-bottom:18px;
">
    <div style="
        font-size:42px;
        font-weight:900;
        letter-spacing:3px;
        color:#ffffff;
        text-shadow:
            0 0 5px #00eaff,
            0 0 15px #00eaff,
            0 0 30px #0077ff;
    ">
        🧮 NEON CALCULATOR
    </div>

    <div style="
        color:#7eeeff;
        font-size:13px;
        letter-spacing:4px;
        margin-top:5px;
    ">
        FUTURISTIC • FAST • DIGITAL
    </div>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# CALCULATOR
# ---------------------------------------------------------

calculator_html = r"""
<!DOCTYPE html>
<html>

<head>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>

* {
    box-sizing: border-box;
    font-family: Arial, Helvetica, sans-serif;
    user-select: none;
}

body {
    margin: 0;
    padding: 10px;
    background: transparent;
}

.calculator {

    width: 100%;
    max-width: 620px;

    margin: auto;

    padding: 22px;

    border-radius: 30px;

    background:
        linear-gradient(
            145deg,
            rgba(25,25,40,0.98),
            rgba(5,5,12,0.98)
        );

    border: 1px solid rgba(0, 234, 255, 0.25);

    box-shadow:
        0 0 20px rgba(0,234,255,0.12),
        0 0 60px rgba(90,0,255,0.12),
        inset 0 0 30px rgba(255,255,255,0.02);

    position: relative;

    overflow: hidden;
}


/* Neon line around calculator */

.calculator::before {

    content: "";

    position: absolute;

    top: -2px;
    left: -2px;
    right: -2px;
    height: 3px;

    background:
        linear-gradient(
            90deg,
            #00eaff,
            #0077ff,
            #a000ff,
            #ff00aa,
            #00eaff
        );

    background-size: 300% 100%;

    animation: neonLine 4s linear infinite;

}

@keyframes neonLine {

    0% {
        background-position: 0%;
    }

    100% {
        background-position: 300%;
    }

}


/* Brand */

.brand {

    display: flex;

    align-items: center;

    gap: 12px;

    margin-bottom: 15px;

}

.logo {

    width: 48px;
    height: 48px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 14px;

    background:
        linear-gradient(
            135deg,
            #00eaff,
            #0066ff
        );

    box-shadow:
        0 0 15px rgba(0,234,255,0.6);

    font-size: 26px;

}

.brand-title {

    color: white;

    font-size: 23px;

    font-weight: bold;

    letter-spacing: 2px;

}

.brand-subtitle {

    color: #5eeeff;

    font-size: 10px;

    letter-spacing: 3px;

    margin-top: 3px;

}


/* Display */

.display {

    background:
        linear-gradient(
            145deg,
            #05070a,
            #10151c
        );

    border-radius: 20px;

    border: 1px solid rgba(0,234,255,0.2);

    padding: 18px;

    margin-bottom: 18px;

    min-height: 120px;

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: flex-end;

    box-shadow:
        inset 0 0 25px rgba(0,0,0,0.9),
        0 0 15px rgba(0,234,255,0.05);

    overflow: hidden;

}

.expression {

    width: 100%;

    text-align: right;

    color: #64717e;

    font-size: 17px;

    min-height: 25px;

    overflow-x: auto;

    white-space: nowrap;

}

.result {

    width: 100%;

    text-align: right;

    color: #ffffff;

    font-size: clamp(30px, 7vw, 50px);

    font-weight: 700;

    letter-spacing: 1px;

    overflow-x: auto;

    white-space: nowrap;

    text-shadow:
        0 0 7px #00eaff,
        0 0 18px rgba(0,234,255,0.5);

}


/* Buttons */

.buttons {

    display: grid;

    grid-template-columns: repeat(4, 1fr);

    gap: 11px;

}


button {

    height: 67px;

    border: none;

    border-radius: 16px;

    background:
        linear-gradient(
            145deg,
            #1c2029,
            #0d1016
        );

    color: #dcecff;

    font-size: 20px;

    font-weight: 600;

    cursor: pointer;

    border: 1px solid rgba(255,255,255,0.06);

    box-shadow:
        0 6px 12px rgba(0,0,0,0.45),
        inset 0 1px 0 rgba(255,255,255,0.04);

    transition:
        transform 0.08s,
        box-shadow 0.15s,
        background 0.15s;

    position: relative;

    overflow: hidden;

}


/* Ripple */

button::after {

    content: "";

    position: absolute;

    width: 10px;

    height: 10px;

    border-radius: 50%;

    background: rgba(255,255,255,0.5);

    transform: scale(0);

    opacity: 0;

    pointer-events: none;

}

button.clicked::after {

    animation: ripple 0.35s ease-out;

}

@keyframes ripple {

    0% {
        transform: scale(0);
        opacity: 0.7;
    }

    100% {
        transform: scale(15);
        opacity: 0;
    }

}


button:hover {

    background:
        linear-gradient(
            145deg,
            #26313d,
            #111822
        );

    box-shadow:
        0 0 12px rgba(0,234,255,0.25),
        0 6px 15px rgba(0,0,0,0.5);

    transform: translateY(-2px);

}

button:active {

    transform:
        translateY(2px)
        scale(0.96);

}


/* Number buttons */

.number {

    color: #ffffff;

}


/* Operators */

.operator {

    color: #00eaff;

    background:
        linear-gradient(
            145deg,
            #102b35,
            #08151b
        );

    border-color:
        rgba(0,234,255,0.25);

}

.operator:hover {

    box-shadow:
        0 0 18px rgba(0,234,255,0.4);

}


/* Equals */

.equals {

    color: white;

    background:
        linear-gradient(
            135deg,
            #0077ff,
            #7a00ff
        );

    box-shadow:
        0 0 15px rgba(0,119,255,0.4),
        0 0 30px rgba(122,0,255,0.25);

}

.equals:hover {

    background:
        linear-gradient(
            135deg,
            #00bfff,
            #9b00ff
        );

    box-shadow:
        0 0 25px rgba(0,234,255,0.6),
        0 0 40px rgba(150,0,255,0.3);

}


/* Clear */

.clear {

    color: #ff5277;

    background:
        linear-gradient(
            145deg,
            #32141e,
            #180b10
        );

    border-color:
        rgba(255,82,119,0.25);

}


/* Backspace */

.back {

    color: #ffb84d;

}


/* Percentage */

.percent {

    color: #bb8cff;

}


/* Zero */

.zero {

    grid-column: span 2;

}


/* History */

.history {

    margin-top: 18px;

    padding-top: 15px;

    border-top:
        1px solid rgba(255,255,255,0.07);

}

.history-title {

    color: #5eeeff;

    font-size: 11px;

    letter-spacing: 3px;

    margin-bottom: 8px;

}

.history-list {

    color: #687581;

    font-size: 13px;

    max-height: 75px;

    overflow-y: auto;

}

.history-item {

    padding: 4px 0;

}


/* Mobile */

@media (max-width: 500px) {

    .calculator {
        padding: 14px;
        border-radius: 22px;
    }

    button {
        height: 58px;
        font-size: 18px;
        border-radius: 13px;
    }

    .display {
        min-height: 105px;
    }

}

</style>

</head>


<body>

<div class="calculator">

    <div class="brand">

        <div class="logo">
            🧮
        </div>

        <div>

            <div class="brand-title">
                NEON CALCULATOR
            </div>

            <div class="brand-subtitle">
                DIGITAL COMPUTATION SYSTEM
            </div>

        </div>

    </div>


    <div class="display">

        <div class="expression" id="expression">
            Ready...
        </div>

        <div class="result" id="result">
            0
        </div>

    </div>


    <div class="buttons">

        <button class="clear" data-value="C">
            C
        </button>

        <button class="back" data-value="BACK">
            ⌫
        </button>

        <button class="percent" data-value="%">
            %
        </button>

        <button class="operator" data-value="/">
            ÷
        </button>


        <button class="number" data-value="7">
            7
        </button>

        <button class="number" data-value="8">
            8
        </button>

        <button class="number" data-value="9">
            9
        </button>

        <button class="operator" data-value="*">
            ×
        </button>


        <button class="number" data-value="4">
            4
        </button>

        <button class="number" data-value="5">
            5
        </button>

        <button class="number" data-value="6">
            6
        </button>

        <button class="operator" data-value="-">
            −
        </button>


        <button class="number" data-value="1">
            1
        </button>

        <button class="number" data-value="2">
            2
        </button>

        <button class="number" data-value="3">
            3
        </button>

        <button class="operator" data-value="+">
            +
        </button>


        <button class="number zero" data-value="0">
            0
        </button>

        <button class="number" data-value=".">
            .
        </button>

        <button class="equals" data-value="=">
            =
        </button>

    </div>


    <div class="history">

        <div class="history-title">
            CALCULATION HISTORY
        </div>

        <div class="history-list" id="history">
            No calculations yet
        </div>

    </div>

</div>


<script>

let current = "";
let expression = "";

const resultDisplay =
    document.getElementById("result");

const expressionDisplay =
    document.getElementById("expression");

const historyDisplay =
    document.getElementById("history");


/* --------------------------------------------------
   SOUND ENGINE
-------------------------------------------------- */

let audioContext = null;


function getAudioContext() {

    if (!audioContext) {

        audioContext =
            new (
                window.AudioContext ||
                window.webkitAudioContext
            )();

    }

    return audioContext;
}


function playClickSound(type = "normal") {

    try {

        const ctx = getAudioContext();

        const oscillator =
            ctx.createOscillator();

        const gain =
            ctx.createGain();

        oscillator.connect(gain);

        gain.connect(ctx.destination);


        if (type === "equals") {

            oscillator.type = "sine";

            oscillator.frequency.setValueAtTime(
                420,
                ctx.currentTime
            );

            oscillator.frequency.exponentialRampToValueAtTime(
                900,
                ctx.currentTime + 0.12
            );

        }

        else if (type === "operator") {

            oscillator.type = "triangle";

            oscillator.frequency.setValueAtTime(
                300,
                ctx.currentTime
            );

            oscillator.frequency.exponentialRampToValueAtTime(
                500,
                ctx.currentTime + 0.07
            );

        }

        else {

            oscillator.type = "sine";

            oscillator.frequency.setValueAtTime(
                650,
                ctx.currentTime
            );

            oscillator.frequency.exponentialRampToValueAtTime(
                350,
                ctx.currentTime + 0.045
            );

        }


        gain.gain.setValueAtTime(
            0.0001,
            ctx.currentTime
        );

        gain.gain.exponentialRampToValueAtTime(
            0.08,
            ctx.currentTime + 0.005
        );

        gain.gain.exponentialRampToValueAtTime(
            0.0001,
            ctx.currentTime + 0.09
        );


        oscillator.start();

        oscillator.stop(
            ctx.currentTime + 0.1
        );

    }

    catch(error) {

        console.log("Audio unavailable");

    }

}


/* --------------------------------------------------
   DISPLAY
-------------------------------------------------- */

function updateDisplay() {

    if (current === "") {

        resultDisplay.innerText = "0";

    }

    else {

        resultDisplay.innerText = current;

    }

    expressionDisplay.innerText =
        expression || "Ready...";

}


/* --------------------------------------------------
   HISTORY
-------------------------------------------------- */

let history = [];


function addHistory(text) {

    history.unshift(text);

    if (history.length > 5) {

        history.pop();

    }

    historyDisplay.innerHTML =
        history
        .map(item =>
            `<div class="history-item">${item}</div>`
        )
        .join("");

}


/* --------------------------------------------------
   CALCULATE
-------------------------------------------------- */

function calculate() {

    if (!current) return;

    try {

        let calculation = current;

        calculation =
            calculation.replace(/%/g, "/100");

        /*
           Only allow calculator characters.
           This prevents arbitrary JavaScript
           from being entered.
        */

        if (!/^[0-9+\-*/().\s]+$/.test(calculation)) {

            throw new Error("Invalid");

        }

        let answer =
            Function(
                '"use strict"; return (' +
                calculation +
                ')'
            )();


        if (!Number.isFinite(answer)) {

            throw new Error("Math error");

        }


        let oldExpression = current;

        let formatted =
            Number.isInteger(answer)
                ? answer.toString()
                : Number(answer.toFixed(10)).toString();


        expression =
            oldExpression + " =";

        current =
            formatted;


        addHistory(
            oldExpression
            .replace(/\*/g, "×")
            .replace(/\//g, "÷")
            + " = "
            + formatted
        );


        playClickSound("equals");

        updateDisplay();

    }

    catch(error) {

        resultDisplay.innerText =
            "ERROR";

        expressionDisplay.innerText =
            "Invalid calculation";

        playClickSound("operator");

        setTimeout(() => {

            current = "";

            expression = "";

            updateDisplay();

        }, 900);

    }

}


/* --------------------------------------------------
   BUTTON PRESS
-------------------------------------------------- */

function press(value, button) {

    button.classList.remove("clicked");

    void button.offsetWidth;

    button.classList.add("clicked");


    /* Clear */

    if (value === "C") {

        current = "";

        expression = "";

        playClickSound();

        updateDisplay();

        return;

    }


    /* Backspace */

    if (value === "BACK") {

        current =
            current.slice(0, -1);

        playClickSound();

        updateDisplay();

        return;

    }


    /* Equals */

    if (value === "=") {

        calculate();

        return;

    }


    /* Percentage */

    if (value === "%") {

        if (current !== "") {

            current += "%";

        }

        playClickSound("operator");

        updateDisplay();

        return;

    }


    /* Operators */

    if (
        value === "+" ||
        value === "-" ||
        value === "*" ||
        value === "/"
    ) {

        if (current === "") {

            return;

        }


        /* Prevent double operators */

        if (/[+\-*/]$/.test(current)) {

            current =
                current.slice(0, -1);

        }


        current += value;

        playClickSound("operator");

        updateDisplay();

        return;

    }


    /* Decimal */

    if (value === ".") {

        let parts =
            current.split(/[+\-*/]/);

        let lastNumber =
            parts[parts.length - 1];


        if (lastNumber.includes(".")) {

            return;

        }

    }


    /* Number */

    current += value;

    playClickSound();

    updateDisplay();

}


/* --------------------------------------------------
   BUTTON EVENTS
-------------------------------------------------- */

document
    .querySelectorAll("button")
    .forEach(button => {

        button.addEventListener(
            "click",
            () => {

                press(
                    button.dataset.value,
                    button
                );

            }
        );

    });


/* --------------------------------------------------
   KEYBOARD SUPPORT
-------------------------------------------------- */

document.addEventListener(
    "keydown",
    function(event) {

        let key =
            event.key;

        let button =
            document.querySelector(
                `button[data-value="${CSS.escape(key)}"]`
            );


        if (
            /^[0-9]$/.test(key) ||
            key === "." ||
            key === "+" ||
            key === "-" ||
            key === "*" ||
            key === "/" ||
            key === "%"
        ) {

            if (button) {

                press(key, button);

            }

            return;

        }


        if (
            key === "Enter" ||
            key === "="
        ) {

            let equals =
                document.querySelector(
                    'button[data-value="="]'
                );

            press("=", equals);

            return;

        }


        if (key === "Backspace") {

            let back =
                document.querySelector(
                    'button[data-value="BACK"]'
                );

            press("BACK", back);

            return;

        }


        if (key === "Escape") {

            let clear =
                document.querySelector(
                    'button[data-value="C"]'
                );

            press("C", clear);

        }

    }
);


/* Initial display */

updateDisplay();

</script>

</body>
</html>
"""


components.html(
    calculator_html,
    height=720,
    scrolling=False
)


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown("""
<div style="
    text-align:center;
    margin-top:15px;
    color:#4d5965;
    font-size:11px;
    letter-spacing:2px;
">
    PRESS THE BUTTONS • USE YOUR KEYBOARD • ENJOY THE SOUND
</div>
""", unsafe_allow_html=True)
import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Grade Calculator",
    page_icon="🎓",
    layout="centered"
)


# ============================================================
# CUSTOM DESIGN
# ============================================================

st.markdown(
    """
    <style>

    /* =========================
       MAIN PAGE
       ========================= */

    .stApp {
        background:
            radial-gradient(
                circle at 50% -10%,
                rgba(124, 77, 255, 0.18),
                transparent 35%
            ),
            #080a0f;
    }

    .block-container {
        max-width: 820px;
        padding-top: 35px;
        padding-bottom: 60px;
    }


    /* =========================
       TITLE
       ========================= */

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 850;
        letter-spacing: -1.5px;

        background: linear-gradient(
            90deg,
            #8b5cf6,
            #ec4899,
            #38bdf8
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        margin-bottom: 3px;
    }

    .subtitle {
        text-align: center;
        color: #858b9b;
        font-size: 15px;
        margin-bottom: 35px;
    }


    /* =========================
       SECTION HEADERS
       ========================= */

    .section-title {
        font-size: 22px;
        font-weight: 750;
        margin-top: 15px;
        margin-bottom: 15px;
        color: #f4f5f7;
    }


    /* =========================
       INPUTS
       ========================= */

    .stTextInput label,
    .stNumberInput label {
        color: #8e95a5 !important;
        font-size: 13px !important;
    }

    .stTextInput input,
    .stNumberInput input {

        background-color: #171a22 !important;

        color: #f4f5f7 !important;

        border: 1px solid #2c303c !important;

        border-radius: 9px !important;

        height: 42px !important;
    }

    .stTextInput input:focus,
    .stNumberInput input:focus {

        border-color: #8b5cf6 !important;

        box-shadow:
            0 0 0 1px #8b5cf6 !important;
    }


    /* =========================
       NORMAL BUTTONS
       ========================= */

    .stButton button {

        border-radius: 9px;

        background-color: #12151c;

        color: #dfe2e8;

        border: 1px solid #303542;

        font-weight: 600;

        min-height: 42px;

        transition: all 0.18s ease;
    }

    .stButton button:hover {

        border-color: #8b5cf6;

        background-color: #191522;

        color: white;

        transform: translateY(-1px);
    }


    /* =========================
       CALCULATE BUTTON
       ========================= */

    div.stButton > button[kind="primary"] {

        background:
            linear-gradient(
                100deg,
                #7c3aed,
                #db2777
            );

        border: none;

        color: white;

        font-size: 15px;

        font-weight: 750;

        min-height: 48px;

        box-shadow:
            0 8px 25px
            rgba(124, 58, 237, 0.20);
    }

    div.stButton > button[kind="primary"]:hover {

        background:
            linear-gradient(
                100deg,
                #8b5cf6,
                #ec4899
            );

        box-shadow:
            0 10px 30px
            rgba(236, 72, 153, 0.22);
    }


    /* =========================
       METRIC CARDS
       ========================= */

    [data-testid="stMetric"] {

        background:
            linear-gradient(
                145deg,
                #151821,
                #101219
            );

        border:
            1px solid #292e3a;

        border-radius: 13px;

        padding:
            15px 14px;

        min-height: 92px;

        box-shadow:
            0 8px 25px
            rgba(0,0,0,0.18);
    }

    [data-testid="stMetricLabel"] {

        color: #858b9b !important;

        font-size: 12px !important;
    }

    [data-testid="stMetricValue"] {

        color: #f5f6f8 !important;

        font-size: 25px !important;

        font-weight: 750 !important;
    }


    /* =========================
       OVERALL GRADE
       ========================= */

    .grade-container {

        text-align: center;

        background:
            radial-gradient(
                circle at center,
                rgba(236, 72, 153, 0.09),
                transparent 65%
            );

        border:
            1px solid #343946;

        border-radius: 16px;

        padding:
            20px;

        margin-top: 18px;
        margin-bottom: 18px;
    }

    .grade-label {

        color: #858b9b;

        font-size: 13px;
    }

    .grade-number {

        font-size: 62px;

        line-height: 1.05;

        font-weight: 900;

        background:
            linear-gradient(
                135deg,
                #a78bfa,
                #f472b6
            );

        -webkit-background-clip: text;

        -webkit-text-fill-color: transparent;
    }

    .grade-average {

        color: #858b9b;

        font-size: 14px;
    }


    /* =========================
       SUBJECT RESULT
       ========================= */

    .subject-result-box {

        background-color: #11141b;

        border:
            1px solid #282d38;

        border-radius: 10px;

        padding:
            11px 15px;

        margin-bottom: 7px;
    }


    /* =========================
       DIVIDER
       ========================= */

    hr {

        border-color: #252a34;

        margin:
            28px 0;
    }


    /* =========================
       MOBILE
       ========================= */

    @media (max-width: 700px) {

        .block-container {
            padding-left: 18px;
            padding-right: 18px;
        }

        .main-title {
            font-size: 34px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_grade(percentage):

    if percentage >= 90:
        return "A+"

    if percentage >= 85:
        return "A"

    if percentage >= 80:
        return "A-"

    if percentage >= 75:
        return "B+"

    if percentage >= 70:
        return "B"

    if percentage >= 65:
        return "B-"

    if percentage >= 60:
        return "C+"

    if percentage >= 55:
        return "C"

    if percentage >= 50:
        return "C-"

    if percentage >= 45:
        return "D"

    return "F"


def get_gpa(percentage):

    if percentage >= 90:
        return 4.0

    if percentage >= 85:
        return 3.9

    if percentage >= 80:
        return 3.7

    if percentage >= 75:
        return 3.3

    if percentage >= 70:
        return 3.0

    if percentage >= 65:
        return 2.7

    if percentage >= 60:
        return 2.3

    if percentage >= 55:
        return 2.0

    if percentage >= 50:
        return 1.7

    if percentage >= 45:
        return 1.0

    return 0.0


def format_number(number):

    # 85.0 -> 85
    # 85.50 -> 85.5
    # 85.67 -> 85.67

    if number == int(number):
        return str(int(number))

    return f"{number:.2f}".rstrip("0").rstrip(".")


# ============================================================
# TITLE
# ============================================================

st.markdown(
    '<div class="main-title">🎓 Grade Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Calculate your marks, percentage, grade and GPA'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "subjects" not in st.session_state:

    st.session_state.subjects = [
        {
            "name": "Mathematics",
            "marks": 0.0
        },
        {
            "name": "Science",
            "marks": 0.0
        },
        {
            "name": "English",
            "marks": 0.0
        }
    ]


if "results" not in st.session_state:

    st.session_state.results = None


# ============================================================
# SUBJECT HEADER
# ============================================================

st.markdown(
    '<div class="section-title">📚 Your Subjects</div>',
    unsafe_allow_html=True
)


# ============================================================
# SUBJECT INPUTS
# ============================================================

for i in range(
    len(st.session_state.subjects)
):

    # Much tighter column proportions.
    #
    # Before:
    # subject ----------- marks -------- delete
    #
    # Now:
    # subject ---------------- marks -- x

    col_subject, col_marks, col_delete = st.columns(
        [5.4, 2.1, 0.55],
        gap="small"
    )


    # -------------------------
    # SUBJECT NAME
    # -------------------------

    with col_subject:

        st.text_input(
            "Subject",
            value=st.session_state.subjects[i]["name"],
            key=f"subject_name_{i}"
        )


    # -------------------------
    # MARKS
    # -------------------------

    with col_marks:

        st.number_input(
            "Marks",
            min_value=0.0,
            max_value=100.0,
            value=float(
                st.session_state.subjects[i]["marks"]
            ),
            step=0.5,
            key=f"subject_marks_{i}"
        )


    # -------------------------
    # DELETE
    # -------------------------

    with col_delete:

        st.write("")

        if st.button(
            "×",
            key=f"delete_subject_{i}",
            help="Remove subject"
        ):

            if len(
                st.session_state.subjects
            ) > 1:

                st.session_state.subjects.pop(i)

                st.session_state.results = None

                st.rerun()

            else:

                st.warning(
                    "You need at least one subject."
                )


# ============================================================
# UPDATE SUBJECT DATA
# ============================================================

for i in range(
    len(st.session_state.subjects)
):

    st.session_state.subjects[i]["name"] = (
        st.session_state.get(
            f"subject_name_{i}",
            st.session_state.subjects[i]["name"]
        )
    )

    st.session_state.subjects[i]["marks"] = (
        st.session_state.get(
            f"subject_marks_{i}",
            st.session_state.subjects[i]["marks"]
        )
    )


# ============================================================
# ADD / RESET
# ============================================================

col_add, col_reset = st.columns(
    2,
    gap="small"
)


with col_add:

    if st.button(
        "＋ Add Subject",
        use_container_width=True
    ):

        new_subject_number = (
            len(st.session_state.subjects) + 1
        )

        st.session_state.subjects.append(
            {
                "name":
                    f"Subject {new_subject_number}",

                "marks":
                    0.0
            }
        )

        st.session_state.results = None

        st.rerun()


with col_reset:

    if st.button(
        "↻ Reset",
        use_container_width=True
    ):

        st.session_state.subjects = [
            {
                "name": "Mathematics",
                "marks": 0.0
            },
            {
                "name": "Science",
                "marks": 0.0
            },
            {
                "name": "English",
                "marks": 0.0
            }
        ]

        st.session_state.results = None

        st.rerun()


# ============================================================
# CALCULATE BUTTON
# ============================================================

st.write("")

calculate = st.button(
    "⚡ Calculate My Grade",
    type="primary",
    use_container_width=True
)


# ============================================================
# CALCULATE
# ============================================================

if calculate:

    subjects = []

    total_marks = 0.0


    for i in range(
        len(st.session_state.subjects)
    ):

        name = st.session_state.get(
            f"subject_name_{i}",
            ""
        )

        marks = st.session_state.get(
            f"subject_marks_{i}",
            0.0
        )


        # -------------------------
        # CLEAN NAME
        # -------------------------

        name = str(name).strip()

        if name == "":
            name = f"Subject {i + 1}"


        # -------------------------
        # CLEAN MARKS
        # -------------------------

        marks = float(marks)

        marks = max(
            0.0,
            min(
                100.0,
                marks
            )
        )


        subjects.append(
            {
                "name": name,
                "marks": marks
            }
        )


        total_marks += marks


    # ========================================================
    # TOTAL
    # ========================================================

    total_possible = (
        len(subjects) * 100
    )


    # ========================================================
    # PERCENTAGE
    # ========================================================

    if total_possible > 0:

        percentage = (
            total_marks
            /
            total_possible
        ) * 100

    else:

        percentage = 0.0


    # ========================================================
    # GRADE
    # ========================================================

    grade = get_grade(
        percentage
    )


    # ========================================================
    # GPA
    # ========================================================

    gpa = get_gpa(
        percentage
    )


    # ========================================================
    # SAVE
    # ========================================================

    st.session_state.results = {

        "subjects":
            subjects,

        "total":
            total_marks,

        "possible":
            total_possible,

        "percentage":
            percentage,

        "grade":
            grade,

        "gpa":
            gpa
    }


# ============================================================
# RESULTS
# ============================================================

if st.session_state.results is not None:

    result = st.session_state.results


    # ========================================================
    # DIVIDER
    # ========================================================

    st.divider()


    # ========================================================
    # RESULTS TITLE
    # ========================================================

    st.markdown(
        '<div class="section-title">📊 Your Results</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # RESULT CARDS
    # ========================================================

    col1, col2, col3 = st.columns(
        3,
        gap="small"
    )


    # --------------------------------------------------------
    # TOTAL MARKS
    # --------------------------------------------------------

    with col1:

        st.metric(
            "Total Marks",
            (
                f'{format_number(result["total"])}'
                f'/{result["possible"]}'
            )
        )


    # --------------------------------------------------------
    # PERCENTAGE
    # --------------------------------------------------------

    with col2:

        st.metric(
            "Percentage",
            (
                f'{format_number(result["percentage"])}%'
            )
        )


    # --------------------------------------------------------
    # GPA
    # --------------------------------------------------------

    with col3:

        st.metric(
            "GPA",
            f'{result["gpa"]:.2f}/4.0'
        )


    # ========================================================
    # OVERALL GRADE
    # ========================================================

    st.markdown(
        '<div class="grade-container">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="grade-label">'
        'Overall Grade'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="grade-number">'
        f'{result["grade"]}'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="grade-average">'
        f'Average: {format_number(result["percentage"])}%'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # PERFORMANCE BAR
    # ========================================================

    progress = (
        result["percentage"] / 100
    )

    progress = max(
        0.0,
        min(
            1.0,
            progress
        )
    )

    st.progress(
        progress,
        text=(
            "Overall Performance • "
            f'{format_number(result["percentage"])}%'
        )
    )


    # ========================================================
    # SUBJECT RESULTS
    # ========================================================

    st.markdown(
        '<div class="section-title">'
        '📚 Subject Results'
        '</div>',
        unsafe_allow_html=True
    )


    for subject in result["subjects"]:

        marks = subject["marks"]

        subject_grade = get_grade(
            marks
        )


        col_name, col_result = st.columns(
            [5, 2],
            gap="small"
        )


        with col_name:

            st.markdown(
                '<div class="subject-result-box">',
                unsafe_allow_html=True
            )

            st.write(
                f'**{subject["name"]}**'
            )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )


        with col_result:

            st.markdown(
                '<div class="subject-result-box">',
                unsafe_allow_html=True
            )

            st.write(
                f'**{format_number(marks)}/100 '
                f'· {subject_grade}**'
            )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )
import random
import streamlit as st

# ----------------------------------------------------------------------
# Page setup
# ----------------------------------------------------------------------
st.set_page_config(page_title="Quiz Master", page_icon="🧠", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&display=swap');

html, body, .stApp, .stMarkdown, p, div, span, label {
    font-family: 'VT323', monospace !important;
    font-size: 22px;
}

.stApp {
    background-color: #000000 !important;
}

.main-title, h1, h2, h3, h4 {
    font-family: 'Press Start 2P', monospace !important;
    color: #FFFFFF !important;
}

.main-title {
    text-align: center;
    font-size: 1.7rem;
    letter-spacing: 2px;
    margin-bottom: 0.4rem;
}

.subtitle {
    text-align: center;
    color: #AAAAAA !important;
    font-size: 1.3rem;
    margin-bottom: 2rem;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #0D0D0D !important;
    border: 2px solid #FFFFFF !important;
    border-radius: 4px !important;
}

.result-box {
    font-family: 'VT323', monospace !important;
    font-size: 1.2rem !important;
    padding: 1rem;
    border: 2px solid #FFFFFF;
    border-radius: 4px;
    margin-bottom: 0.6rem;
    color: #FFFFFF !important;
    line-height: 1.5;
}
.result-box.wrong {
    border-style: dashed;
    color: #CCCCCC !important;
}

.stButton > button,
button[kind="primary"], button[kind="secondary"],
[data-testid="stBaseButton-primary"], [data-testid="stBaseButton-secondary"] {
    font-family: 'Press Start 2P', monospace !important;
    font-size: 0.65rem !important;
    border-radius: 2px !important;
    background-color: #000000 !important;
    color: #FFFFFF !important;
    border: 2px solid #FFFFFF !important;
    padding: 0.7rem !important;
}
.stButton > button:hover,
button[kind="primary"]:hover, button[kind="secondary"]:hover,
[data-testid="stBaseButton-primary"]:hover, [data-testid="stBaseButton-secondary"]:hover {
    background-color: #FFFFFF !important;
    color: #000000 !important;
}
button[kind="primary"], [data-testid="stBaseButton-primary"] {
    background-color: #FFFFFF !important;
    color: #000000 !important;
}
button[kind="primary"]:hover, [data-testid="stBaseButton-primary"]:hover {
    background-color: #CCCCCC !important;
    color: #000000 !important;
}

div[data-testid="stMetricValue"] {
    font-family: 'Press Start 2P', monospace !important;
    color: #FFFFFF !important;
    font-size: 1.4rem !important;
}
div[data-testid="stMetricLabel"] {
    font-family: 'VT323', monospace !important;
    color: #AAAAAA !important;
}
.choice-dot {
    font-size: 0.95rem;
    font-weight: 600;
    margin-bottom: -0.6rem;
    color: #FFFFFF !important;
    font-family: 'VT323', monospace !important;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# Easy basic-programming question bank (used to pre-fill new question slots)
# ----------------------------------------------------------------------
QUESTION_BANK = [
    {"question": "Which symbol is used to write a comment in Python?",
     "choices": ["//", "<!-- -->", "#", "**"], "answer": "C"},
    {"question": "Which line correctly creates a variable named age with value 10?",
     "choices": ["age = 10", "var age = 10", "int age = 10;", "10 = age"], "answer": "A"},
    {"question": 'What does print("Hello") do?',
     "choices": ["Nothing", "Shows an error", "Displays the text Hello", "Creates a variable"], "answer": "C"},
    {"question": "Which of these is a whole number (integer)?",
     "choices": ['"5"', "5.0", "5", "True"], "answer": "C"},
    {"question": "Which symbol is used for addition in most languages?",
     "choices": ["+", "&", "-", "%"], "answer": "A"},
    {"question": "Which type of loop repeats code a set number of times?",
     "choices": ["if statement", "for loop", "function", "variable"], "answer": "B"},
    {"question": "What is the file extension for a Python script?",
     "choices": [".py", ".exe", ".txt", ".java"], "answer": "A"},
    {"question": "Which of these stores a list of items, like [1, 2, 3]?",
     "choices": ["String", "List", "Boolean", "Integer"], "answer": "B"},
    {"question": 'What does an "if" statement do?',
     "choices": ["Repeats code forever", "Makes a decision based on a condition",
                 "Stores a number", "Prints text"], "answer": "B"},
    {"question": "A value that is either True or False is called a...",
     "choices": ["String", "Boolean", "Float", "Array"], "answer": "B"},
    {"question": 'Joining "Hello" and "World" into one text is called...',
     "choices": ["Subtraction", "Concatenation", "Division", "Looping"], "answer": "B"},
    {"question": "Which symbol ends a line of code in languages like Java or C++?",
     "choices": [".", ",", ";", ":"], "answer": "C"},
    {"question": "What do we call mistakes in code that stop it from working?",
     "choices": ["Features", "Bugs", "Functions", "Variables"], "answer": "B"},
    {"question": "Which of these is a text (string) data type example?",
     "choices": ["5", "True", '"hello"', "5.5"], "answer": "C"},
    {"question": "What does a function let you do?",
     "choices": ["Store a single number", "Reuse a block of code", "Draw a picture", "Delete files"], "answer": "B"},
]

CHOICE_KEYS = ["a", "b", "c", "d"]


# ----------------------------------------------------------------------
# Callbacks (all session_state mutations happen here, BEFORE widgets
# with the same keys are re-created on the next run)
# ----------------------------------------------------------------------
def init_question_slot(i):
    rq = random.choice(QUESTION_BANK)
    st.session_state[f"q_{i}"] = rq["question"]
    for key, val in zip(CHOICE_KEYS, rq["choices"]):
        st.session_state[f"{key}_{i}"] = val
    st.session_state[f"correct_{i}"] = rq["answer"]


def add_question():
    i = st.session_state.num_questions
    init_question_slot(i)
    st.session_state.num_questions += 1


def remove_last_question():
    if st.session_state.num_questions > 1:
        i = st.session_state.num_questions - 1
        for prefix in ["q", "a", "b", "c", "d", "correct"]:
            st.session_state.pop(f"{prefix}_{i}", None)
        st.session_state.num_questions -= 1


def reroll_question(i):
    init_question_slot(i)


def start_quiz():
    questions = []
    all_filled = True
    for i in range(st.session_state.num_questions):
        q_text = st.session_state.get(f"q_{i}", "")
        a = st.session_state.get(f"a_{i}", "")
        b = st.session_state.get(f"b_{i}", "")
        c = st.session_state.get(f"c_{i}", "")
        d = st.session_state.get(f"d_{i}", "")
        correct = st.session_state.get(f"correct_{i}", "A")
        if not (q_text and a and b and c and d):
            all_filled = False
        questions.append({
            "question": q_text,
            "choices": {"A": a, "B": b, "C": c, "D": d},
            "correct": correct,
        })

    if not all_filled:
        st.session_state.setup_warning = True
        return

    st.session_state.setup_warning = False
    st.session_state.quiz_questions = questions
    st.session_state.quiz_started = True
    st.session_state.user_answers = {}
    st.session_state.submitted = False


def back_to_setup():
    st.session_state.quiz_started = False
    st.session_state.submitted = False


def retry_same_quiz():
    st.session_state.user_answers = {}
    st.session_state.submitted = False


# ----------------------------------------------------------------------
# Session state defaults
# ----------------------------------------------------------------------
st.session_state.setdefault("quiz_started", False)
st.session_state.setdefault("submitted", False)
st.session_state.setdefault("setup_warning", False)
st.session_state.setdefault("quiz_questions", [])
st.session_state.setdefault("user_answers", {})

if "num_questions" not in st.session_state:
    st.session_state.num_questions = 3
    for _i in range(3):
        init_question_slot(_i)

# ----------------------------------------------------------------------
# Header
# ----------------------------------------------------------------------
st.markdown('<div class="main-title">🧠 QUIZ MASTER</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Create your own quiz and challenge yourself!</div>', unsafe_allow_html=True)

# ========================================================================
# PHASE 0 — SETUP / BUILDER (editable, can add or remove questions)
# ========================================================================
if not st.session_state.quiz_started:

    add_col, remove_col = st.columns(2)
    with add_col:
        st.button("➕ ADD QUESTION", use_container_width=True, on_click=add_question)
    with remove_col:
        st.button("➖ REMOVE LAST", use_container_width=True, on_click=remove_last_question)

    st.write("")

    for i in range(st.session_state.num_questions):
        with st.container(border=True):
            head_col, rand_col = st.columns([5, 1])
            with head_col:
                st.markdown(f"#### 📝 Question {i + 1}")
            with rand_col:
                st.button("🎲", key=f"rand_{i}", on_click=reroll_question, args=(i,),
                          help="Fill with a random basic-programming question")

            st.text_input("Question", key=f"q_{i}", placeholder="Example: What is the capital of France?")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<p class="choice-dot">🔵 Choice A</p>', unsafe_allow_html=True)
                st.text_input("Choice A", key=f"a_{i}", placeholder="Enter choice A", label_visibility="collapsed")
                st.markdown('<p class="choice-dot">🟢 Choice C</p>', unsafe_allow_html=True)
                st.text_input("Choice C", key=f"c_{i}", placeholder="Enter choice C", label_visibility="collapsed")
            with col2:
                st.markdown('<p class="choice-dot">🟡 Choice B</p>', unsafe_allow_html=True)
                st.text_input("Choice B", key=f"b_{i}", placeholder="Enter choice B", label_visibility="collapsed")
                st.markdown('<p class="choice-dot">🔴 Choice D</p>', unsafe_allow_html=True)
                st.text_input("Choice D", key=f"d_{i}", placeholder="Enter choice D", label_visibility="collapsed")

            st.radio("Correct answer", ["A", "B", "C", "D"], key=f"correct_{i}", horizontal=True)

    st.write("")
    st.button("🚀 START QUIZ", use_container_width=True, type="primary", on_click=start_quiz)

    if st.session_state.setup_warning:
        st.warning("⚠️ Please fill in every question and all four choices.")

# ========================================================================
# PHASE 1 — TAKE THE QUIZ
# ========================================================================
elif not st.session_state.submitted:

    for i, q in enumerate(st.session_state.quiz_questions):
        with st.container(border=True):
            st.markdown(f"**Q{i + 1}. {q['question']}**")
            options = [f"{k}. {v}" for k, v in q["choices"].items()]
            picked = st.radio("choose", options, key=f"ans_{i}", label_visibility="collapsed")
            st.session_state.user_answers[i] = picked[0]

    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ SUBMIT", use_container_width=True, type="primary"):
            st.session_state.submitted = True
            st.rerun()
    with col2:
        st.button("✏️ BACK TO SETUP", use_container_width=True, on_click=back_to_setup)

# ========================================================================
# PHASE 2 — RESULTS
# ========================================================================
else:
    score = 0
    total = len(st.session_state.quiz_questions)

    for i, q in enumerate(st.session_state.quiz_questions):
        user_letter = st.session_state.user_answers.get(i)
        correct_letter = q["correct"]
        is_correct = user_letter == correct_letter
        if is_correct:
            score += 1

        if is_correct:
            st.markdown(
                f'<div class="result-box">✅ Q{i + 1}. {q["question"]}<br><br>'
                f'Your answer: {user_letter}. {q["choices"][user_letter]} — Correct!</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="result-box wrong">❌ Q{i + 1}. {q["question"]}<br><br>'
                f'Your answer: {user_letter}. {q["choices"][user_letter]}<br>'
                f'Correct answer: {correct_letter}. {q["choices"][correct_letter]}</div>',
                unsafe_allow_html=True,
            )

    st.write("")
    m1, m2 = st.columns(2)
    m1.metric("SCORE", f"{score} / {total}")
    m2.metric("PERCENT", f"{(score / total) * 100:.0f}%" if total else "0%")

    if total and score == total:
        st.balloons()

    col1, col2 = st.columns(2)
    with col1:
        st.button("🔁 RETRY SAME QUIZ", use_container_width=True, type="primary", on_click=retry_same_quiz)
    with col2:
        st.button("✏️ EDIT / NEW QUIZ", use_container_width=True, on_click=back_to_setup)