[toc]

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