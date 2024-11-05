// Fetch all flavors and display them
async function fetchFlavors() {
    const response = await fetch('/flavors');
    const flavors = await response.json();
    const flavorList = document.getElementById('flavors');
    flavorList.innerHTML = ''; // Clear the list before repopulating

    flavors.forEach(flavor => {
        const li = document.createElement('li');
        li.textContent = flavor.name;

        // Create delete button
        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.onclick = () => deleteFlavor(flavor.id);

        li.appendChild(deleteButton);
        flavorList.appendChild(li);
    });
}

// Add a new flavor
document.getElementById('flavor-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const flavorName = document.getElementById('flavor-name').value;

    const response = await fetch('/flavors', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: flavorName })
    });

    if (response.ok) {
        document.getElementById('flavor-name').value = '';
        fetchFlavors(); // Refresh the list
    } else {
        alert('Error adding flavor');
    }
});

// Delete a flavor
async function deleteFlavor(id) {
    const response = await fetch(`/flavors/${id}`, {
        method: 'DELETE'
    });

    if (response.ok) {
        fetchFlavors(); // Refresh the list
    } else {
        alert('Error deleting flavor');
    }
}

// Initial fetch of flavors on page load
fetchFlavors();
