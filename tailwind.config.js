// tailwind.config.js
module.exports = {
  content: ["./templates/**/*.html", "./static/**/*.css"],
  // adjust as needed
  theme: {
    extend: {}
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["forest"]
  }
};

