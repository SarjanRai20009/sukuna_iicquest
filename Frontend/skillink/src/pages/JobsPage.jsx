// src/pages/JobsPage.jsx
import React, { useEffect, useState } from 'react';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer';

const JobsPage = () => {
    const [jobs, setJobs] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [searchTerm, setSearchTerm] = useState('');
    const [filterCategory, setFilterCategory] = useState('All');
    const [filterType, setFilterType] = useState('All');

    useEffect(() => {
        const fetchJobs = async () => {
            try {
                // Construct query parameters for filters
                const queryParams = new URLSearchParams();
                if (searchTerm) {
                    queryParams.append('search', searchTerm);
                }
                if (filterCategory !== 'All') {
                    queryParams.append('category', filterCategory);
                }
                if (filterType !== 'All') {
                    queryParams.append('job_type', filterType);
                }

                const url = `/api/jobs/?${queryParams.toString()}`;
                const response = await fetch(url); // Replace with your actual Django API endpoint
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const data = await response.json();
                setJobs(data);
            } catch (err) {
                setError('Failed to fetch jobs. Please try again later.');
                console.error('Error fetching jobs:', err);
            } finally {
                setLoading(false);
            }
        };

        fetchJobs();
    }, [searchTerm, filterCategory, filterType]);

    if (loading) {
        return (
            <div className="min-h-screen flex flex-col">
                <Navbar />
                <main className="flex-grow flex items-center justify-center">
                    <p className="text-white">Loading jobs...</p>
                </main>
                <Footer />
            </div>
        );
    }

    if (error) {
        return (
            <div className="min-h-screen flex flex-col">
                <Navbar />
                <main className="flex-grow flex items-center justify-center">
                    <p className="text-red-500">{error}</p>
                </main>
                <Footer />
            </div>
        );
    }

    return (
        <div className="min-h-screen flex flex-col">
            <Navbar />
            <main className="flex-grow px-4 py-24 sm:py-32">
                <div className="text-center max-w-4xl mx-auto">
                    <h1 className="text-4xl sm:text-6xl font-bold mb-6 holographic">Job Openings</h1>
                    <p className="text-lg text-gray-300 leading-relaxed mb-12">
                        Discover exciting career opportunities and find your next challenge.
                    </p>
                </div>

                <div className="max-w-6xl mx-auto glass-morphism p-6 rounded-lg mb-8">
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <input
                            type="text"
                            placeholder="Search by title or company..."
                            value={searchTerm}
                            onChange={(e) => setSearchTerm(e.target.value)}
                            className="w-full p-3 rounded bg-gray-700/50 text-white border-2 border-transparent focus:outline-none focus:border-purple-500"
                        />
                        <select
                            value={filterCategory}
                            onChange={(e) => setFilterCategory(e.target.value)}
                            className="w-full p-3 rounded bg-gray-700/50 text-white border-2 border-transparent focus:outline-none focus:border-purple-500"
                        >
                            <option value="All">All Categories</option>
                            <option value="Software">Software Development</option>
                            <option value="Design">Design</option>
                            <option value="Marketing">Marketing</option>
                            {/* Add more categories as needed */}
                        </select>
                        <select
                            value={filterType}
                            onChange={(e) => setFilterType(e.target.value)}
                            className="w-full p-3 rounded bg-gray-700/50 text-white border-2 border-transparent focus:outline-none focus:border-purple-500"
                        >
                            <option value="All">All Types</option>
                            <option value="Full-time">Full-time</option>
                            <option value="Part-time">Part-time</option>
                            <option value="Contract">Contract</option>
                            <option value="Internship">Internship</option>
                            {/* Add more types as needed */}
                        </select>
                    </div>
                </div>

                <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    {jobs.length > 0 ? (
                        jobs.map((job) => (
                            <div key={job.id} className="glass-morphism p-6 rounded-lg flex flex-col justify-between">
                                <div>
                                    <h2 className="text-2xl font-bold text-white mb-2">{job.title}</h2>
                                    <p className="text-purple-300 mb-2">{job.company}</p>
                                    <p className="text-gray-400 text-sm mb-4">{job.location} &bull; {job.job_type}</p>
                                    <p className="text-gray-300 line-clamp-3 mb-4">{job.description}</p>
                                </div>
                                <div>
                                    {job.multimedia_url && (
                                        <p className="text-gray-500 text-xs mb-2">
                                            <a href={job.multimedia_url} target="_blank" rel="noopener noreferrer" className="text-blue-400 hover:underline">View Multimedia</a>
                                        </p>
                                    )}
                                    {job.related_course && (
                                        <p className="text-gray-500 text-xs mb-4">
                                            Related Course: <span className="text-green-400">{job.related_course.title}</span>
                                        </p>
                                    )}
                                    <button className="cyber-button w-full py-2 rounded-lg font-bold text-sm">
                                        View Details
                                    </button>
                                </div>
                            </div>
                        ))
                    ) : (
                        <p className="text-white text-center col-span-full">No jobs found matching your criteria.</p>
                    )}
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default JobsPage;