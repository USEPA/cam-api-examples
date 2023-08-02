const path = require('path');
const Dotenv = require('dotenv-webpack');

const config = {
    entry: './src/index.js',
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname, 'dist'),
    },
    plugins: [
        new Dotenv()
    ]
};
  
module.exports = config;
