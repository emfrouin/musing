import React from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { PathFormData } from '../types/pathFormData';
import { apiPost } from '../utils/api';

const PathForm: React.FC = () => {
    // Init React Hook Form
    const { register, handleSubmit, formState: { errors } } = useForm<PathFormData>();

    // Submit handler
    const onSubmit: SubmitHandler<PathFormData> = async (data) => {
        try {
            const response = await apiPost<PathFormData>('paths', data);
            console.log('New Path submitted:', response);
            //TODO: HANDLE SUCCESS HERE ie. show message or reset/redirect
        } catch (error) {
            console.error ('Error submitting form:', error);
            if (error instanceof Error) {
                alert(error.message);
            }
        }
    };


    return (
        <div className="min-h-screen bg-gray-100 flex items-center justify-center p-6">
            <div className="max-w-md w-full bg-white p-8 rounded-lg shadow-lg">
                <h2 className="text-2xl font-semibold text-center text-gray-800 mb-6">Create Item</h2>
        

                <form onSubmit={handleSubmit(onSubmit)}>
                    <div>
                        <label htmlFor='name'>Name</label>
                        <input id='name' {...register('name', {required: 'Name is required'})} />
                        {errors && <div style={{color: 'red'}}>ERROR!!!</div>}
                    </div>
                    <div>
                        <label htmlFor='description'>Description</label>
                        <textarea id='description' />

                    </div>
                    <button
                        type="submit"
                        className="w-full py-2 bg-blue-500 text-white font-semibold rounded-md shadow-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50">
                        Submit
                    </button>
                </form>
            </div>
        </div>
    );

};

export default PathForm;