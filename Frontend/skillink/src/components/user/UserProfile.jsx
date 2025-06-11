import React, { useState, useEffect } from 'react';
import Navbar from '../layout/Navbar';
import Footer from '../layout/Footer';

const UserProfile = () => {
    const [user, setUser] = useState(null);
    const [rating, setRating] = useState(0);

    useEffect(() => {
        const fetchUserData = () => {
            setTimeout(() => {
                setUser({
                    fullName: "Jane Doe",
                    username: "janedoe",
                    profilePic: "https://i.pravatar.cc/150?u=a042581f4e29026704d",
                    cvUrl: "/path/to/dummy_cv.pdf",
                    interests: ["IT", "Creative Arts", "Marketing"],
                    rating: 4.5
                });
                setRating(4.5); 
            }, 1000);
        };
        fetchUserData();
    }, []);

    if (!user) {
        return <div className="min-h-screen flex items-center justify-center text-white">Loading...</div>;
    }

    return (
        <div className="min-h-screen flex flex-col">
            <Navbar />
            <main className="flex-grow px-4 py-24 sm:py-32">
                <div className="max-w-4xl mx-auto glass-morphism p-8 rounded-lg">
                    <div className="flex flex-col md:flex-row items-center md:items-start gap-8">
                        <img src={user.profilePic} alt="Profile" className="w-40 h-40 rounded-full border-4 border-purple-500" />
                        <div className="text-center md:text-left">
                            <h1 className="text-4xl font-bold text-white">{user.fullName}</h1>
                            <p className="text-xl text-purple-300">@{user.username}</p>
                            <div className="flex items-center justify-center md:justify-start my-4">
                                {[...Array(5)].map((_, i) => (
                                    <svg key={i} className={`h-6 w-6 ${i < Math.floor(rating) ? 'text-yellow-400' : 'text-gray-600'}`} fill="currentColor" viewBox="0 0 24 24">
                                        <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z" />
                                    </svg>
                                ))}
                                <span className="text-white ml-2">{user.rating.toFixed(1)}</span>
                            </div>
                            <div className="mt-6">
                                <h2 className="text-2xl font-semibold text-white mb-2">Interests</h2>
                                <div className="flex flex-wrap gap-2 justify-center md:justify-start">
                                    {user.interests.map(interest => (
                                        <span key={interest} className="bg-gray-700 text-white px-3 py-1 rounded-full text-sm">{interest}</span>
                                    ))}
                                </div>
                            </div>
                            <a href={user.cvUrl} target="_blank" rel="noopener noreferrer" className="inline-block mt-6 cyber-button px-6 py-2 rounded-full font-medium text-sm">View CV</a>
                        </div>
                    </div>
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default UserProfile;