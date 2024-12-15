import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import AdminApp from './components/AdminApp.tsx'

createRoot(document.getElementById('root')!).render(
    <StrictMode>
        <AdminApp />
    </StrictMode>,
)
