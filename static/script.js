async function sendMessage() {
    let userInput = document.getElementById("userInput").value;
    let chatHistory = document.getElementById("chatHistory");

    chatHistory.value += "You: " + userInput + "\n";
    document.getElementById("userInput").value = "";

    try {
        let response = await fetch("http://127.0.0.1:5000/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question: userInput })
        });

        let data = await response.json();
        chatHistory.value += "ATLAS: " + (data.answer || data.error) + "\n";
    } catch (error) {
        chatHistory.value += "ATLAS: Error connecting to server.\n";
    }
}