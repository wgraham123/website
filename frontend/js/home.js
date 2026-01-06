import { getHello } from "./api";

document.getElementById("helloBtn").onClick = async () => {
    const name = document.getElementById("nameInput").value;
    const result = await getHello(name);
    document.getElementById("result").innerText = result;
};