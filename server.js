const net = require('net')

const hostname = '127.0.0.1';
const port = 3000

const server = net.createServer((socket) => {

  let username = "Unknown";

  console.log("client connected");

  socket.on("data", (data) => {
    if (data.toString() == "LISTENER") {
      // Don't establish user
    }
    else if (data.toString().split(" ")[0] == "USER") {
      username = data.toString().split(" ")[1];
      socket.write("WELCOME! " + username + "\r\n")
    } else {
      //This is a message
      console.log(username + ": " + data.toString());
    }
  })

}).listen(port, hostname, () => {
  console.log("Listening.")
})
