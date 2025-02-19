const gameContainer = document.querySelector(".container"),
    userResult = document.querySelector(".user_result img"),
    cpuResult = document.querySelector(".cpu_result img"),
    result = document.querySelector(".result"),
    optionImages = document.querySelectorAll(".option_img"); // FIXED

optionImages.forEach((img, index) => {
    img.addEventListener("click", (e) => { // FIXED
        img.classList.add("active");

        // Remove active class from other options
        optionImages.forEach((image2, index2) => {
            if (index !== index2) {
                image2.classList.remove("active");
            }
        });

        // Update user image
        let ImageSrc = e.currentTarget.querySelector("img").src; // FIXED
        userResult.src = ImageSrc;

        // Simple random CPU choice
        const cpuChoices = ["fist.png", "scissors.png", "hand-paper.png"];
        let randomChoice = cpuChoices[Math.floor(Math.random() * cpuChoices.length)];
        cpuResult.src = randomChoice;

        // Simple result logic
        if (
            (ImageSrc.includes("fist") && randomChoice.includes("scissors")) ||
            (ImageSrc.includes("scissors") && randomChoice.includes("hand-paper")) ||
            (ImageSrc.includes("hand-paper") && randomChoice.includes("fist"))
        ) {
            result.textContent = "You Win!";
        } else if (ImageSrc === randomChoice) {
            result.textContent = "It's a Draw!";
        } else {
            result.textContent = "You Lose!";
        }
    });
});
