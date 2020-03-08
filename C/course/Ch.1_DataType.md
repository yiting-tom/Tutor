[toc]


# 資料型態
1. __變數與常數__
- 變數(variable) : 利利用宣告，將一定空間的記憶體給此變數，不管變數的值如何改變，它會一直佔用相同的記憶體空間。
> ``` c
> int i = 3;
> float f = 3.33;
> char ch = 'C';
> ```
- 常數(constant) : 值是固定的，如整數常數、字元常數...
``` c
const int max = 65535;
```
<br>

2. __基本資料型態__
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
