#include <dlfcn.h>
#include <stdio.h>

int main() {
    void *handle = dlopen("./libconundrum.so", RTLD_LAZY);
    if (!handle) {
        printf("Error: %s\n", dlerror());
        return 1;
    }

    // Thay "function_name" bằng tên hàm bạn tìm thấy từ nm hoặc IDA
    void (*func)() = dlsym(handle, "flag_002d91ef3cb4b19a59213f704f86295a");
    if (!func) {
        printf("Error: %s\n", dlerror());
        return 1;
    }

    func(); // Gọi hàm
    dlclose(handle);
    return 0;
}
