import React from 'react';
import { Link } from 'react-router-dom';

const Footer = () => {
    return (
        <footer className="bg-black/50 text-white p-8">
            <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-8">
                <div>
                    <h3 className="text-xl font-bold mb-4 holographic">Skillink</h3>
                    <p className="text-gray-400">Where Vision Meets Expertise.</p>
                </div>
                <div>
                    <h4 className="font-semibold mb-3">Quick Links</h4>
                    <ul>
                        <li><Link to="/about" className="hover:text-purple-300">About Us</Link></li>
                        <li><Link to="/contact" className="hover:text-purple-300">Contact</Link></li>
                        <li><Link to="/pricing" className="hover:text-purple-300">Pricing</Link></li>
                    </ul>
                </div>
                <div>
                    <h4 className="font-semibold mb-3">Support</h4>
                    <ul>
                        <li><Link to="/faq" className="hover:text-purple-300">FAQ</Link></li>
                        <li><Link to="/privacy" className="hover:text-purple-300">Privacy Policy</Link></li>
                    </ul>
                </div>
                <div>
                    <h4 className="font-semibold mb-3">Connect</h4>
                    <p className="text-gray-400">contact@skillink.com</p>
                </div>
            </div>
            <div className="text-center text-gray-500 mt-8 pt-8 border-t border-gray-800">
                © {new Date().getFullYear()} Skillink. All rights reserved.
            </div>
        </footer>
    );
};

export default Footer;