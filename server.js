'use strict';

const net = require('net')

const hostname = '10.168.0.2';
//const hostname = 'localhost';
const port = 4000

let listeners = [];
let listenerID = 0;

let messages = [];

class Chat {
  constructor(message, username) {
    this.message =  message;
    this.username = username;
  }
}

function writeChatToListeners(message, username = "SERVER") {
  let chat = new Chat(message, username);
  messages.push(chat);

  let rawOutput = JSON.stringify(messages);

  for (let i = 0; i < listeners.length; i++) {
    listeners[i].write(rawOutput + "\r\n");
  }
}

const server = net.createServer((socket) => {

  let id = 0;
  let username = "Unknown";

  console.log("client connected");

  socket.on("data", (data) => {
    if (data.toString() == "LISTENER") {
      // Don't establish user
      // TODO: Remove sockets from list on exit
      socket.id = listenerID++;
      socket.chat_type = "listener";
      listeners.push(socket);
    }
    else if (data.toString().split(" ")[0] == "USER") {
      let userData = data.toString().split(" ");
      username = "";
      for (let i = 1; i< userData.length; i++) {
        username += userData[i];
        if (i < userData.length - 1) {
          username += "_";
        }
      }
      // For individual users only!
      socket.write("WELCOME! " + username + "\r\n")

      writeChatToListeners("User " + username + " has joined.\r\n");
    } else {
      //This is a message
      console.log(username + ": " + data.toString());

      writeChatToListeners(data.toString(), username);
    }
  })

  socket.on("close", () => {
    if (socket.chat_type && socket.chat_type == "listener") {
      for (let i = 0; i < listeners.length; i++) {
        if (listeners[i].id == socket.id) {
          listeners.splice(i, 1);
        }
      }
      console.log("Removed listener. There are " + listeners.length + " listeners.")
    } else {
      console.log("User " + username + " has left.");
      writeChatToListeners("User " + username + " has left.\r\n");
    }
  })

  socket.on("error", () => {
    console.log("Something wack happened.");
  })

}).listen(port, hostname, () => {
  console.log("Listening.")
})
