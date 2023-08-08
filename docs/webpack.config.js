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
    ],
    module: {
        rules: [
            {
                test: /\.md$/,
                use: [
                {
                    loader: "html-loader",
                },
                {
                    loader: "markdown-loader",
                    options: {
                    // Pass options to marked
                    // See https://marked.js.org/using_advanced#options
                    },
                },
                ],
            },
        ],
    },
};
  
module.exports = config;
