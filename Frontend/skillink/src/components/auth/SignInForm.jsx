import React, { useState } from 'react';

const SignInForm = ({ onSignInSuccess }) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        // Check for preview credentials
        if (username === 'user' && password === 'pass') {
            onSignInSuccess();
        } else {
            setError('Invalid credentials. Please try again.');
        }
    };

    return (
        <form className="space-y-6" onSubmit={handleSubmit}>
            <h2 className="text-3xl font-bold text-center text-white mb-8">Welcome Back</h2>
            {error && <p className="text-red-500 text-center">{error}</p>}
            <div className="relative">
                <input
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    className="w-full p-3 bg-gray-700/50 text-white border-2 border-transparent rounded-lg focus:outline-none focus:border-purple-500 transition-all"
                    placeholder="Username"
                />
            </div>
            <div className="relative">
                <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Password"
                    className="w-full p-3 bg-gray-700/50 text-white border-2 border-transparent rounded-lg focus:outline-none focus:border-purple-500 transition-all"
                />
            </div>
            <button type="submit" className="w-full cyber-button p-3 rounded-lg font-bold text-lg">Sign In</button>
        </form>
    );
};
export default SignInForm;