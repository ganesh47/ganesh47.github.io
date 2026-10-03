const { defineConfig } = require('@playwright/test');
module.exports = defineConfig({
  testDir: './tests', workers: 1, timeout: 45000,
  reporter: [['list'], ['html', { open: 'never' }]],
  use: { baseURL: process.env.BLOG_BASE_URL || 'http://127.0.0.1:4315', screenshot: 'only-on-failure', trace: 'retain-on-failure' },
  webServer: process.env.BLOG_BASE_URL ? undefined : { command: 'python3 -m http.server 4315 --bind 127.0.0.1 --directory _site', url:'http://127.0.0.1:4315', reuseExistingServer:!process.env.CI },
});
