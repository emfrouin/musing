
import React, { useState } from "react";
import PathAdmin from "./PathAdmin";
import LevelAdmin from "./LevelAdmin";
import SkillAdmin from "./SkillAdmin";

const AdminApp: React.FC = () => {
    const [selectedPathId, setSelectedPathId] = useState<number | null>(null);

    return (
        <div className="min-h-screen bg-gray-100">
            <div className="max-w-screen-lg mx-auto p-6">
                <h1 className="text-3xl font-bold mb-4">Admin Panel</h1>

                <PathAdmin />

                {selectedPathId && (
                    <>
                        <LevelAdmin pathId={selectedPathId} />
                        <SkillAdmin levelId={1} /> {/* Replace levelId dynamically */}
                    </>
                )}
            </div>
        </div>
    );
};

export default AdminApp;