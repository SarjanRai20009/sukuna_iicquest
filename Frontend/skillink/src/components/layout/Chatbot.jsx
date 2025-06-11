import React, { useState, useRef, useEffect } from 'react';

const Chatbot = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [messages, setMessages] = useState([
        { from: 'bot', text: "Hi there! I'm the Skillink assistant. How can I help you today?" }
    ]);
    const chatboxRef = useRef(null);

    const botResponses = {
        "hi": "Hello! It's great to hear from you. What can I help you with?",
        "what is skillink?": "Skillink is a dynamic platform designed to connect skilled professionals with project providers. Our goal is to bridge the gap between talent and opportunity seamlessly.",
        "how do i find a project?": "You can find projects by using the search bar in the navigation to look for specific roles or technologies. You can also visit the 'Hub' to see recent project postings.",
        "what are the pricing plans?": "We have several pricing tiers, including a free Basic plan! You can view all the details and features of our Pro and Advanced plans on the 'Pricing' page."
    };

    const readyMadeQuestions = [
        "Hi",
        "What is Skillink?",
        "How do I find a project?",
        "What are the pricing plans?"
    ];

    const handleQuestionClick = (question) => {
        const userMessage = { from: 'user', text: question };
        setMessages(prev => [...prev, userMessage]);

        // Find the bot's response
        const answer = botResponses[question.toLowerCase()] || "I'm not sure how to answer that yet, but I'm learning!";
        
        setTimeout(() => {
            const botMessage = { from: 'bot', text: answer };
            setMessages(prev => [...prev, botMessage]);
        }, 1000);
    };

    // Auto-scroll to the latest message
    useEffect(() => {
        if (chatboxRef.current) {
            chatboxRef.current.scrollTop = chatboxRef.current.scrollHeight;
        }
    }, [messages]);

    return (
        <div className="fixed bottom-5 right-5 z-50">
            {isOpen && (
                <div className="w-80 h-96 bg-gray-800/80 backdrop-blur-md rounded-lg shadow-xl flex flex-col">
                    <div className="p-4 border-b border-gray-700 flex justify-between items-center">
                        <h3 className="text-lg font-bold text-white">Skillink Assistant</h3>
                    </div>
                    <div ref={chatboxRef} className="flex-grow p-4 overflow-y-auto">
                        {messages.map((msg, index) => (
                            <div key={index} className={`flex mb-3 ${msg.from === 'bot' ? 'justify-start' : 'justify-end'}`}>
                                <span className={`inline-block p-2 rounded-lg max-w-xs ${msg.from === 'bot' ? 'bg-purple-600 text-white' : 'bg-gray-600 text-white'}`}>
                                    {msg.text}
                                </span>
                            </div>
                        ))}
                    </div>
                    <div className="p-2 border-t border-gray-700">
                        <div className="flex flex-wrap gap-2 justify-center">
                            {readyMadeQuestions.map(q => (
                                <button key={q} onClick={() => handleQuestionClick(q)} className="bg-gray-700 text-white text-sm px-3 py-1 rounded-full hover:bg-purple-500 transition-colors">
                                    {q}
                                </button>
                            ))}
                        </div>
                    </div>
                </div>
            )}
            <button
                onClick={() => setIsOpen(!isOpen)}
                className="w-16 h-16 bg-purple-600 rounded-full flex items-center justify-center text-white text-3xl shadow-lg hover:bg-purple-700 transition-all transform hover:scale-110"
            >
                {isOpen ? '✖' : '💬'}
            </button>
        </div>
    );
};

export default Chatbot;
