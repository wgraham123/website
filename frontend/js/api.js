import { getIdToken } from "./firebase.js";

const urlRoot =
    "https://europe-west2-potent-thought-483207-v4.cloudfunctions.net";

export async function getHello(name) {
    const token = await getIdToken();
    const response = await fetch(
        `${urlRoot}/hello-world?name=${encodeURIComponent(name)}`,
        {
            method: "GET",
            headers: {
                Authorization: `Bearer ${token}`,
                "Content-Type": "application/json"
            }
        }
    );
    if (!response.ok) {
        throw new Error(
            `API error: ${response.status}: ${await response.text()}`
        );
    }
    return response.text();
}
