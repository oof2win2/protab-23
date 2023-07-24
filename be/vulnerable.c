#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>


int main(int argc, char **argv){
	struct{
		char buffer[16];
		int32_t check;
	}locals;
	locals.check=0xabcdc3cf;
	printf("Zadej vstup\n");
	fflush(stdout);
	assert(fgets(locals.buffer, 512, stdin) != NULL); // read 512 bytes from stdin to locals.buffer, otherwise exit
	printf("%d\n", locals.check);
	if(locals.check == 0x79beef8b){
		printf("Pekny, tady mas heslo:\n");

		int fd = open("flag", O_CLOEXEC, O_RDONLY);
		char buf[64];
		ssize_t len = read(fd, &buf, sizeof(buf));
		buf[len] = '\0';
		printf("%s\n", &buf);
		close(fd);
	}
	else{
		printf("Nope, tohle nebyl spravny vstup. Hezky den preji!\n");
	}
	return 0;
}
