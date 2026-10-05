const baseConfig = require('./webpack.config.js');

// Development server config: bundles the demo app (src/demo) with React
// included (not externalized) and serves it from index.html.
module.exports = (env, argv) => {
    const config = baseConfig(env, {...argv, mode: 'development'});

    config.mode = 'development';
    config.entry = {main: './src/demo/index.js'};
    config.output.filename = 'output.js';
    config.output.library = undefined;
    config.output.libraryTarget = undefined;

    // Bundle react/react-dom for the standalone demo instead of expecting
    // them on window (Dash provides them in production, the demo does not).
    config.externals = undefined;

    config.devServer = {
        static: {
            directory: __dirname,
        },
        hot: true,
        open: true,
        port: 5080,
    };

    return config;
};
