import axios, { AxiosError } from 'axios';

const API_URL = 'http://127.0.0.1:8000';

const axiosInstance = axios.create({
    baseURL: API_URL,
    timeout: 10000,
});

export const apiPost = async <T>(url: string, data: T) => {
    try {
        const response = await axiosInstance.post(url, data);
        return response.data;
    } catch (error) {
        if (error instanceof AxiosError) {
            throw new Error(error.response?.data.message || 'API POST request failed');
        }
        throw new Error('Unknown error occurred');
    }
};

export const apiGet = async <T>(url: string) => {
    try {
        const response = await axiosInstance.get(url);
        return response.data;
    } catch (error) {
        if (error instanceof AxiosError) {
            throw new Error(error.response?.data.message || 'API GET request failed');
        }
        throw new Error('Unknown error occurred');
    }
}