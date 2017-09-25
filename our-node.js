var firebase = require("firebase");
var mysql = require('mysql');
var mesaj="";

var config = {
  apiKey: "AIzaSyBwT_xzetsYKEUDy-dOHny9MP3Y7xULdkg",
  authDomain: "android-chat-starter-199e0.firebaseapp.com",
  databaseURL: "https://android-chat-starter-199e0.firebaseio.com",
  storageBucket: "android-chat-starter-199e0.appspot.com",
};
firebase.initializeApp(config);
var database = firebase.database();
 firebase.database().ref('/mesajlar/telefon').once('value').then(function(snapshot) {
  mesaj = (snapshot.val() && snapshot.val()) || 'Sizi anlayamadim';
  console.log(mesaj);
  var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "mysql",
  database: "albaraka"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
  var sql = "INSERT INTO temp_node ( name) VALUES ('"+mesaj+"')";
  console.log(sql)
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("1 record inserted");
    process.exit();
  });
});

});
