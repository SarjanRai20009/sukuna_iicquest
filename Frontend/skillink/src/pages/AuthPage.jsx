// src/pages/AuthPage.jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import SignInForm from '../components/auth/SignInForm';
import SignUpForm from '../components/auth/SignUpForm';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer';

const AuthPage = () => {
    const [isSigningIn, setIsSigningIn] = useState(true);
    const navigate = useNavigate();

    const handleAuthSuccess = () => {
        // Simulate setting a token
        localStorage.setItem('authToken', 'dummy-token');
        // Change this line:
        navigate('/'); // Navigate to the root path (which will be SignedInLandingPage for authenticated users)
    };

    return (
        <div className="min-h-screen bg-black flex flex-col">
            <Navbar />
            <main className="flex-grow flex items-center justify-center pt-24 sm:pt-32">
                <div className="glass-morphism p-8 rounded-lg w-full max-w-md">
                    {isSigningIn ? <SignInForm onSignInSuccess={handleAuthSuccess} /> : <SignUpForm onSignUpSuccess={handleAuthSuccess} />}
                    <button
                        onClick={() => setIsSigningIn(!isSigningIn)}
                        className="mt-4 text-center w-full text-white hover:text-purple-300"
                    >
                        {isSigningIn ? "Don't have an account? Sign Up" : "Already have an account? Sign In"}
                    </button>
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default AuthPage;