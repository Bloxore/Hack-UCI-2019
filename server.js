const net = require('net')

const hostname = '35.235.78.32';
const port = 22

let listeners = [];
let listenerID = 0;

const server = net.createServer((socket) => {

  let id = 0;
  let username = "Unknown";

  console.log("client connected");

  socket.on("data", (data) => {
    if (data.toString() == "LISTENER") {
      // Don't establish user
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

  socket.on("close", () => {
    console.log("User " + username + " has left.");
  })

  socket.on("error", () => {
    console.log("Something wack happened.");
  })

}).listen(port, hostname, () => {
  console.log("Listening.")
})
