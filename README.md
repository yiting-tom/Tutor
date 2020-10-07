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


# 變數&資料型態
## 1. 變數與常數
- 變數(variable) : 利利用宣告，將一定空間的記憶體給此變數，不管變數的值如何改變，它會一直佔用相同的記憶體空間。
> ``` c
> int i = 3;
> float f = 3.33;
> char ch = 'C';
> ```
- 常數(constant) : 值是固定的，如整數常數、字元常數...
> ``` c
> const int max = 65535;
> ```
<br>

## 2. 基本資料型態 (main1)
- 整數 : 表示整數值，可以區分為 short、int、long 與 long long（C99），配置的記憶體長度在不同編譯器上各不相同，可容納的大小各不相同
``` c
Type     size(bytes)    Range
short         2         -32,768 ~ 32,767         
int           4         -2,147,483,648 ~ 2,147,483,647
long          4         -9223372036854775808 ~ 9223372036854775807
```
- 浮點數 : 表示小數值，可以區分為 float、double 與 long double，越後面的型態使用的記憶體空間越大，精度也就越高
``` c
Type     size(bytes)    Range
float         4         1.2e-38 ~ 3.4e38
double        8         2.2e-308 ~ 1.8e308
long double   12        3.4e-4932 ~ 1.1e4932
```
- 字元 : 主要用來儲存字元資料，但沒有規定什麼是字元資料，也可用來儲存較小範圍的整數
``` c
Type     Size(bytes)       Range
char          1            0 ~ 255
```
- 補充 : 
    1. unsigned : 以上所有基本型態皆可使用 unsigned 修飾，使可用數值範圍為正數
    2. overflow : 如果儲存值超出這個範圍的話發生Overflow(溢位)

## 3. 變數命名
1. 不能使用關鍵字
2. 只有前 8 個字元為有效字元
3. 可使用英文字母、數字或底線
4. 變數名稱中間不可以有空白
5. 第一個字元不可為數字
6. 變數名稱要有意義，且長短適中
7. 大小寫有別

## 4. 資料型態轉換 (main2)
1. 指派轉換 : ``` x = 100;```
2. 算術轉換 : ```y = i * 5 + 7 / 23;```
3. 模式轉換 : ```i = (int) ( x + 0.9 );```
4. 函數轉換 : ```x = sum (a, b);```



# 基本運算子

## 1.算術運算子
> ``` c
> int a = 9, b = 4;
> 運算子  意義    用法    結果
> +       加      a+b     13
> -       減      a-b      5
> *       乘      a*b     36
> /       除      a/b      2
> %       餘      a%b      1
> 
> +=              a+=b    a=13;
> -=              a-=b    a=5;
> *=              ...     ...
> /=              ...     ...
> %=              ...     ...
> ```

## 2. 關係運算子
> ``` c
> int a = 9, b = 4;
> 運算子  意義        用法       結果
> >      大於         a>b       TRUE
> <      小於         a<b       FALSE
> >=     大於等於     a>=b      TRUE
> <=     小於等於     a<=b      FALSE
> ==     等於         a==b      FALSE
> !=     不等於       a!=b       TRUE
> ```

## 3. 邏輯運算子
> ``` c
> bool a = TRUE, b = FALSE;
> 運算子  意義     用法      結果
> &&      AND     a&&b     FALSE   
> ||      OR      a||b     TRUE
> !       NOT     !a       FALSE     
> ```

## 4. 遞增/遞減運算子
> i++/i-- : 此指令全部做完最後再將i加/減1並存回
> ++i/--i : 先將i加/減1後，再執行其他指令

## 5. 條件運算子
> 判斷條件 ? 指令1 : 指令2
> 意義 : 
> if(判斷條件) 指令1;
> else 指令2;

# 流程控制

## 1. if-else 敘述
1.  基本語法(main0.c)
> ``` c
> if (條件句) 
>     陳述句1;
> else
>     陳述句2;
> ```
2.  else-if-else語法(main1.c)
> ``` c
> if (條件句) {
>     陳述句1;
>     陳述句2;
> } else if (條件句二) {
>     陳述句3;
>     陳述句4;
> } else {
>     陳述句5;
>     陳述句6;
> }
> ```

## 2. switch 敘述
1. 基本語法(main2.c)
> ``` c
> switch (變數名稱或運算式) { 
>     case 符合數字或字元: 
>         陳述句一; 
>         break; 
>     case 符合數字或字元: 
>         陳述句二; 
>         break; 
>     default: 
>         陳述句三; 
> }
> ```

## 3. for 敘述
1. 基本語法(main3.c)
> ``` c
> for (初始變數; 判斷式; 遞增式) { 
>     陳述句一; 
>     陳述句二; 
> }
> ```

## 4. while 敘述
1. 基本語法(main4.c)
> ``` c
> while(條件式) { 
>     陳述句一; 
>     陳述句二; 
> }
> ```

