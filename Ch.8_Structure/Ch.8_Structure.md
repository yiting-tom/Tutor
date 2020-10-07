[toc]

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