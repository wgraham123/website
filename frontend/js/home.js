import { getHello } from "./api.js";
import { waitForAuthReady } from "./firebase.js";

await waitForAuthReady();

document.getElementById("helloBtn").addEventListener("click", async () => {
    const name = document.getElementById("nameInput").value;
    const result = await getHello(name);
    document.getElementById("result").innerText = result;
});
