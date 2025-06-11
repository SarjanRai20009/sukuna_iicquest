// src/pages/ForumsPage.jsx
import React from 'react';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer';
import { Link } from 'react-router-dom';

const ForumsPage = () => {
    // Mock Data for Forum Topics/Groups
    const forumTopics = [
        {
            id: 1,
            title: 'Discussion: Future of AI in Development',
            author: 'Jane Doe',
            replies: 15,
            last_activity: '2 hours ago',
            tags: ['AI', 'Development', 'Tech']
        },
        {
            id: 2,
            title: 'Project Ideas for Junior Developers',
            author: 'John Smith',
            replies: 22,
            last_activity: '1 day ago',
            tags: ['Beginner', 'Projects', 'Learning']
        },
        {
            id: 3,
            title: 'Looking for a UI/UX Collaboration Partner',
            author: 'Alice Johnson',
            replies: 8,
            last_activity: '5 hours ago',
            tags: ['UI/UX', 'Collaboration', 'Design']
        },
        {
            id: 4,
            title: 'Frontend Frameworks: React vs. Vue vs. Angular',
            author: 'Bob Williams',
            replies: 30,
            last_activity: '3 days ago',
            tags: ['Frontend', 'React', 'Vue', 'Angular']
        }
    ];

    return (
        <div className="min-h-screen flex flex-col">
            <Navbar />
            <main className="flex-grow px-4 py-24 sm:py-32">
                <div className="text-center max-w-4xl mx-auto">
                    <h1 className="text-4xl sm:text-6xl font-bold mb-6 holographic">Community Forums</h1>
                    <p className="text-lg text-gray-300 leading-relaxed mb-12">
                        Connect with peers, discuss ideas, and collaborate on projects.
                    </p>
                </div>

                <div className="max-w-6xl mx-auto glass-morphism p-6 rounded-lg">
                    <div className="flex justify-between items-center mb-6 border-b border-gray-700 pb-4">
                        <h2 className="text-2xl font-bold text-white">Popular Topics</h2>
                        <Link to="#" className="cyber-button px-4 py-2 rounded-full font-medium text-sm">
                            New Topic
                        </Link>
                    </div>

                    <div className="space-y-6">
                        {forumTopics.length > 0 ? (
                            forumTopics.map((topic) => (
                                <div key={topic.id} className="p-4 rounded-lg border border-gray-700 hover:border-purple-500 transition-colors">
                                    <h3 className="text-xl font-semibold text-white mb-2">
                                        <Link to={`/forums/${topic.id}`} className="hover:text-purple-300">{topic.title}</Link>
                                    </h3>
                                    <p className="text-gray-400 text-sm mb-2">
                                        Posted by {topic.author} &bull; {topic.replies} replies &bull; Last activity {topic.last_activity}
                                    </p>
                                    <div className="flex flex-wrap gap-2">
                                        {topic.tags.map(tag => (
                                            <span key={tag} className="px-3 py-1 bg-gray-700 text-gray-300 text-xs rounded-full">
                                                {tag}
                                            </span>
                                        ))}
                                    </div>
                                </div>
                            ))
                        ) : (
                            <p className="text-white text-center">No forum topics available.</p>
                        )}
                    </div>
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default ForumsPage;