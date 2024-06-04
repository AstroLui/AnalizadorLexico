/** @type {import('tailwindcss').Config} */
import daisyui from "daisyui"
module.exports = {
  content: ["./AnalizadorLexico/templates/**/*.{html,js}"],
  theme: {
    extend: {
      transitionProperty: 
      {
        'display': 'display',
      }
    },
  },
  plugins: [
    daisyui,
  ],
  daisyui: {
    themes: [
      "retro",
      "aqua",
      "lofi",
      "pastel",
      "fantasy",
      "wireframe",
      "black",
      "luxury",
      "dracula",
      "coffee",
      "sunset",
    ],
  },
}

