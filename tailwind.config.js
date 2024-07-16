/** @type {import('tailwindcss').Config} */
import daisyui from "daisyui"
module.exports = {
  content: ["./AnalizadorLexico/templates/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        'culpa': ['"Mea Culpa"'],
        'inter':['"Inter Tight"']
      }
    },
    colors: {
      'luxury': '#F7DC6F',
      'rose': '#E3242B',
    }
  },
  plugins: [
    daisyui,
  ],
  daisyui: {
    themes: [
      "light",
    ],
    
  },
}

