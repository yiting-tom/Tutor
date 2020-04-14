[toc]

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
>malloc 會配置 _size Bytes 的空間，並傳回該空間的位址, 若失敗則回傳NULL

>free 會釋放 _var 的記憶體空間
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
```