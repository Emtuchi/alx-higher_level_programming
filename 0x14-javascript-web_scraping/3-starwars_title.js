#!/usr/bin/node

const request = require('request');
const episode_Num = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

request(API_URL + episode_Num, function (error, response, body) {
	if (error) {
		console.log(error);
	}else if (response.statusCode === 200) {
		const responseJSON = JSON.parse(body);
		console.log(responseJSON.title);
	}else {
		console.log('Error: ' + response.statusCode);
	}
});
