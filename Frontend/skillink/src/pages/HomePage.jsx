import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer';

const ParticleSystem = () => {
    return <div className="particle-bg"></div>;
};

const HomePage = () => {
    const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });

    useEffect(() => {
        const handleMouseMove = (e) => {
            setMousePosition({ x: e.clientX, y: e.clientY });
        };
        window.addEventListener('mousemove', handleMouseMove);
        return () => window.removeEventListener('mousemove', handleMouseMove);
    }, []);

    return (
        <div className="min-h-screen bg-black overflow-x-hidden">
            <Navbar />
            <section className="aurora-bg min-h-screen flex items-center justify-center relative overflow-hidden">
                <ParticleSystem />
                <div className="absolute inset-0 z-10"></div>
                <div className="relative z-20 text-center text-white px-6 max-w-6xl mx-auto">
                    <h1 className="text-6xl md:text-8xl font-black mb-8 text-glow leading-tight">
                        Where <span className="holographic">Vision</span> Meets <br />
                        <span className="holographic">Expertise</span>
                    </h1>
                    <p className="text-xl md:text-2xl mb-12 text-white/80 max-w-3xl mx-auto leading-relaxed">
                        Our platform empowers providers to find the perfect talents, and helps talents discover impactful projects.
                    </p>
                    <div className="flex justify-center">
                        <Link to="/auth" className="cyber-button px-12 py-5 rounded-full font-bold text-lg neon-glow">
                            🚀 Get Started
                        </Link>
                    </div>
                </div>
                <div className="scroll-indicator"></div>
            </section>
            <Footer />
        </div>
    );
};

export default HomePage;