/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx,html}",
  ],
  darkMode: 'media',
  theme: {
    extend: {
      colors: {
        // Primary Colors
        'warm-yellow': '#FFD700', // Bright, energetic yellow
        'teal': '#008080',        // Soothing teal color
        'navy-blue': '#003366',   // Dark, professional blue
        
        // Accent Colors
        'coral': '#FF6F61',       // Playful, energetic coral
        'soft-lavender': '#B39DDB', // Calming lavender accent
        
        // Neutrals
        'light-gray': '#F4F4F4',  // Light neutral background
        'charcoal-gray': '#333333', // Dark text color for legibility
        
        // Optional Pop Colors
        'bright-green': '#32CD32', // For highlights, success, etc.
        'bright-pink': '#FF1493', // For creative pops of color
      },
      fontFamily: {
        // Define your font family here (example)
        sans: ['Helvetica', 'Arial', 'sans-serif'],
        serif: ['Georgia', 'serif'],
      },
      spacing: {
        // Custom spacing if needed
        '128': '32rem', // Example: Custom large spacing
      },
    },
  },
  plugins: [],
}

