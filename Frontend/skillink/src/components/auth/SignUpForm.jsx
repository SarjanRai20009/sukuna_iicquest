import React from 'react';

const SignUpForm = () => {
    const interests = ["IT", "Business", "Creative Arts", "Engineering", "Healthcare", "Marketing", "Education"];
    const genders = ["Male", "Female", "Other"];

    return (
        <form className="space-y-4">
            <h2 className="text-2xl font-bold text-center text-white">Create Your Account</h2>

            {/* Full Name & Username */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                    <label className="block text-sm font-medium text-gray-300 mb-1">Full Name</label>
                    <input type="text" className="w-full p-2 rounded bg-gray-700 text-white border border-gray-600" />
                </div>
                <div>
                    <label className="block text-sm font-medium text-gray-300 mb-1">Username</label>
                    <input type="text" className="w-full p-2 rounded bg-gray-700 text-white border border-gray-600" />
                </div>
            </div>

            {/* Phone & DOB */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                    <label className="block text-sm font-medium text-gray-300 mb-1">Phone Number</label>
                    <input type="tel" className="w-full p-2 rounded bg-gray-700 text-white border border-gray-600" />
                </div>
                <div>
                    <label className="block text-sm font-medium text-gray-300 mb-1">Date of Birth</label>
                    <input type="date" className="w-full p-2 rounded bg-gray-700 text-white border border-gray-600" />
                </div>
            </div>

            {/* Email */}
            <div>
                <label className="block text-sm font-medium text-gray-300 mb-1">Email</label>
                <input type="email" className="w-full p-2 rounded bg-gray-700 text-white border border-gray-600" />
            </div>

            {/* Password */}
            <div>
                <label className="block text-sm font-medium text-gray-300 mb-1">Password</label>
                <input type="password" placeholder="••••••••" className="w-full p-2 rounded bg-gray-700 text-white border border-gray-600" />
            </div>

            {/* Address */}
            <div>
                <label className="block text-sm font-medium text-gray-300 mb-1">Address</label>
                <textarea className="w-full p-2 rounded bg-gray-700 text-white border border-gray-600" rows="2"></textarea>
            </div>

            {/* Gender */}
            <div>
                <label className="block text-sm font-medium text-gray-300 mb-1">Gender</label>
                <select className="w-full p-2 rounded bg-gray-700 text-white border border-gray-600">
                    <option value="">Select</option>
                    {genders.map(gender => (
                        <option key={gender} value={gender}>{gender}</option>
                    ))}
                </select>
            </div>

            {/* Profile Picture */}
            <div>
                <label className="block text-sm font-medium text-gray-300 mb-1">Profile Picture</label>
                <input type="file" accept="image/*" className="w-full text-sm text-gray-400 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-purple-500 file:text-white hover:file:bg-purple-600" />
            </div>

            {/* CV Upload */}
            <div>
                <label className="block text-sm font-medium text-gray-300 mb-1">CV (PDF only)</label>
                <input type="file" accept=".pdf" className="w-full text-sm text-gray-400 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-500 file:text-white hover:file:bg-blue-600" />
            </div>

            {/* Interests */}
            <div>
                <label className="block text-sm font-medium text-gray-300 mb-1">Areas of Interest</label>
                <div className="grid grid-cols-2 sm:grid-cols-3 gap-2">
                    {interests.map(interest => (
                        <div key={interest} className="flex items-center">
                            <input id={interest} type="checkbox" className="h-4 w-4 rounded border-gray-300 text-purple-600 focus:ring-purple-500" />
                            <label htmlFor={interest} className="ml-2 text-sm text-gray-300">{interest}</label>
                        </div>
                    ))}
                </div>
            </div>

            {/* Submit Button */}
            <button type="submit" className="w-full cyber-button p-3 rounded-lg font-bold mt-4">
                Sign Up
            </button>
        </form>
    );
};

export default SignUpForm;
    