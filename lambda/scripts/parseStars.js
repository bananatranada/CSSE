// CSV to map[star] -> 'lat,long'
var fs = require('fs');
var path = require('path');

var csvFile = process.env.argv[1];
