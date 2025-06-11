// src/components/layout/Navbar.jsx
import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';

const Navbar = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const navigate = useNavigate();

    useEffect(() => {
        // Check authentication status on component mount and when localStorage changes
        const checkAuth = () => {
            setIsAuthenticated(!!localStorage.getItem('authToken'));
        };
        checkAuth(); // Initial check

        // Listen for changes in localStorage (e.g., from sign-in/sign-out)
        window.addEventListener('storage', checkAuth);
        return () => {
            window.removeEventListener('storage', checkAuth);
        };
    }, []);

    const handleSignOut = () => {
        localStorage.removeItem('authToken'); // Remove the dummy token
        setIsAuthenticated(false);
        navigate('/'); // Redirect to home page
    };

    const navLinks = [
        { name: 'Home', path: '/' },
        { name: 'Opportunities', path: '/opportunities' }, // New link
        { name: 'Forums', path: '/forums' },             // New link
        { name: 'Events', path: '/events' },               // New link
        { name: 'About', path: '/about' },
        { name: 'Pricing', path: '/pricing' },
        { name: 'FAQ', path: '/faq' },
        { name: 'Contact', path: '/contact' },
        // Connection page might be better accessed from a user dashboard or specific feature
        // { name: 'Connection', path: '/connection' },
        // Privacy Policy usually in footer, but can be here too if desired
        // { name: 'Privacy Policy', path: '/privacy' },
    ];

    return (
        <nav className="fixed w-full z-50 p-4 transition-all duration-300 backdrop-blur-lg bg-black/70">
            <div className="container mx-auto flex justify-between items-center">
                <Link to="/" className="text-2xl font-bold holographic">
                    Skillink
                </Link>

                {/* Desktop Navigation */}
                <div className="hidden md:flex items-center space-x-6">
                    {navLinks.map((link) => (
                        <Link
                            key={link.name}
                            to={link.path}
                            className="text-white hover:text-purple-300 transition-colors text-lg"
                        >
                            {link.name}
                        </Link>
                    ))}
                    {isAuthenticated ? (
                        <>
                            <Link
                                to="/profile"
                                className="text-white hover:text-purple-300 transition-colors text-lg"
                            >
                                Profile
                            </Link>
                            <button
                                onClick={handleSignOut}
                                className="cyber-button px-6 py-2 rounded-full font-bold text-md"
                            >
                                Sign Out
                            </button>
                        </>
                    ) : (
                        <Link
                            to="/auth"
                            className="cyber-button px-6 py-2 rounded-full font-bold text-md"
                        >
                            Sign In
                        </Link>
                    )}
                </div>

                {/* Mobile Menu Button */}
                <div className="md:hidden">
                    <button onClick={() => setIsOpen(!isOpen)} className="text-white text-3xl focus:outline-none">
                        ☰
                    </button>
                </div>
            </div>

            {/* Mobile Navigation */}
            {isOpen && (
                <div className="md:hidden bg-black/90 pt-4 pb-6 px-4 space-y-4">
                    {navLinks.map((link) => (
                        <Link
                            key={link.name}
                            to={link.path}
                            onClick={() => setIsOpen(false)} // Close menu on click
                            className="block text-white hover:text-purple-300 transition-colors text-xl"
                        >
                            {link.name}
                        </Link>
                    ))}
                    {isAuthenticated ? (
                        <>
                            <Link
                                to="/profile"
                                onClick={() => setIsOpen(false)}
                                className="block text-white hover:text-purple-300 transition-colors text-xl"
                            >
                                Profile
                            </Link>
                            <button
                                onClick={() => {
                                    handleSignOut();
                                    setIsOpen(false);
                                }}
                                className="cyber-button w-full py-2 rounded-full font-bold text-lg"
                            >
                                Sign Out
                            </button>
                        </>
                    ) : (
                        <Link
                            to="/auth"
                            onClick={() => setIsOpen(false)}
                            className="cyber-button w-full py-2 rounded-full font-bold text-lg"
                        >
                            Sign In
                        </Link>
                    )}
                </div>
            )}
        </nav>
    );
};

export default Navbar;