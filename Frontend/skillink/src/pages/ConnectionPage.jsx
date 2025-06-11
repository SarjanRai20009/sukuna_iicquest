import React from 'react';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer';
import { Link } from 'react-router-dom';

const ConnectionPage = () => {
    const posts = [
        {
            author: "John Doe",
            role: "Provider",
            content: "Looking for a React developer with experience in building dynamic user interfaces.",
            profileLink: "/profile"
        },
        {
            author: "Jane Smith",
            role: "Talent",
            content: "I'm a UI/UX designer passionate about creating intuitive and visually appealing applications.",
            profileLink: "/profile"
        }
    ];

    return (
        <div className="min-h-screen flex flex-col">
            <Navbar />
            <main className="flex-grow flex items-center justify-center px-4 py-24 sm:py-32">
                <div className="w-full max-w-4xl">
                    <h1 className="text-4xl sm:text-6xl font-bold text-center mb-12 holographic">Connection Hub</h1>
                    <div className="space-y-8">
                        {posts.map((post, index) => (
                            <div key={index} className="glass-morphism p-6 rounded-lg">
                                <p className="text-gray-300">{post.content}</p>
                                <div className="mt-4 flex justify-between items-center">
                                    <p className="text-purple-300 font-semibold">{post.author} <span className="text-gray-400 font-normal">({post.role})</span></p>
                                    <Link to={post.profileLink} className="cyber-button px-4 py-2 rounded-full font-medium text-sm">
                                        View Profile
                                    </Link>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default ConnectionPage;