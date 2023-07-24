import brotliPromise from "https://esm.sh/brotli-wasm@2.0.0"; // Import the default export
import { readableStreamFromReader } from "https://deno.land/std@0.160.0/streams/mod.ts";

const brotli = await brotliPromise; // Import is async in browsers due to wasm requirements!

const file = await Deno.open("./03.b", { read: true });
const inputStream = readableStreamFromReader(file);

// You can use whatever stream chunking size you like here, depending on your use case:
const OUTPUT_SIZE = 512;

const decompressStream = new brotli.DecompressStream();
const decompressionStream = new TransformStream({
	transform(chunk, controller) {
		let resultCode;
		let inputOffset = 0;

		// Decompress this chunk, producing up to OUTPUT_SIZE output bytes at a time, until the
		// entire input has been decompressed.

		do {
			const input = chunk.slice(inputOffset);
			const result = decompressStream.decompress(input, OUTPUT_SIZE);
			controller.enqueue(result.buf);
			resultCode = result.code;
			inputOffset += result.input_offset;
		} while (resultCode === brotli.BrotliStreamResultCode.NeedsMoreOutput);
		if (
			resultCode !== brotli.BrotliStreamResultCode.NeedsMoreInput &&
			resultCode !== brotli.BrotliStreamResultCode.ResultSuccess
		) {
			controller.error(`Brotli decompression failed with code ${resultCode}`);
		}
	},
	flush(controller) {
		controller.terminate();
	},
});

const textDecoderStream = new TextDecoderStream();

const outputStream = new WritableStream({
	write(chunk) {
		console.log(chunk);
	},
});

await inputStream
	.pipeThrough(decompressionStream)
	.pipeThrough(textDecoderStream)
	.pipeTo(outputStream);
