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
    char* day;
};
```

## 3. 存取結構屬性(attribute)(main0.c)
> . dot運算子
``` c
date.year = 2020;
date.month = "Apr.";
date.day = "Wen.";

printf("year: %d", date.year);
printf("month: %s", date.year);
printf("day: %s", date.year);
```

## 4. 指定結構初始值(main1.c, main2.c)
> 照順序附值：{... , ... , ...... };
> 照欄位名稱附值：{.欄位名稱1 = ... , .欄位名稱2 = ... , ...... };
> 直接宣告結構實例：struct 結構名稱{內容} 實例名稱 = {附值內容}; 
``` c
struct date = {0000, "Jun.", "Mon."};
struct date = {.year = 0000, .month = "Jun.", .day = "Mon."};
struct date {
    int year;
    char* month;
    char* day;
} today = {0000, "Jun.", "Mon."};
```

## 5. typedef 定義別名(main3.c)
> typedef struct 結構名稱{內容} 結構別名
``` c
typedef struct date {
    int year;
    char* month;
    char* day;
} Date;
```