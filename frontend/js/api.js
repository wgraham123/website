export async function getHello(name) {
    const response = await fetch(`${url}?name=${encodeURIComponent(name)}`, {
        method: 'GET'
    });
    return response.text();
}