#include <stdio.h>
#include <stdlib.h>

#define FLAG "/flag"
#define READSIZE 1024

int main() {
	char buf[READSIZE] = {0};
	
	FILE *fp = fopen(FLAG, "rb");
	fgets(buf, READSIZE, fp);
	fclose(fp);

	puts(buf);

	return 0;
}
