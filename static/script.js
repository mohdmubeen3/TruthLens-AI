const detectBtn = document.getElementById("detectBtn");
const clearBtn = document.getElementById("clearBtn");
const exampleBtn = document.getElementById("exampleBtn");
const news = document.getElementById("news");
const loading = document.getElementById("loading");
const result = document.getElementById("result");
const count = document.getElementById("count");

// Character Counter
news.addEventListener("input", () => {
    count.innerText = news.value.length;
});

// Detect News
detectBtn.addEventListener("click", async () => {

    const text = news.value.trim();

    if (text === "") {
        alert("Please enter some news.");
        return;
    }

    loading.style.display = "block";
    result.style.display = "none";

    try {

        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                news: text
            })
        });

        const data = await response.json();

        loading.style.display = "none";
        result.style.display = "block";

        if (!data.success) {
            result.innerHTML = `<h2>${data.message}</h2>`;
            return;
        }

        const isReal = data.prediction === "REAL NEWS";

        result.innerHTML = `
            <span class="badge ${isReal ? "real" : "fake"}">
                ${isReal ? "🟢 REAL NEWS" : "🔴 FAKE NEWS"}
            </span>

            <h2>${data.prediction}</h2>

            <br>

            <p><b>Model Used:</b> Linear SVM</p>

            <br>

            <p><b>Confidence Score</b></p>

            <div class="progress">
                <div class="progress-bar" id="bar"></div>
            </div>

            <br>

            <h3>${data.confidence}%</h3>
        `;

        setTimeout(() => {
            document.getElementById("bar").style.width =
                `${data.confidence}%`;
        }, 100);

    } catch (err) {

        loading.style.display = "none";

        result.style.display = "block";

        result.innerHTML = `
            <h2>Something went wrong.</h2>
        `;
    }

});

// Clear Button
clearBtn.addEventListener("click", () => {

    news.value = "";

    count.innerText = "0";

    result.style.display = "none";

});
exampleBtn.addEventListener("click", () => {

    news.value = `WASHINGTON (Reuters) - The Reserve Bank of India announced new monetary policy measures today. Officials stated that inflation remains under control while economic growth continues to improve. Financial markets responded positively to the announcement.`;

    count.innerText = news.value.length;

});