module.exports = {
  content: ["./templates/**/*.html", "./theme/templates/**/*.html"],
  theme: {
    extend: {
      fontFamily: {
        "space-grotesk": ["Space Grotesk", "sans-serif"],
      },
    },
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["cyberpunk"],
  },
};
