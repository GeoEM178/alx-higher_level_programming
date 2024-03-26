#!/usr/bin/node
const req_URL = process.argv[2];
const theReq = require('request');

theReq(req_URL, function (err, sss, dtata) {
  if (err) {
    console.log(err);
  } else if (sss.statusCode === 200) {
    const done = {};
    const all_tasks = JSON.parse(dtata);
    for (const i in all_tasks) {
      const task = all_tasks[i];
      if (task.completed === true) {
        if (!done[task.userId]) {
          done[task.userId] = 1;
        } else {
          done[task.userId]++;
        }
      }
    }
    console.log(done);
  } else {
    console.log('An error occured. Status code: ' + sss.statusCode);
  }
});
