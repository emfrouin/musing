import React, { useEffect, useState } from "react";
import { apiGet } from "../utils/api";
import { Path } from "../types/path";


const PathCollection: React.FC = () => {

    const [paths, setPaths] = useState<Path[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchPaths = async () => {
            setLoading(true);
            setError(null);

            try{
                const paths = await apiGet<Path[]> ('paths');
                setPaths(paths);
            } catch (error) {
                setError(error instanceof Error ? error.message : 'Something went wrong retrieving paths');
            } finally {
                setLoading(false);
            }
        };

        fetchPaths();

    },[]);




    return (
        <div className="bg-gray-100">
            <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                <div className="mx-auto max-w-2xl py-16 sm:py-24 lg:max-w-none lg:py-32">
                <h2 className="text-2xl font-bold text-gray-900">Paths</h2>
                {/* Loading state */}
                {loading && (
                    <div className="flex items-center justify-center text-lg text-blue-500">
                    <svg
                        className="animate-spin h-6 w-6 mr-3"
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                    >
                        <circle cx="12" cy="12" r="10" strokeWidth="4" stroke="currentColor" fill="none"></circle>
                        <path
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="4"
                        d="M4 12a8 8 0 1 0 8-8"
                        ></path>
                    </svg>
                    Loading...
                    </div>
                )}

                {/* Error state */}
                {error && (
                    <div className="bg-coral-100 text-yellow-800 p-4 rounded-md shadow-md mt-4">
                        <h3 className="font-semibold">No Paths Available</h3>
                    </div>
                )}
                

                
                    {/* Path Data */}

                    {!loading && !error && (
                        <div className="mt-6 space-y-12 lg:grid lg:grid-cols-3 lg:gap-x-6 lg:space-y-0">
                        {paths.map((path) => (
                            <div className="group relative">
                                <img 
                                    src="https://tailwindui.com/plus/img/ecommerce-images/home-page-02-edition-02.jpg" 
                                    alt="Wood table with porcelain mug, leather journal, brass pen, leather key ring, and a houseplant." 
                                    className="w-full rounded-lg bg-white object-cover group-hover:opacity-75 max-sm:h-80 sm:aspect-[2/1] lg:aspect-square"
                                />
                                <h3 className="mt-6 text-sm text-gray-500">
                                    <a href="#">
                                    <span className="absolute inset-0"></span>
                                    {path.name}
                                    </a>
                                </h3>
                                <p className="text-base font-semibold text-gray-900">{path.description}</p>
                            </div>

                        ))}
                        </div>
                    )}


                    

                
                </div>
            </div>
            </div>
    );
}
export default PathCollection;