2. do-while語法(main5.c)
> ``` c
> do { 
>     陳述句一; 
>     陳述句二; 
>     .... 
> } while(條件式);
> ```

## 5. break, continue, goto
1. break
> 離開目前 switch、for、while、do while 的區塊
2. continue
> 的作用與 break 類似，主要使用於迴圈，所不同的是 break 會結束區塊的執行，而 continue 只會結束接下來區塊中的陳述句，並跳回迴圈區塊的開頭繼續下一個迴圈，而不是離開迴圈

# 陣列

## 1. 一維陣列(main0)

1. 基本語法
``` c
int data[5] = {1};              /* 將所有元素值都設為 1 */
int num[] = {60,75,48,92};      /* 依照初值設定的個數決定陣列的大小 */
int student[10] = {1,2,3,4,5};  /* 初值個數少於宣告元素個數時，剩餘空間填 0 */

a = data[0] /* a get 1 */
data[0] = 1  /* data[0] get 1 */
```

## 2.二維陣列(main1)

1. 基本語法
``` c
int table[2][4] = {{1,2,3,4}, {5,6,7,8}};       /*2列4行*/
```

## 3. 字元陣列與字串(main2)
串就是一串文字，一個意義是指字元組成的陣列，最後加上一個空（null）字元 '\0'

# 指標

## 1. 指標與記憶體位置
變數提供具名稱的記憶體儲存空間
1. 變數新增
``` c
int *i_ptr;     /* 整數型態之指標變數 */
double *d_ptr;  /* 浮點數型態之指標變數 */
char *c_ptr;    /* 字元型態之指標變數 */
```
2. 指標運算子(main0.c)
> - 位址運算子 &：用來取得變數或陣列元素在記憶體中的位址
> - 依址取值運算子 *：用來取得指標所指向的記憶體位址的內容
``` c
int a = 10, b;
int *p;
p = &a;
b = *p;
*p = 20;
//執行結果: a is 20, b is 10
```
## 2. 指標的運算
1. 設定: 將等號右邊的值設定給左邊的指標變數
2. 加減: 針對各個資料型態的長度來處理位址的加減法運算
3. 差值: 計算兩個指標之間的距離,其單位為資料型態的長度
``` c
int a=10, b=20;
int *p1, *p2;
char ch='a', *pch;

/* 設定運算 */
p1 = &a; /* 將 a 的位址存放於 p1 */
p2 = &b; /* 將 b 的位址存放於 p2 */
pch = &ch; /* 將 ch 的位址存放於 pch */

/* 加減法運算 */
p1++; /* 將 p1 中的位址值加上 4 bytes (int 型態的大小) */
pch--; /* 將 pch 中的位址值減去 1 byte (char 型態的大小) */

/* 差值運算 */
/* 計算 p1 和 p2 相差的距離 (以 int 為單位的距離) */
sub = p1 – p2;
```

## 3. 指標與陣列 (main1, main2)
陣列可看成是指標的分身,陣列元素的排列可利用指標運算來存取

## 4. 指標陣列
陣列中存放的變數為指標變數,即為指標陣列
``` c
int i=10, j=28, k=34;
int* a[3];

a[0] = &j;
a[1] = &k;
a[2] = &i;
```
- 字串陣列 V.S. 指標陣列
``` c
//字串陣列
char name[3][10] = {"David", "Jane Wang", "Tom Lee"};
//指標陣列
char *name[3] = {“David”, “Jane Wang”, “Tom Lee”};
//利用指標陣列可節省浪費的記憶體空間
```

## 5. 多重指標(main3.c)
指標變數中存放另一指標變數位址
``` c
//雙重指標
int a = 1;
int* ap = &a;
int** app = &ap;
```

## 6. 動態配置記憶體(main4.c, main5.c)
- malloc(_size) and free(_var): 
> malloc 會配置 _size Bytes 的空間，並傳回該空間的位址, 若失敗則回傳NULL
- calloc(_size, type_size):
> calloc 配置完成後預設為型態的零值
- free(&var)
> free 會釋放 _var 的記憶體空間
``` c
/* 一維配置 */
int n=5;
int* p;
//要求5個sizeof(int)的空間,
//並轉換成 int* 的格式後,
//再傳給p
p = (int*) malloc( n * sizeof(int) );
free(p)

/* 二維配置 */
int row=3,col=5,i;
int** array;
array = (int**) malloc(row * sizeof(int*));
for (i=0; i<row; i++)
array[i] = (int*) malloc(col * sizeof(int));

/* calloc */
int *p = malloc(sizeof(int) * 1000);
int *p = calloc(1000, sizeof(int));
```

# 函式

## 1. 為何要函式化?
> 1. 使程式發展容易管理
> 2. 軟體再使用 (抽象化的技術, abstraction)
> 3. 避免重複撰寫相同的程式碼

## 2. 定義格式
> ``` c
> 回傳型態 含式名稱（引數）{
>     本地變數宣告
>     指令
>     回傳回傳值
> }
> ``` 
``` c
int sum(int a, int b) {
    int num;
    num = a + b;
    return num;
}
```

