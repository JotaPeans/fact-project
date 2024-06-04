const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    // lembrar de mudar pro localhost ou host na azure
    // test site https://automationpractice.pl
    baseUrl: "http://127.0.0.1:8000/",
    viewportWidth: 1920,
    viewportHeight: 1080,
    watchForFileChanges: false,
    setupNodeEvents(on, config) {
    
    },
  },
});