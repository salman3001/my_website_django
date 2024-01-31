// moveHtmlFile.js
import fs from 'fs'
import path from 'path';

const sourcePath = 'core/static/core/index.html';  // Adjust the source path
const destinationPath = 'core/templates/core/base.html';  // Adjust the destination path

fs.renameSync(path.resolve(sourcePath), path.resolve(destinationPath));

console.log(`Renamed ${sourcePath} and copy to ${destinationPath}`);