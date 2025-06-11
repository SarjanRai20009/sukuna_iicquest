import React, { useState } from 'react';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer';

const FAQItem = ({ question, answer }) => {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <div className="border-b border-gray-700 py-4">
            <button
                className="w-full text-left flex justify-between items-center text-white text-lg font-semibold"
                onClick={() => setIsOpen(!isOpen)}
            >
                {question}
                <span className={`transform transition-transform ${isOpen ? 'rotate-180' : ''}`}>▼</span>
            </button>
            {isOpen && <p className="text-gray-400 mt-2">{answer}</p>}
        </div>
    );
};

const FAQPage = () => {
    const faqs = [
        { question: "What is Skillink?", answer: "Skillink is a platform designed to connect talented individuals with meaningful opportunities." },
        { question: "How do I create an account?", answer: "You can create an account by clicking the 'Get Started' button on our homepage and filling out the sign-up form." },
        { question: "Is there a fee to join?", answer: "We offer both free and paid plans. Our basic plan is free, while our Pro and Advanced plans offer additional features for a yearly fee." }
    ];

    return (
        <div className="min-h-screen flex flex-col">
            <Navbar />
            <main className="flex-grow flex items-center justify-center px-4 py-24 sm:py-32">
                <div className="w-full max-w-4xl glass-morphism p-8 rounded-lg">
                    <h1 className="text-4xl sm:text-6xl font-bold text-center mb-12 holographic">FAQs</h1>
                    <div className="space-y-4">
                        {faqs.map((faq, index) => (
                            <FAQItem key={index} question={faq.question} answer={faq.answer} />
                        ))}
                    </div>
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default FAQPage;