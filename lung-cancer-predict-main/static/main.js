const predictionForm = document.getElementById("prediction-form");
const resultDiv = document.getElementById("result-div");

predictionForm.addEventListener("submit", function (event) {
  event.preventDefault();

  const gender = document.getElementById("gender-input").value;
  const age = document.getElementById("age-input").value;
  const smoking = document.getElementById("smoking-input").value;
  const yellowFinger = document.getElementById("yellow-finger-input").value;
  const anxiety = document.getElementById("anxiety-input").value;
  const peer = document.getElementById("peer-input").value;
  const chronic = document.getElementById("chronic-input").value;
  const fatigue = document.getElementById("fatigue-input").value;
  const allergy = document.getElementById("allergy-input").value;
  const wheezing = document.getElementById("wheezing-input").value;
  const alcohol = document.getElementById("alcohol-input").value;
  const coughing = document.getElementById("coughing-input").value;
  const breath = document.getElementById("breath-input").value;
  const swallow = document.getElementById("swallow-input").value;
  const chest = document.getElementById("chest-input").value;

  const data = {
    GENDER: gender,
    AGE: age,
    SMOKING: smoking,
    YELLOW_FINGERS: yellowFinger,
    ANXIETY: anxiety,
    PEER_PRESSURE: peer,
    CHRONIC_DISEASE: chronic,
    FATIGUE: fatigue,
    ALLERGY: allergy,
    WHEEZING: wheezing,
    ALCOHOL_CONSUMPTION: alcohol,
    COUGHING: coughing,
    SHORTNESS_OF_BREATH: breath,
    SWALLOWING_DIFFICULTY: swallow,
    CHEST_PAIN: chest,
  };

  fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((result) => {
      const message = result.message;
      resultDiv.textContent = message;
    });
});
