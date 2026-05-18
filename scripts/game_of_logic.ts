import * as readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const syllogisms = [
    {
        premise1: "Some fresh cakes are sweet.",
        premise2: "No sweet cakes are healthy.",
        question: "What conclusion can you draw about fresh cakes and being healthy?",
        answerKeywords: ["fresh", "healthy", "not"] // Example: "Some fresh cakes are not healthy."
    },
    {
        premise1: "All cats understand French.",
        premise2: "Some chickens are cats.",
        question: "What conclusion can you draw about chickens and French?",
        answerKeywords: ["some", "chickens", "understand", "french"] // Example: "Some chickens understand French."
    },
    {
        premise1: "No bald creatures need hairbrushes.",
        premise2: "No lizards have hair.",
        question: "Can you draw a conclusion?",
        answerKeywords: ["no", "none", "cannot", "can't", "nothing"] // Fallacy of exclusive premises / no conclusion can be drawn
    }
];

function play() {
    console.log("=========================================");
    console.log("       THE GAME OF LOGIC (CLI)           ");
    console.log("         by Lewis Carroll                ");
    console.log("=========================================\n");
    console.log("Welcome! In this game, you'll be given two premises.");
    console.log("Your task is to improvise and type the correct conclusion.\n");

    let currentSyllogism = 0;

    const askQuestion = () => {
        if (currentSyllogism >= syllogisms.length) {
            console.log("Congratulations! You've completed The Game of Logic!");
            rl.close();
            return;
        }

        const s = syllogisms[currentSyllogism];
        console.log(`\nPremise 1: ${s.premise1}`);
        console.log(`Premise 2: ${s.premise2}`);

        rl.question(`\n${s.question}\nYour conclusion: `, (answer) => {
            const lowerAnswer = answer.toLowerCase();
            const correct = s.answerKeywords.every(kw => lowerAnswer.includes(kw));

            if (correct || (currentSyllogism === 2 && lowerAnswer.includes("no conclusion"))) {
                console.log("Correct!\n");
                currentSyllogism++;
            } else {
                console.log(`\nNot quite. A possible conclusion involves: ${s.answerKeywords.join(", ")}`);
                console.log("Let's try the next one.\n");
                currentSyllogism++;
            }
            askQuestion();
        });
    };

    askQuestion();
}

play();
