function sendMessage() {

    let input = document.getElementById("user-input")
    let msg = input.value

    fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg })
    })
    .then(res => res.json())
    .then(data => {

        let chat = document.getElementById("chat-box")

        chat.innerHTML += `<p><b>You:</b> ${msg}</p>`
        chat.innerHTML += `<p><b>AI:</b> ${data.reply}</p>`

        input.value = ""
        chat.scrollTop = chat.scrollHeight

    })
    .catch(err => console.error(err))

}