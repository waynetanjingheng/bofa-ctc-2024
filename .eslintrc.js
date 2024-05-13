module.exports = {
  parser: "@typescript-eslint/parser",
  plugins: ["check-file", "import", "@typescript-eslint"],
  extends: [
    "next/core-web-vitals",
    "prettier",
    "plugin:import/recommended",
    "plugin:@typescript-eslint/recommended",
  ],
  settings: {
    "import/resolver": {
      typescript: true,
      node: true,
    },
  },
};
