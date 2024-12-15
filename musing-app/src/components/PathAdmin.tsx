// src/components/PathAdmin.tsx

import React, { useState, useEffect } from "react";
import { apiPost, apiGet } from "../utils/api";

const PathAdmin: React.FC = () => {
    const [paths, setPaths] = useState<any[]>([]);
    const [newPath, setNewPath] = useState({ name: "", description: "" });

    useEffect(() => {
        const getPaths = async () => {
            try {
                const paths = await apiGet('paths');
                setPaths(paths);
            } catch (error) {
                console.error("Error fetching paths:", error);
            }
        };
        getPaths();
    }, []);

    const handleCreatePath = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const createdPath = await apiPost('paths', newPath);
            setPaths([...paths, createdPath]);
            setNewPath({ name: "", description: "" });
        } catch (error) {
            console.error("Error creating path:", error);
        }
    };

    return (
        <div className="p-6">
            <h2 className="text-2xl font-semibold">Paths</h2>

            <div className="mt-4">
                <h3 className="text-xl">Create New Path</h3>
                <form onSubmit={handleCreatePath} className="space-y-4">
                    <input
                        type="text"
                        className="border p-2 w-full"
                        placeholder="Path Name"
                        value={newPath.name}
                        onChange={(e) => setNewPath({ ...newPath, name: e.target.value })}
                    />
                    <textarea
                        className="border p-2 w-full"
                        placeholder="Path Description"
                        value={newPath.description}
                        onChange={(e) => setNewPath({ ...newPath, description: e.target.value })}
                    />
                    <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">
                        Add Path
                    </button>
                </form>
            </div>

            <div className="mt-8">
                <h3 className="text-xl">Path List</h3>
                <ul className="space-y-4 mt-4">
                    {paths.map((path) => (
                        <li key={path.id} className="border p-4 rounded">
                            <h4 className="font-semibold">{path.name}</h4>
                            <p>{path.description}</p>
                            <button className="mt-2 text-blue-500">Manage Levels</button>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default PathAdmin;
