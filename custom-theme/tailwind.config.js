module.exports = {
  content: [
    './templates/**/*.html',
    './templates/**/*.jinja2',
  ],
  theme: {
    extend: {
      colors: {
        accent: '#059669',
      },
      fontFamily: {
        serif: ['Georgia', 'Cambria', 'serif'],
        mono: ['SF Mono', 'Monaco', 'Cascadia Code', 'Roboto Mono', 'Consolas', 'Courier New', 'monospace'],
      },
    },
  },
  plugins: [],
}
