const url = "strevo.protab.cz";
const port = 9431;

const listener = Deno.listenDatagram({
	hostname: "0.0.0.0",
	port: port,
	transport: "udp",
});

const dat = new TextEncoder().encode("GET PASSWORD".repeat(1));
const overflow = new TextEncoder().encode("GET PASSWORD".repeat(2));

listener.send(dat, { hostname: url, port: port, transport: "udp" });

// for (let i = 0; i < 100_000; i++) {
// 	listener.send(dat, {
// 		hostname: url,
// 		port: port,
// 		transport: "udp",
// 	});
// }

console.log("all sent");

for await (const [datagram] of listener) {
	const text = new TextDecoder().decode(datagram);
	console.log(text);
}
