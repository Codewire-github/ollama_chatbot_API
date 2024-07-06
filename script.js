const chatOutput = document.querySelector(".chat-output");
const userInput = document.querySelector("#user-input");
const sendBtn = document.querySelector("#send-btn");
const chatForm = document.querySelector("#chat-form");

chatForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  if (userInput.value.trim() === "") return;

  // Disable the send button to prevent multiple submissions
  sendBtn.disabled = true;

  const data = {
    model: "llama3",
    prompt: `Give answer in html format for heading, bold, list and all, dont include ** for given prompt: ${userInput.value}`,
  };

  try {
    const response = await axios.post(
      "http://localhost:8000/chat/llama3",
      data,
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );

    const answer = response.data.data.response; // Ensure this matches your backend response structure

    chatOutput.innerHTML += `<p class="rich-text"><b>You:</b> ${userInput.value}</p>`;
    chatOutput.innerHTML += `<div class="rich-text">${answer}</div>`;

    userInput.value = ""; // clear the input field

    // Re-enable the send button after receiving the response
    sendBtn.disabled = false;
  } catch (error) {
    console.error(error);
    alert("Error sending request. Please try again.");

    // Re-enable the send button if there's an error
    sendBtn.disabled = false;
  }
});
