// src/pages/EventsPage.jsx
import React from 'react';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer';

const EventsPage = () => {
    // Mock Data for Events
    const events = [
        {
            id: 1,
            title: 'Web Dev Conference 2025',
            date: 'July 15-17, 2025',
            location: 'Virtual',
            description: 'A global conference covering the latest in web development technologies and trends.',
            link: '#'
        },
        {
            id: 2,
            title: 'Local Hackathon: Build the Future',
            date: 'August 10-11, 2025',
            location: 'Community Center, Cityville',
            description: 'Join us for a 24-hour hackathon to build innovative solutions to local problems.',
            link: '#'
        },
        {
            id: 3,
            title: 'Design Thinking Workshop',
            date: 'September 5, 2025',
            location: 'Online',
            description: 'An interactive workshop on applying design thinking principles to product development.',
            link: '#'
        },
        {
            id: 4,
            title: 'Startup Pitch Competition',
            date: 'October 20, 2025',
            location: 'Tech Hub Auditorium',
            description: 'Pitch your startup idea to a panel of investors and mentors.',
            link: '#'
        }
    ];

    return (
        <div className="min-h-screen flex flex-col">
            <Navbar />
            <main className="flex-grow px-4 py-24 sm:py-32">
                <div className="text-center max-w-4xl mx-auto">
                    <h1 className="text-4xl sm:text-6xl font-bold mb-6 holographic">Upcoming Events</h1>
                    <p className="text-lg text-gray-300 leading-relaxed mb-12">
                        Stay informed about industry meetups, workshops, and conferences.
                    </p>
                </div>

                <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    {events.length > 0 ? (
                        events.map((event) => (
                            <div key={event.id} className="glass-morphism p-6 rounded-lg flex flex-col justify-between">
                                <div>
                                    <h2 className="text-2xl font-bold text-white mb-2">{event.title}</h2>
                                    <p className="text-purple-300 mb-2">{event.date}</p>
                                    <p className="text-gray-400 text-sm mb-4">{event.location}</p>
                                    <p className="text-gray-300 line-clamp-3 mb-4">{event.description}</p>
                                </div>
                                <button className="cyber-button w-full py-2 rounded-lg font-bold text-sm">
                                    <a href={event.link} target="_blank" rel="noopener noreferrer">Learn More</a>
                                </button>
                            </div>
                        ))
                    ) : (
                        <p className="text-white text-center col-span-full">No events found.</p>
                    )}
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default EventsPage;