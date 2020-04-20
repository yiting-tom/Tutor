[toc]

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
