import React from 'react';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer';

const AboutPage = () => {
    return (
        <div className="min-h-screen flex flex-col">
            <Navbar />
            <main className="flex-grow px-4 py-24 sm:py-32">
                <div className="text-center max-w-4xl mx-auto">
                    <h1 className="text-4xl sm:text-6xl font-bold mb-6 holographic">About Skillink</h1>
                    <p className="text-lg text-gray-300 leading-relaxed mb-12">
                        We are a passionate team of innovators dedicated to closing the gap between opportunity and talent. Our mission is to create a global ecosystem where skills are the currency, and collaboration knows no bounds.
                    </p>
                </div>
                <div className="max-w-7xl mx-auto grid md:grid-cols-2 gap-12 items-center">
                    <div className="glass-morphism p-8 rounded-lg">
                        <h2 className="text-3xl font-bold text-white mb-4">Our Vision</h2>
                        <p className="text-gray-400">
                            To empower every individual and organization to reach their full potential by providing a transparent, efficient, and intelligent platform for collaboration. We envision a world where the best ideas and the best minds find each other effortlessly.
                        </p>
                    </div>
                    <div className="glass-morphism p-8 rounded-lg">
                        <h2 className="text-3xl font-bold text-white mb-4">Our Story</h2>
                        <p className="text-gray-400">
                            Founded in 2024, Skillink was born from a simple observation: talented individuals struggled to find meaningful work, while companies desperately needed their skills. We built this platform to break down those barriers and foster innovation on a global scale.
                        </p>
                    </div>
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default AboutPage;