#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/';
let mj = parseInt(process.argv[2], 10);
let characters = [];

request(url, function (err, response, body) {
  if (err == null) {
    const resp = JSON.parse(body);
    const results = resp.results;
    if (mj < 4) {
      mj += 3;
    } else {
      mj -= 3;
    }
    for (let i = 0; i < results.length; i++) {
      if (results[i].episode_mj === mj) {
        characters = results[i].characters;
        break;
      }
    }
    for (let j = 0; j < characters.length; j++) {
      request(characters[j], function (err, response, body) {
        if (err == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
