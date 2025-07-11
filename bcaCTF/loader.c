#include <stdio.h>
#include <dlfcn.h>

int main() {
    void *handle = dlopen("./libconundrum.so", RTLD_LAZY);
    if (!handle) {
        printf("dlopen failed: %s\n", dlerror());
        return 1;
    }

    void (*main_func)() = dlsym(handle, "main");  // hoặc thử "flag_..." nếu muốn
    if (!main_func) {
        printf("dlsym failed: %s\n", dlerror());
        return 1;
    }

    main_func();  // Gọi hàm chính
    return 0;
}
