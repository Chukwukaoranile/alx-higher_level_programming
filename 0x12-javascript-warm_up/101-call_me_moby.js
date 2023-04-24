#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let moby = 0; moby < x; moby++) {
    theFunction();
  }
};
