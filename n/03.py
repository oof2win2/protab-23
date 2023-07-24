import brotli

def decompress_chunks(input_data, chunk_size=4096):
	decompressor = brotli.Decompressor()
	offset = 0
	while offset < len(input_data):
		chunk = input_data[offset:offset+chunk_size]
		offset += chunk_size
		yield decompressor.process(chunk)
	yield decompressor.finish()

with open('03.b', 'rb') as f:
	# chunk = f.readline()
	dat = decompress_chunks(f.read())
	print(*dat)
	