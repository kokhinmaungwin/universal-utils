const resolve = require('@rollup/plugin-node-resolve').default;
const commonjs = require('@rollup/plugin-commonjs');
const { terser } = require('@rollup/plugin-terser');

module.exports = {
  input: 'index.js',
  output: {
    file: 'dist/bundle.min.js',
    format: 'cjs',  // CommonJS format
    sourcemap: true,
  },
  plugins: [
    resolve(),
    commonjs(),
    terser()
  ]
};
