// src/pages/SignedInLandingPage.jsx
import React, { useEffect, useState } from 'react';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer';

const SignedInLandingPage = () => {
    const [userData, setUserData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchUserProfile = async () => {
            try {
                const token = localStorage.getItem('authToken');
                if (!token) {
                    setError('No authentication token found.');
                    setLoading(false);
                    return;
                }

                // Replace with your actual Django API endpoint for user profile
                // This part is for future backend integration; currently uses mock data concept
                // const response = await fetch('/api/profile/', {
                //     headers: {
                //         'Authorization': `Token ${token}`
                //     }
                // });
                // if (!response.ok) {
                //     throw new Error(`HTTP error! status: ${response.status}`);
                // }
                // const data = await response.json();
                // setUserData(data);

                // --- Mock data for frontend-only demonstration ---
                setUserData({
                    username: 'DemoUser',
                    email: 'demouser@example.com',
                    bio: 'Welcome to your personalized dashboard!'
                });
                // --- End Mock data ---

            } catch (error) {
                console.error('Error fetching user profile:', error);
                setError('Failed to load user profile. Please try again later.');
            } finally {
                setLoading(false);
            }
        };

        fetchUserProfile();
    }, []);

    if (loading) {
        return (
            <div className="min-h-screen flex flex-col">
                <Navbar />
                <main className="flex-grow flex items-center justify-center">
                    <p className="text-white">Loading profile data...</p>
                </main>
                <Footer />
            </div>
        );
    }

    if (error) {
        return (
            <div className="min-h-screen flex flex-col">
                <Navbar />
                <main className="flex-grow flex items-center justify-center">
                    <p className="text-red-500">{error}</p>
                </main>
                <Footer />
            </div>
        );
    }

    return (
        <div className="min-h-screen flex flex-col">
            <Navbar />
            <main className="flex-grow px-4 py-24 sm:py-32">
                <div className="text-center max-w-4xl mx-auto glass-morphism p-8 rounded-lg">
                    <h1 className="text-4xl sm:text-6xl font-bold mb-6 holographic">Welcome, {userData?.username || 'User'}!</h1>
                    <p className="text-lg text-gray-300 leading-relaxed mb-8">
                        This is your personalized dashboard.
                    </p>
                    {userData && (
                        <div className="text-left">
                            <h2 className="text-2xl font-bold text-white mb-4">Your Profile Details:</h2>
                            <p className="text-gray-400"><strong>Email:</strong> {userData.email}</p>
                            <p className="text-gray-400"><strong>Bio:</strong> {userData.bio || 'Not provided'}</p>
                        </div>
                    )}
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default SignedInLandingPage; 