import React from 'react';

const AuthPage = () => {
  const handleGoogleLogin = () => {
    // Redirect to the backend's Google OAuth login endpoint
    window.location.href = '/auth/google';
  };

  const handleLogout = () => {
    // Call the backend API to logout and clear session cookies
    fetch('/auth/logout', {
      method: 'POST',
      credentials: 'include', // Include session cookies
    })
      .then((response) => {
        if (response.ok) {
          window.location.href = '/'; // Redirect to home page after logout
        } else {
          console.error('Logout failed. Please try again.');
        }
      })
      .catch((error) => console.error('Error during logout:', error));
  };

  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', flexDirection: 'column' }}>
      <h1>Login to Chatbot</h1>
      <button onClick={handleGoogleLogin} style={{ padding: '10px 20px', fontSize: '16px', cursor: 'pointer', marginBottom: '10px' }}>
        Login with Google
      </button>
      <button onClick={handleLogout} style={{ padding: '10px 20px', fontSize: '16px', cursor: 'pointer' }}>
        Logout
      </button>
    </div>
  );
};

export default AuthPage;
