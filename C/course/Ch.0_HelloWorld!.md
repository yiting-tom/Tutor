[toc]

# C 程式結構
以下為Hello World的Source Code
``` c
#include <stdio.h>

int main(void) {
    printf("Hello World!\n");

    return 0;
}
```

1. __前置處理器指令 (Preprocessor direcctive)__
它告訴編譯器(Compiler)這個程式會用到標頭檔(Header file) stdio.h 裡定義的函式(Function)

``` c
#include <stdio.h>
```

2. __主函式(Main function)__
主函數為程式開始的位置，也是函數，而函數的組成如下
``` c
函數回傳類型 函數名稱(輸入參數類型 參數名稱, ...) {
     ... 
     return 函數回傳值; 
}
```
``` c
int main(void) {
    ...
    return 0;
}
```
- int         為函數回傳類型
- main        為函數名稱
- void        為不使用參數
- return      為回傳0作為函式的回傳值