## 3. 函式原形
``` c
回傳型態 函式名稱 (引數型態);
```
``` c
int sum(int, int);
int sum(int a, int b);
```

## 4. 函式呼叫
``` c
/*函式原形*/
int sum(int, int);

/*main function*/
int main(void) {
    int a = 1, b= 2;
    /*sum 函式呼叫*/
    int c = sum(a, b);

    return 0;
}

/*函數定義*/
int sum(int a, int b) {
    int c;
    c = a + b;
    return c;
}
```

## 5. 遞迴函式 (main3.c, main4.c)
> 1. 自己呼叫自己,注意終止條件的設定
> 2. 用到大量的堆疊 (stack) 空間,容易造成記憶體不足
> 3. 可以改寫成迴圈形式

# 結構

## 1. 為何要結構化？
> 1. 可讀性
> 2. 相關聯的資料組織在一起

## 2. 定義格式
> ``` c
> struct 名稱 {
>     資料型態1 欄位名稱1;
>     資料型態2 欄位名稱2;
>     ...
> };
> ```
``` c
struct date {
    int year;
    char* month;
    int day;
};
```

## 3. 存取結構屬性(attribute)(main0.c)
> . dot運算子 : 結構變數.結構屬性
``` c
date.year = 2020;
date.month = "Apr.";
date.day = 1;

printf("year: %d", date.year);
printf("month: %s", date.month);
printf("day: %d", date.day);
```

## 4. 指定結構初始值(main1.c, main2.c)
> 照順序附值：{... , ... , ...... };
> 照欄位名稱附值：{.欄位名稱1 = ... , .欄位名稱2 = ... , ...... };
> 直接宣告結構實例：struct 結構名稱{內容} 實例名稱 = {附值內容}; 
``` c
struct date = {0000, "Jun.", 1};
struct date = {.year = 0000, .day = 1, .month = "Jun."};
struct date {
    int year;
    char* month;
    int day;
} today = {0000, "Jun.", 1};
```

## 5. typedef 定義別名(main3.c)
> typedef struct 結構名稱{內容} 結構別名
``` c
typedef struct date {
    int year;
    char* month;
    int day;
} Date;
```

## 6. 結構指標
a -> b : (*a).b 為一種擴充運算子
``` c
struct mydata student[10];
struct mydata *ptr = student; /* 結構陣列 */
/* 結構指標,初值為 student 陣列的起始位址 */
for (i=0;i<10;i++)
{
    printf("Name, Score:");
    scanf("%s, %d", (student+i)->name, &(student+i)->score);
    printf("%s got %d points!\n", ptr->name, ptr->score);
    ptr++;
}
```

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

# 字串處理
字串是一個字元陣列，最後一個字元以空字元 '\0' 作結尾

## 字串長度、複製、串接 (main0, main1, main2)
``` c
size_t strlen(const char *str); //獲取字串所含字元長度（不包括空字元）

char *strcpy( char *restrict dest, const char *restrict src ); //字串複製

char *strncpy( char *restrict dest, const char *restrict src, size_t count ); //複製字串中若干字元內容

char *strcat( char *restrict dest, const char *restrict src ); //串接兩個字串

char *strncat( char *restrict dest, const char *restrict src, size_t count ); //串接部份字串
```
- size_t 是 unsigned 型態，在大部份系統是定義為 unsigned int，但在 64 位元系統中可以是 unsigned long。strlen 會傳回字元陣列中第一個字元至空字元的長度值減 1

## 字串比較、搜尋 (main3, main4, main5, main6)
``` c
int strcmp( const char *lhs, const char *rhs ); //比較字串 str1 與 str2 的大小

int strncmp( const char *lhs, const char *rhs, size_t count ); //比較兩個字串中指定長度內的字元是否相同

char *strstr( const char* str, const char* substr ); //搜尋子字串

size_t strspn( const char *dest, const char *src ); //找出兩個字串中開始不匹配的地方

char *strchr( const char *str, int ch ); //找出字串中的指定字元第一次出現

char *strrchr( const char *str, int ch ); //strchr的反向搜尋

size_t strcspn( const char *dest, const char *src ); //找出一個字串中與另一個字串任何字元第一次匹配的索引位置

```

- strcmp(str1, str2) : 會比較字串 str1 與 str2 的大小，若相同就傳回 0，str1 大於 str2 則傳回大於 0 的值，小於則傳回小於 0 的值，比較的標準是依字典順序，例如若 str1 大於 str2，表示 str1 在字典中的順序是在 str2 之後。
- strstr(str1, str2) : 第一個參數是被搜尋字串，第二個參數是想要搜尋的子字串，如果沒找到子字串則傳回 NULL，如果搜尋到第一個符合的子字串，則傳回符合位置的指標，若想要得知子字串是在哪一個索引位置，則可以利用該指標減去字串（字元陣列）開頭的指標，得到的位移量即為符合的索引位置