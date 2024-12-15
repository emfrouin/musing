// src/components/LevelAdmin.tsx

import React, { useState } from "react";
import { apiPost } from "../utils/api";

interface LevelAdminProps {
    pathId: number;
}

const LevelAdmin: React.FC<LevelAdminProps> = ({ pathId }) => {
    const [newLevel, setNewLevel] = useState({ name: "", description: "" });

    const handleCreateLevel = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            await apiPost('level', { ...newLevel, pathId });
            setNewLevel({ name: "", description: "" });
        } catch (error) {
            console.error("Error creating level:", error);
        }
    };

    return (
        <div className="p-6 mt-4">
            <h3 className="text-xl">Add New Level</h3>
            <form onSubmit={handleCreateLevel} className="space-y-4">
                <input
                    type="text"
                    className="border p-2 w-full"
                    placeholder="Level Name"
                    value={newLevel.name}
                    onChange={(e) => setNewLevel({ ...newLevel, name: e.target.value })}
                />
                <textarea
                    className="border p-2 w-full"
                    placeholder="Level Description"
                    value={newLevel.description}
                    onChange={(e) => setNewLevel({ ...newLevel, description: e.target.value })}
                />
                <button type="submit" className="bg-green-500 text-white px-4 py-2 rounded">
                    Add Level
                </button>
            </form>
        </div>
    );
};

export default LevelAdmin;
