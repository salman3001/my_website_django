/** @type {import('tailwindcss').Config} */
const { addDynamicIconSelectors } = require('@iconify/tailwind');

export default {
  content: [
    // "./src/**/*.{js,ts,jsx,tsx}",
    "./*/templates/**/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("daisyui"),
    addDynamicIconSelectors(),
  ],
  daisyui: {
    themes: ["cmyk", "luxury"],
  },
}