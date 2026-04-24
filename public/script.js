const btn = document.getElementById('send-btn');
const msg = document.getElementById('response-msg');

btn.addEventListener('click', async () => {
    btn.disabled = true;
    msg.textContent = 'Loading...';

    try {
        const response = await fetch('https://backend-server-template.vercel.app/api/endpoint', {
            method: 'GET',
        });

        if (!response.ok) throw new Error(`Server error: ${response.status}`);
        const data = await response.json();
        msg.textContent = `Success: ${JSON.stringify(data)}`;
    } catch (error) {
        msg.textContent = `Error: ${error.message}`;
    } finally {
        btn.disabled = false;
    }
});
