// App.jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import HomePage from './pages/HomePage';
import AuthPage from './pages/AuthPage';
import ContactPage from './pages/ContactPage';
import AboutPage from './pages/AboutPage';
import PlanPage from './pages/PlanPage';
import UserProfile from './components/user/UserProfile';
import FAQPage from './pages/FAQPage';
import PrivacyPolicyPage from './pages/PrivacyPolicyPage';
import ConnectionPage from './pages/ConnectionPage';
import Chatbot from './components/layout/Chatbot';
import SignedInLandingPage from './pages/SignedInLandingPage';
import OpportunitiesPage from './pages/OpportunitiesPage'; // Import the new OpportunitiesPage
import ForumsPage from './pages/ForumsPage'; // Import the new ForumsPage
import EventsPage from './pages/EventsPage'; // Import the new EventsPage

const App = () => {
    const isAuthenticated = () => !!localStorage.getItem('authToken');

    return (
        <Router>
            <div className="relative">
                <Routes>
                    <Route
                        path="/"
                        element={isAuthenticated() ? <SignedInLandingPage /> : <HomePage />}
                    />
                    <Route path="/auth" element={<AuthPage />} />
                    <Route path="/contact" element={<ContactPage />} />
                    <Route path="/about" element={<AboutPage />} />
                    <Route path="/pricing" element={<PlanPage />} />
                    <Route path="/faq" element={<FAQPage />} />
                    <Route path="/privacy" element={<PrivacyPolicyPage />} />
                    <Route path="/connection" element={<ConnectionPage />} />
                    <Route path="/opportunities" element={<OpportunitiesPage />} /> {/* Add the new Opportunities route */}
                    <Route path="/forums" element={<ForumsPage />} /> {/* Add the new Forums route */}
                    <Route path="/events" element={<EventsPage />} /> {/* Add the new Events route */}
                    <Route
                        path="/profile"
                        element={isAuthenticated() ? <UserProfile /> : <Navigate to="/auth" />}
                    />
                </Routes>
                <Chatbot />
            </div>
        </Router>
    );
};

export default App;