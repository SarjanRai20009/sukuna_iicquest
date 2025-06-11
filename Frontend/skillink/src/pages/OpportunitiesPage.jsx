// src/pages/OpportunitiesPage.jsx
import React, { useState, useEffect } from 'react';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer';

const OpportunitiesPage = () => {
    // Mock Data for Opportunities (Jobs, Internships, Scholarships)
    const allOpportunities = [
        {
            id: 1,
            type: 'Job',
            title: 'Senior React Developer',
            company: 'Tech Solutions Inc.',
            location: 'Remote',
            description: 'We are seeking a highly skilled Senior React Developer to join our dynamic team...',
            category: 'Software',
            job_type: 'Full-time',
            posted_date: '2024-05-20',
            multimedia_url: 'https://example.com/react-dev-job-video.mp4', // Example multimedia
            related_course: { title: 'Advanced React Course', url: 'https://example.com/react-course' } // Example course
        },
        {
            id: 2,
            type: 'Internship',
            title: 'UI/UX Design Intern',
            company: 'Creative Hub',
            location: 'New York, NY',
            description: 'Gain hands-on experience in user interface and user experience design...',
            category: 'Design',
            job_type: 'Internship',
            posted_date: '2024-06-01',
            multimedia_url: '',
            related_course: { title: 'UI/UX Fundamentals', url: 'https://example.com/uiux-course' }
        },
        {
            id: 3,
            type: 'Scholarship',
            title: 'AI/ML Research Grant',
            company: 'Future Innovators Fund',
            location: 'Global',
            description: 'Scholarship for students pursuing advanced research in Artificial Intelligence and Machine Learning.',
            category: 'Education',
            job_type: 'Scholarship', // Using job_type to signify scholarship
            posted_date: '2024-05-15',
            multimedia_url: 'https://example.com/ai-scholarship-info.pdf',
            related_course: null
        },
        {
            id: 4,
            type: 'Job',
            title: 'Digital Marketing Specialist',
            company: 'Global Brands Ltd.',
            location: 'London, UK',
            description: 'Looking for a passionate digital marketer with SEO and SEM experience.',
            category: 'Marketing',
            job_type: 'Full-time',
            posted_date: '2024-05-25',
            multimedia_url: '',
            related_course: { title: 'Digital Marketing Masterclass', url: 'https://example.com/digital-marketing' }
        },
        {
            id: 5,
            type: 'Internship',
            title: 'Software Engineering Intern',
            company: 'Innovate Solutions',
            location: 'San Francisco, CA',
            description: 'Join our engineering team for a summer internship program.',
            category: 'Software',
            job_type: 'Internship',
            posted_date: '2024-06-10',
            multimedia_url: '',
            related_course: null
        },
        {
            id: 6,
            type: 'Job',
            title: 'Product Manager',
            company: 'NextGen Products',
            location: 'Remote',
            description: 'Drive the roadmap for our cutting-edge SaaS product.',
            category: 'Product Management',
            job_type: 'Full-time',
            posted_date: '2024-06-05',
            multimedia_url: '',
            related_course: null
        },
    ];

    const [opportunities, setOpportunities] = useState(allOpportunities);
    const [searchTerm, setSearchTerm] = useState('');
    const [filterType, setFilterType] = useState('All'); // 'Job', 'Internship', 'Scholarship', 'All'
    const [filterCategory, setFilterCategory] = useState('All');

    useEffect(() => {
        let filtered = allOpportunities;

        // Filter by Type
        if (filterType !== 'All') {
            filtered = filtered.filter(opp => opp.type === filterType);
        }

        // Filter by Category
        if (filterCategory !== 'All') {
            filtered = filtered.filter(opp => opp.category === filterCategory);
        }

        // Search by Term
        if (searchTerm) {
            const lowerCaseSearchTerm = searchTerm.toLowerCase();
            filtered = filtered.filter(opp =>
                opp.title.toLowerCase().includes(lowerCaseSearchTerm) ||
                opp.company.toLowerCase().includes(lowerCaseSearchTerm) ||
                opp.description.toLowerCase().includes(lowerCaseSearchTerm)
            );
        }

        setOpportunities(filtered);
    }, [searchTerm, filterType, filterCategory]);

    const categories = ['All', 'Software', 'Design', 'Marketing', 'Education', 'Product Management'];

    return (
        <div className="min-h-screen flex flex-col">
            <Navbar />
            <main className="flex-grow px-4 py-24 sm:py-32">
                <div className="text-center max-w-4xl mx-auto">
                    <h1 className="text-4xl sm:text-6xl font-bold mb-6 holographic">Opportunities Hub</h1>
                    <p className="text-lg text-gray-300 leading-relaxed mb-12">
                        Explore jobs, internships, and scholarships tailored to your aspirations.
                    </p>
                </div>

                <div className="max-w-6xl mx-auto glass-morphism p-6 rounded-lg mb-8">
                    <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                        <input
                            type="text"
                            placeholder="Search opportunities..."
                            value={searchTerm}
                            onChange={(e) => setSearchTerm(e.target.value)}
                            className="w-full p-3 rounded bg-gray-700/50 text-white border-2 border-transparent focus:outline-none focus:border-purple-500"
                        />
                        <select
                            value={filterType}
                            onChange={(e) => setFilterType(e.target.value)}
                            className="w-full p-3 rounded bg-gray-700/50 text-white border-2 border-transparent focus:outline-none focus:border-purple-500"
                        >
                            <option value="All">All Types</option>
                            <option value="Job">Jobs</option>
                            <option value="Internship">Internships</option>
                            <option value="Scholarship">Scholarships</option>
                        </select>
                        <select
                            value={filterCategory}
                            onChange={(e) => setFilterCategory(e.target.value)}
                            className="w-full p-3 rounded bg-gray-700/50 text-white border-2 border-transparent focus:outline-none focus:border-purple-500"
                        >
                            {categories.map(cat => (
                                <option key={cat} value={cat}>{cat}</option>
                            ))}
                        </select>
                         <button
                            onClick={() => {
                                setSearchTerm('');
                                setFilterType('All');
                                setFilterCategory('All');
                            }}
                            className="w-full cyber-button p-3 rounded-lg font-bold text-sm"
                        >
                            Clear Filters
                        </button>
                    </div>
                </div>

                <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    {opportunities.length > 0 ? (
                        opportunities.map((opp) => (
                            <div key={opp.id} className="glass-morphism p-6 rounded-lg flex flex-col justify-between">
                                <div>
                                    <span className={`px-3 py-1 rounded-full text-xs font-semibold ${
                                        opp.type === 'Job' ? 'bg-green-500/30 text-green-300' :
                                        opp.type === 'Internship' ? 'bg-blue-500/30 text-blue-300' :
                                        'bg-purple-500/30 text-purple-300'
                                    } mb-2 inline-block`}>
                                        {opp.type}
                                    </span>
                                    <h2 className="text-2xl font-bold text-white mb-2">{opp.title}</h2>
                                    <p className="text-purple-300 mb-2">{opp.company}</p>
                                    <p className="text-gray-400 text-sm mb-4">{opp.location} &bull; {opp.job_type}</p>
                                    <p className="text-gray-300 line-clamp-3 mb-4">{opp.description}</p>
                                </div>
                                <div>
                                    {opp.multimedia_url && (
                                        <p className="text-gray-500 text-xs mb-2">
                                            <a href={opp.multimedia_url} target="_blank" rel="noopener noreferrer" className="text-blue-400 hover:underline">View Multimedia</a>
                                        </p>
                                    )}
                                    {opp.related_course && (
                                        <p className="text-gray-500 text-xs mb-4">
                                            Related Course: <a href={opp.related_course.url} target="_blank" rel="noopener noreferrer" className="text-green-400 hover:underline">{opp.related_course.title}</a>
                                        </p>
                                    )}
                                    <button className="cyber-button w-full py-2 rounded-lg font-bold text-sm">
                                        View Details
                                    </button>
                                </div>
                            </div>
                        ))
                    ) : (
                        <p className="text-white text-center col-span-full">No opportunities found matching your criteria.</p>
                    )}
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default OpportunitiesPage;