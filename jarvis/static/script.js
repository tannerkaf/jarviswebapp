var responses = {
    "hello": [
        "Hi there!",
        "Hello!",
        "Greetings!",
        "Hey!",
        "Hi!",
        "Hello, how can I help?",
        "Hey, nice to see you!",
        "Hi, what's up?",
        "Hello, how are you?",
        "Hey, how's it going?",
    ],
    "how are you": [
        "I'm doing well, thank you!",
        "I'm good, how about you?",
        "Everything's running smoothly here!",
        "I'm great, thanks for asking!",
        "Not bad, what about you?",
        "I'm fine, what's up?",
        "I'm doing well, how about yourself?",
        "Pretty good, how are you doing?",
        "All good on this end, thanks!",
        "I'm well, thanks for asking!",
    ],
    "what's your name": [
        "I'm Jarvis, at your service!",
        "I'm Jarvis, your virtual assistant.",
        "Call me Jarvis!",
        "You can call me Jarvis.",
        "I go by the name Jarvis.",
        "The name's Jarvis.",
        "I'm your assistant, Jarvis.",
        "I'm Jarvis, nice to meet you!",
        "Jarvis is the name, assisting is the game.",
        "Just Jarvis here!",
    ],
    // Add more inputs and responses as needed
    // ...
};

function getRandomResponse(input) {
    var inputLowerCase = input.toLowerCase();
    return responses[inputLowerCase] ? responses[inputLowerCase][Math.floor(Math.random() * responses[inputLowerCase].length)] : "I'm not sure how to respond to that.";
}
