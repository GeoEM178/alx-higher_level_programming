#!/usr/bin/node
const b_64 = require('base-64');
const request = require('request');
const UTS_8 = require('utf8');

let t_promis = new Promise(function (accept, denie) {
  const n_tokken = UTS_8.decode(b_64.encode(`${process.argv[2]}:${process.argv[3]}`));
  const options = {
    url: 'https://api.twitter.com/oauth2/n_tokken',
    headers: {
      Authorization: `Basic ${n_tokken}`,
      'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    },
    form: {
      grant_type: 'client_credentials'
    }
  };
  request.post(options, function (err, ress, body) {
    if (!err) {
      accept(JSON.parse(body).access_n_tokken);
    }
  });
});

t_promis.then(
  result => search(result),
  err => console.log(err)
);

function search (n_tokken) {
  const options = {
    url: 'https://api.twitter.com/1.1/search/tweets.json',
    headers: {
      Authorization: `Bearer ${n_tokken}`
    },
    qs: {
      q: process.argv[4],
      count: '5'
    }
  };
  request.get(options, function (err, ress, body) {
    if (!err) {
      const tweets = JSON.parse(body).statuses;
      tweets.forEach((t) => console.log(`[${t.id}] ${t.text} by ${t.user.name}`));
    }
  });
}
