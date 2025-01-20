(() => {
    const buttons = document.querySelectorAll('.putear-button');
    
    buttons.forEach(button => {
        button.type = 'button';
        button.removeAttribute('formaction');
        button.removeAttribute('form');
        
        button.onclick = async function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            const parentId = this.parentElement.id;
            try {
                const response = await fetch(`http://127.0.0.1:5000/api/mcll-post?${parentId}`, {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json'
                    }
                });
                
                if (response.ok) {
                    const data = await response.json();
                    const counterElement = document.getElementById(`counter-${parentId}`);
                    if (counterElement && data.counter !== undefined) {
                        counterElement.textContent = data.counter;
                    }
                }
            } catch (error) {
                console.error('Error:', error);
            }
            return false;
        };
    });
})();