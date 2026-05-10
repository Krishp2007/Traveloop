/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./travel/**/*.html",
    "./travel/**/*.py",
    "./static_src/**/*.css",
    "./static/js/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        travel: {
          night: "#0b1020",
          ocean: "#0ea5e9",
          coral: "#f97316",
          sand: "#fef3c7",
        },
      },
      fontFamily: {
        display: ["'Outfit'", "system-ui", "sans-serif"],
        body: ["'DM Sans'", "system-ui", "sans-serif"],
      },
      backdropBlur: {
        xs: "2px",
      },
      animation: {
        float: "float 6s ease-in-out infinite",
        shimmer: "shimmer 12s linear infinite",
      },
      keyframes: {
        float: {
          "0%, 100%": { transform: "translateY(0)" },
          "50%": { transform: "translateY(-12px)" },
        },
        shimmer: {
          "0%": { backgroundPosition: "0% 50%" },
          "100%": { backgroundPosition: "200% 50%" },
        },
      },
    },
  },
  plugins: [],
};
