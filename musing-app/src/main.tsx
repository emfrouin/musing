import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import PathCollection from './components/PathCollection.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <PathCollection/>
  </StrictMode>,
)
