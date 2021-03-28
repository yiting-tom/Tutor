[toc]

# 檔案輸入輸出

## 檔案儲存在記憶體的形式
> 1. text file : 以 ASCII 碼儲存
> 2. binary file :以二進位的格式除存

## 檔案存取模式
> r  : 讀取舊檔
> w  : 覆寫新舊檔
> a  : 附加新舊檔
> r+ : 讀取、覆寫舊檔
> w+ : 讀取、覆寫新舊檔
> a+ : 讀取、附加新舊檔
> rb : 讀取二進位檔
> wb : 覆寫二進位檔
> ab : 附加二進位檔

## 檔案處理函數
1. 變數宣告：
``` c
FILE *file;
char ch;
char buffer[128];
```

``` c
file = fopen(“C:\abc.txt”, “r”);         // 開檔
fclose(file);                            // 關檔  
ch = getc(file);                         // 讀取字元    
putc(ch, file);                          // 寫入字元      
fget(buffer, 128, file);                 // 讀取字串
fputs(buffer, file);                     // 寫入字串
fprintf(file, “%c \n”, ch);              // 格式化輸出   
fscanf(file, “%c”, &ch);                 // 格式化輸入       
fread(buffer, sizeof(char), 128, file);  // 區塊輸入           
fwrite(buffer, sizeof(char), 128, file); // 區塊輸出           
while( !feof(file) ) ch = getc(file);    // 檢查是否結束       
if ( ferror(file) )printf(“error”);      // 檢查錯誤   
fseek(file, 128, SEEK_SET);              // 移動檔案指標位置   
```

## 命令列參數的使用 (main.c)
> 1. argc (argument count):記錄參數個數
> 2. argv (argument value):記錄參數值
``` c
main(argc, argv)
int argc;
char *argv[];
{
...
}
```
``` c
#include <stdio.h>
int main (int argc, char* argv[])
{
    int i;
    printf(“The value of argc is %d \n”, argc);
    for(i=0; i<argc; i++)
    printf(“argv[%d]=%s \n”, i, argv[i]);
    return 0;
}
```