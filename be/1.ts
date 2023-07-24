const url = "strevo.protab.cz";
const port = 7001;

const decoder = new TextDecoder();

const conn = await Deno.connect({ hostname: url, port });
const buf = new Uint8Array(1024);
await conn.read(buf);
console.log("Client - Response:", decoder.decode(buf));
buf.fill(0);

// create the buffer to send
const data = new Uint8Array(49);
data.fill(0);
const number = -559038737;
const byte1 = 0xff & number;
const byte2 = 0xff & (number >> 8);
const byte3 = 0xff & (number >> 16);
const byte4 = 0xff & (number >> 24);
data.set([byte1, byte2, byte3, byte4], 16);
data.set([0x0a], 48);
console.log(data);
Deno.writeFileSync("data.b", data);
await conn.write(data);
// Read response
await conn.read(buf);
console.log("Client - Response:", decoder.decode(buf));
conn.close();
