/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../home/templates/**/*.{html,js}"],
  theme: {
    fontFamily: {
      'sans': ['Poppins', 'sans-serif'],
    },
    fontWeight: {
      light: '300',
      normal: '400',
      medium: '500',
      semibold: '600',
      bold: '700',
    },
    extend: {},
  },
  plugins: [],
}

