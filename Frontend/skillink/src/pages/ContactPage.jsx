import React from 'react';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer';

const ContactPage = () => {
    return (
        <div className="min-h-screen flex flex-col">
            <Navbar />
            <main className="flex-grow flex items-center justify-center px-4 py-24 sm:py-32">
                <div className="glass-morphism p-6 sm:p-8 rounded-lg w-full max-w-4xl">
                    <h1 className="text-3xl sm:text-5xl font-bold text-center mb-6 holographic">Get in Touch</h1>
                    <p className="text-center text-gray-300 mb-10 sm:mb-12">
                        We're here to help and answer any question you might have.
                    </p>
                    <div className="grid md:grid-cols-2 gap-10 md:gap-12">
                        <div className="space-y-6">
                            <h2 className="text-2xl sm:text-3xl font-bold text-white">Contact Information</h2>
                            <div>
                                <h3 className="text-lg sm:text-xl font-semibold text-purple-300">Email Us</h3>
                                <p className="text-gray-400">contact@skillink.com</p>
                            </div>
                            <div>
                                <h3 className="text-lg sm:text-xl font-semibold text-purple-300">Call Us</h3>
                                <p className="text-gray-400">+1 (555) 123-4567</p>
                            </div>
                            <div>
                                <h3 className="text-lg sm:text-xl font-semibold text-purple-300">Our Office</h3>
                                <p className="text-gray-400">123 Innovation Drive, Tech City, 54321</p>
                            </div>
                        </div>
                        <div>
                            <form className="space-y-6">
                                <h2 className="text-2xl sm:text-3xl font-bold text-white">Send Us a Message</h2>
                                <div>
                                    <label htmlFor="name" className="block text-sm font-medium text-gray-300 mb-1">Your Name</label>
                                    <input type="text" id="name" name="name" className="w-full p-3 rounded bg-gray-700 text-white border border-gray-600 focus:outline-none focus:border-purple-500" />
                                </div>
                                <div>
                                    <label htmlFor="email" className="block text-sm font-medium text-gray-300 mb-1">Your Email</label>
                                    <input type="email" id="email" name="email" className="w-full p-3 rounded bg-gray-700 text-white border border-gray-600 focus:outline-none focus:border-purple-500" />
                                </div>
                                <div>
                                    <label htmlFor="message" className="block text-sm font-medium text-gray-300 mb-1">Your Message</label>
                                    <textarea id="message" name="message" rows="5" className="w-full p-3 rounded bg-gray-700 text-white border border-gray-600 focus:outline-none focus:border-purple-500"></textarea>
                                </div>
                                <button type="submit" className="w-full cyber-button p-3 rounded-lg font-bold">
                                    Send Message
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default ContactPage; 