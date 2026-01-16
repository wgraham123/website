import { getHello } from "./api.js";

document.getElementById("helloBtn").addEventListener("click", async () => {
    const name = document.getElementById("nameInput").value;
    const result = await getHello(name);
    document.getElementById("result").innerText = result;
});
