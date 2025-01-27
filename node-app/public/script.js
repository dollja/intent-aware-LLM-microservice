async function fetchSessionHistory(userId) {
    const response = await fetch(`/session/${userId}`);
    const sessionHistory = await response.json();

    const sessionDiv = document.getElementById("session-history");
    sessionDiv.innerHTML = "";

    sessionHistory.forEach((entry, index) => {
        const item = document.createElement("div");
        item.innerHTML = `<strong>Turn ${index + 1}:</strong> ${entry.input} → ${entry.output}`;
        sessionDiv.appendChild(item);
    });
}

fetchSessionHistory("user123");