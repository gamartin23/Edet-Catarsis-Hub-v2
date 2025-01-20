async function fetchInitialCounters() {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/mcll-get');
        const data = await response.json();
        
        for (const [divId, count] of Object.entries(data)) {
            const counterElement = document.getElementById(`counter-${divId}`);
            if (counterElement) {
                counterElement.textContent = count;
            }
        }
    } catch (error) {
        console.error('Error fetching initial counts:', error);
    }
}

document.addEventListener('DOMContentLoaded', fetchInitialCounters);