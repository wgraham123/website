const urlRoot = 'https://europe-west2-potent-thought-483207-v4.cloudfunctions.net'

export async function getHello(name) {
    const response = await fetch(`${urlRoot}/hello-world?name=${encodeURIComponent(name)}`, {
        method: 'GET'
    });
    return response.text();
}