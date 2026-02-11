import streamlit as st
import streamlit.components.v1 as components



components.html("""
<!DOCTYPE html>
<html>
<style>

body {
    margin: 0;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, #020617, #020617);
    font-family: Arial, sans-serif;
}

/* Container */
.container {
    text-align: center;
}

/* Title Styling */
.title {
    font-size: 40px;
    font-weight: bold;
    color: white;
    margin-bottom: 30px;
    letter-spacing: 2px;
}

/* Fancy Input Box */
input {
    padding: 15px 20px;
    width: 320px;
    font-size: 18px;
    border-radius: 12px;
    border: 2px solid transparent;
    outline: none;
    background: rgba(255,255,255,0.08);
    color: white;
    backdrop-filter: blur(10px);
    transition: 0.3s ease;
}

/* Glow on focus */
input:focus {
    border-color: #ff69b4;
    box-shadow: 0 0 15px rgba(255,105,180,0.6);
}

/* Output */
#output {
    margin-top: 25px;
    font-size: 42px;
    color: #d946ef;
    letter-spacing: 6px;
}

/* Flower Animation */
.flower {
    position: fixed;
    top: -50px;
    font-size: 30px;
    animation: fall 3s linear forwards;
}

/* Heart rises from bottom */
.love {
    position: fixed;
    bottom: -50px;
    font-size: 30px;
    animation: rise 3s linear forwards;
}


@keyframes fall {
    to {
        transform: translateY(100vh);
        opacity: 0;
    }
}

/* Bottom → Top */
@keyframes rise {
    from {
        transform: translateY(0);
        opacity: 1;
    }
    to {
        transform: translateY(-100vh);
        opacity: 0;
    }
}

</style>

<body>

<div class="container">

<div class="title">🌸'SHE' is a Flower to 'ME'</div>

<input id="inputBox" placeholder="Type Flower to see the magic👀" />

<div id="output"></div>

</div>

<script>

const inputWord = "ANKITA";
const outputWord = "FLOWER";

const inputreverse = "FLOWER";
const outputreverse = "ANKITA";

const inputBox = document.getElementById("inputBox");
const output = document.getElementById("output");

inputBox.addEventListener("input", () => {

    let typed = inputBox.value.toUpperCase();
    let converted = "";

    for (let i = 0; i < typed.length; i++) {
        if (typed[i] === inputWord[i]) {
            converted += outputWord[i];
        }
    }
                
    for (let i = 0; i < typed.length; i++) {
        if (typed[i] === inputreverse[i]) {
            converted += outputreverse[i];
        }
    }

    output.innerHTML = converted;

    if (typed === inputWord || typed === inputreverse ) {

        for (let i = 0; i < 20; i++) {

            let flower = document.createElement("div");
            flower.className = "flower";
            flower.innerHTML = "🌸";
            flower.style.left = Math.random() * 100 + "vw";

            document.body.appendChild(flower);

            setTimeout(() => flower.remove(), 3000);
                let love = document.createElement("div");
            love.className = "love";
            love.innerHTML = "❤️";
            love.style.left = Math.random() * 100 + "vw";

            document.body.appendChild(love);

            setTimeout(() => love.remove(), 3000);
        }
    }
        
    
});

</script>

</body>
</html>
""", height=500)
