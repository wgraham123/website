const urlRoot =
    "https://europe-west2-potent-thought-483207-v4.cloudfunctions.net";

export async function getHello(name) {
    const response = await fetch(
        `${urlRoot}/hello-world?name=${encodeURIComponent(name)}`,
        {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        }
    );
    if (!response.ok) {
        throw new Error(
            `API error: ${response.status}: ${response.text()}`
        );
    }
    return response.text();
}
