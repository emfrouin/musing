// src/components/SkillAdmin.tsx

import React, { useState } from "react";
import { apiPost } from "../utils/api";

interface SkillAdminProps {
    levelId: number;
}

const SkillAdmin: React.FC<SkillAdminProps> = ({ levelId }) => {
    const [newSkill, setNewSkill] = useState({ name: "", description: "" });

    const handleCreateSkill = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            await apiPost('skill' ,{ ...newSkill, levelId });
            setNewSkill({ name: "", description: "" });
        } catch (error) {
            console.error("Error creating skill:", error);
        }
    };

    return (
        <div className="p-6 mt-4">
            <h3 className="text-xl">Add New Skill</h3>
            <form onSubmit={handleCreateSkill} className="space-y-4">
                <input
                    type="text"
                    className="border p-2 w-full"
                    placeholder="Skill Name"
                    value={newSkill.name}
                    onChange={(e) => setNewSkill({ ...newSkill, name: e.target.value })}
                />
                <textarea
                    className="border p-2 w-full"
                    placeholder="Skill Description"
                    value={newSkill.description}
                    onChange={(e) => setNewSkill({ ...newSkill, description: e.target.value })}
                />
                <button type="submit" className="bg-purple-500 text-white px-4 py-2 rounded">
                    Add Skill
                </button>
            </form>
        </div>
    );
};

export default SkillAdmin;
