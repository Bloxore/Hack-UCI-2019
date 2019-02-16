const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

http.createServer(function(request,response){
  request.on("data", (msg) => {
    response.write(msg);
  });

  request.on("end", () => {
    response.end();
  })
}).listen(port, hostname);
