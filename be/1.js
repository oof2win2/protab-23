const net = require("net")

const client = new net.Socket();
client.connect(7000, 'strevo.protab.cz', function() {
	console.log('Connected');
});

client.on('data', function(data) {
	console.log('Received: ' + data);
	client.write(new TextEncoder().encode("0123456789abcdef0a"))
});

client.on('close', function() {
	console.log('Connection closed');
});