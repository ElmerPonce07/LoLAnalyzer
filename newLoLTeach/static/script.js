document.getElementById("send-button").onclick = function () {
  const userInput = document.getElementById("user-input").value;
  if (!userInput) return;


  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<div class="user-message">You: ${userInput}</div>`;
  document.getElementById("user-input").value = "";

  fetch("/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message: userInput }),
  })
    .then((response) => response.json())
    .then((data) => {
      let responseHtml = data.response;

      
      const isList = /^\d+\.\s/.test(responseHtml);

      if (isList) {
        const listItems = responseHtml
          .split("\n")
          .filter((line) => line.trim() !== "");
        responseHtml =
          "<ol>" +
          listItems.map((item) => `<li>${item}</li>`).join("") +
          "</ol>";
      } else {
        responseHtml = responseHtml
          .split("\n")
          .map((line) => `<p>${line}</p>`)
          .join("");
      }

      chatBox.innerHTML += `<div class="oracle-message">${responseHtml}</div>`;
      chatBox.scrollTop = chatBox.scrollHeight; 
    })

    .catch((error) => {
      console.error("Error:", error);
    });
};


document
  .getElementById("user-input")
  .addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
      document.getElementById("send-button").click();
    }
  });
