import React from 'react';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer';

const PlanPage = () => {
    const plans = [
        { name: "Basic", price: "Free", features: ["Access to public projects", "Basic profile", "Community support"] },
        { name: "Pro", price: "$99/year", features: ["All Basic features", "Apply to exclusive projects", "Enhanced profile visibility", "Direct messaging with providers"] },
        { name: "Advanced", price: "$199/year", features: ["All Pro features", "AI-powered project matching", "Portfolio hosting", "Priority support"] }
    ];

    return (
        <div className="min-h-screen flex flex-col">
            <Navbar />
            <main className="flex-grow flex items-center justify-center px-4 py-24 sm:py-32">
                <div className="w-full max-w-6xl">
                    <h1 className="text-4xl sm:text-6xl font-bold text-center mb-6 holographic">Choose Your Plan</h1>
                    <p className="text-center text-gray-300 mb-12 max-w-2xl mx-auto">
                        Unlock your potential with a plan that’s designed for your professional growth.
                    </p>
                    <div className="grid md:grid-cols-3 gap-8">
                        {plans.map(plan => (
                            <div key={plan.name} className="glass-morphism p-8 rounded-lg flex flex-col">
                                <h2 className="text-3xl font-bold text-white mb-4">{plan.name}</h2>
                                <p className="text-4xl font-extrabold text-purple-300 mb-6">{plan.price}</p>
                                <ul className="space-y-3 mb-8 flex-grow">
                                    {plan.features.map(feature => (
                                        <li key={feature} className="flex items-center">
                                            <svg className="h-6 w-6 text-green-400 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 13l4 4L19 7" />
                                            </svg>
                                            <span className="text-gray-300">{feature}</span>
                                        </li>
                                    ))}
                                </ul>
                                <button className="w-full cyber-button p-3 rounded-lg font-bold mt-auto">Get Started</button>
                            </div>
                        ))}
                    </div>
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default PlanPage;