const net = require('net')

const hostname = '127.0.0.1';
const port = 3000

let listeners = [];
let listenerID = 0;

const server = net.createServer((socket) => {

  let id = 0;
  let username = "Unknown";

  console.log("client connected");

  socket.on("data", (data) => {
    if (data.toString() == "LISTENER") {
      // Don't establish user
      socket.write("Welcome listener.\r\n");

      // TODO: Remove sockets from list on exit
      socket.id = listenerID++;
      listeners.push(socket);
    }
    else if (data.toString().split(" ")[0] == "USER") {
      username = data.toString().split(" ")[1];
      socket.write("WELCOME! " + username + "\r\n")
    } else {
      //This is a message
      console.log(username + ": " + data.toString());

      for (let i = 0; i < listeners.length; i++) {
        listeners[i].write(username + ": " + data.toString() + "\r\n");
      }
    }
  })

}).listen(port, hostname, () => {
  console.log("Listening.")
})
