const API_BASE_URL = localStorage.getItem('apiUrl') || (window.location.hostname === 'localhost' ? 'http://localhost:8000' : 'https://william-edition.onrender.com');

function redirectTo(page) {
    window.location.href = page;
}

function getToken() {
    return localStorage.getItem('accessToken');
}

function setToken(token, refreshToken) {
    localStorage.setItem('accessToken', token);
    if (refreshToken) {
        localStorage.setItem('refreshToken', refreshToken);
    }
}

function clearAuth() {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    localStorage.removeItem('user');
}

async function apiCall(endpoint, options = {}) {
    const url = `${API_BASE_URL}${endpoint}`;
    const headers = {
        'Content-Type': 'application/json',
        ...options.headers,
    };

    const token = getToken();
    if (token) {
        headers['Authorization'] = `Bearer ${token}`;
    }

    try {
        const response = await fetch(url, {
            ...options,
            headers,
        });

        if (response.status === 401) {
            clearAuth();
            window.location.href = 'auth.html';
            return null;
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('API Call Error:', error);
        throw error;
    }
}

function isAuthenticated() {
    return !!getToken();
}

function checkAuth(redirectPage = 'auth.html') {
    if (!isAuthenticated()) {
        window.location.href = redirectPage;
        return false;
    }
    return true;
}

function showMessage(message, type = 'success') {
    const container = document.createElement('div');
    container.className = type === 'error' ? 'error-message' : 'success-message';
    container.textContent = message;

    const body = document.body;
    body.insertBefore(container, body.firstChild);

    setTimeout(() => container.remove(), 3000);
}

function getCurrentUser() {
    return JSON.parse(localStorage.getItem('user'));
}

function setCurrentUser(user) {
    localStorage.setItem('user', JSON.stringify(user));
}

document.addEventListener('DOMContentLoaded', () => {
    const token = getToken();
    if (token) {
        const authButtons = document.querySelector('.auth-buttons');
        if (authButtons) {
            authButtons.innerHTML = `
                <button class="btn-outline" onclick="redirectTo('dashboard.html')">My Dashboard</button>
                <button class="btn-outline" onclick="logout()">Logout</button>
            `;
        }
    }
});

async function logout() {
    clearAuth();
    showMessage('Logged out successfully');
    setTimeout(() => window.location.href = 'index.html', 1000);
}
