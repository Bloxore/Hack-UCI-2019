const net = require('net')

const hostname = '127.0.0.1';
const port = 3000

const server = net.createServer((socket) => {

  console.log("client connected");

  socket.on("data", (data) => {
    if (data.toString() == "LISTENER") {
      // Don't establish user
    }
    else if (data.toString().split(" ")[0] == "USER") {
      socket.write("WELCOME!\r\n")
    }
  })

}).listen(port, hostname, () => {
  console.log("Listening.")
})
