const resolve = require('@rollup/plugin-node-resolve').default;
const commonjs = require('@rollup/plugin-commonjs');

module.exports = {
  input: 'index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'cjs',
    sourcemap: false
  },
  plugins: [
    resolve(),
    commonjs()
  ]
};
