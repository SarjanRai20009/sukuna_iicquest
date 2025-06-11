import React from 'react';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer';

const PrivacyPolicyPage = () => {
    return (
        <div className="min-h-screen flex flex-col">
            <Navbar />
            <main className="flex-grow flex items-center justify-center px-4 py-24 sm:py-32">
                <div className="w-full max-w-4xl glass-morphism p-8 rounded-lg">
                    <h1 className="text-4xl sm:text-6xl font-bold text-center mb-12 holographic">Privacy Policy</h1>
                    <div className="text-gray-300 space-y-4">
                        <p>This is a placeholder for your privacy policy. You should replace this with your own terms.</p>
                        <h2 className="text-2xl font-semibold text-white pt-4">Information We Collect</h2>
                        <p>We collect information you provide directly to us, such as when you create an account, as well as information that is automatically collected when you use our services.</p>
                        <h2 className="text-2xl font-semibold text-white pt-4">How We Use Your Information</h2>
                        <p>We use the information we collect to provide, maintain, and improve our services, as well as to develop new ones.</p>
                    </div>
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default PrivacyPolicyPage;