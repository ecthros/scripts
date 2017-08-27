#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char *argv[]) {
	if(argc != 3) {
		printf("Usage: ./client <color> <IP of scorebot>\n");
		exit(1);
	}
	if(getuid() != 0) {
		printf("You can only claim this machine as a root user.\n");
		exit(1);
	}
	printf("Attempting to claim for team %s to scorebot at IP %s\n", argv[1], argv[2]);
	char cmdbuf[256];
	snprintf(cmdbuf, sizeof(cmdbuf), "ip=`ip addr | grep inet[^6] | grep -v \"127\\..*\" | head -1 | grep -o \"10\\.[0-9]\\+\\.[0-9]\\+\\.[0-9]\\+\" | head -1`; curl --data \"team=%s,ip=$ip\" %s:8001", argv[1], argv[2]);
	system(cmdbuf);

}
