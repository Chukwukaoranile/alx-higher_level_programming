#!/usr/bin/node
/**
 * A script that imports a dictionary of occurrences by user id
 * and computes a dictionary of user ids by occurrence.
 * @module Provide functions to write to a file from
 * multiple sources
 */

// Module to interact with system files
const fs = require('fs');

// Validate number of arguments
if (process.argv.length < 4) {
  console.error(
    '\x1b[38;2;255;119;119m%s\x1b[0m',
    'Error: Number of arguments is invalid'
  );
  process.exit(-1);
}
// Destructure
const [target, ...sourceFiles] = process.argv.splice(2).reverse();

/**
 * Stating the destination.
 * source files
 * @param { Array } sourceFiles
 * @param { String } target.
 * @return { Number } 1 if successful. -1 if it fails
 */
function readToWrite (filesList = sourceFiles.reverse(), targetFile = target) {
  try {
    let data = '';

    // Reading from multiple sources
    // Store variables
    for (const pathFile of filesList) {
      data += fs.readFileSync(pathFile, 'utf8');
    }

    // Write to te destination file
    fs.writeFileSync(targetFile, data);

    return 1;
  } catch (err) {
    console.error(err);
  }
}

readToWrite();

module.exports = { readToWrite };

