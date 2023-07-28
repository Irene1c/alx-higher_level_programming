#!/usr/bin/node

// script that computes the number of tasks completed by user id

const request = require('request');

const userUrl = 'https://jsonplaceholder.typicode.com/users';

const userIds = [];
request.get(userUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const user = JSON.parse(body);
    for (let u = 0; u < user.length; u++) {
      userIds.push(user[u].id);
    }

    request.get(process.argv[2], (error, response, body) => {
      if (error) {
        console.error(error);
      } else {
        const data = JSON.parse(body);
        const aDict = {};
        for (let i = 0; i < userIds.length; i++) {
          let count = 0;
          for (let a = 0; a < data.length; a++) {
            if (userIds[i] === (data[a].userId) && data[a].completed) {
              count++;
            }
          }
          aDict[userIds[i]] = count;
        }
        console.log(aDict);
      }
    });
  }
});
