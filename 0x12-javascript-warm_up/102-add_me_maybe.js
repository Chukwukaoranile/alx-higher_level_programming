#!/usr/bin/node
exports.addMeMaybe = function (addMe, theFunction) {
  theFunction.call(this, addMe + 1);
};
