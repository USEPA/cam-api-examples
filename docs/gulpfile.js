/* gulpfile.js */

const uswds = require("@uswds/compile");

/**
 * USWDS version
 */

uswds.settings.version = 3;

/**
 * Path settings
 * Set as many as you need
 */

uswds.paths.dist.css = './dist/assets/css';
uswds.paths.dist.fonts = './dist/assets/fonts';
uswds.paths.dist.js = './dist/assets/js';
uswds.paths.dist.theme = './dist/sass';

/**
 * Exports
 * Add as many as you need
 */

exports.init = uswds.init;
exports.compile = uswds.compile;